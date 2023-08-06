"""
Tarkus - IDA Plugin Manager

Usage:
    tarkus.py init [<ida-path>]
    tarkus.py repo [<repo-path>]
    tarkus.py install <plugin-name> [-l|-g]
    tarkus.py remove <plugin-name>
    tarkus.py freeze
    tarkus.py update <plugin-name>
"""
from itertools import imap
import stat
from tempfile import mkdtemp
from awesome.context import redirect_stdout
import docopt
import pip
import git
import os
import shutil
import yaml
from attrdict import AttrMap

PLUGIN_DEFINITION_NAME = "tarkus.yml"

PLUGINS_DIR_NAME = "plugins"

TARKUS_BASE_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "tarkus.base.yml")
TARKUS_CONFIG_PATH = os.path.join(os.getenv("APPDATA"), "Tarkus", "tarkus.yml")

PLUGIN_TEMPLATE = ("name: {name}  # The name of the plugin. Preferable lowercase.\n"
                   "root: .  # Relative root directory of the plugin.\n"
                   "include: []  # All non-python files you need to include.\n"
                   "requirements: null  # Name of the pip-requirements file for your plugin, if one exists.")


class TarkusException(Exception):
    pass


class TarkusError(TarkusException):
    pass


class PluginAlreadyInstalledError(TarkusError):
    pass


class PluginFileExistsError(TarkusError):
    pass


class PluginNotFoundError(TarkusError):
    pass


class FailedCloningRepo(TarkusError):
    pass


class PluginNotInRepo(TarkusError):
    pass


def install_requirements(requirements):
    with redirect_stdout():
        try:
            pip.main(["install", "-r", requirements])
        except SystemExit:
            pass


class Config(object):
    def __init__(self, path, base_path):
        self._path = path

        with open(base_path, "rb") as f:
            base_config = yaml.safe_load(f)

        with open(self._path, "rb") as f:
            config = yaml.safe_load(f)

        full_config = base_config

        try:
            full_config.update(config)
        except:
            pass

        self._config = AttrMap(full_config)

    def __getattr__(self, name):
        return getattr(self._config, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            return super(Config, self).__setattr__(name, value)

        return setattr(self._config, name, value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = yaml.safe_dump(dict(self._config), default_flow_style=False)
        with open(self._path, "wb") as f:
            f.write(data)


def remove_dir(temp_path):
    def onerror(func, path, exc_info):
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
            func(path)
        else:
            raise

    shutil.rmtree(temp_path, onerror=onerror)


class Tarkus(object):
    def __init__(self):
        super(Tarkus, self).__init__()

        self._config = Config(TARKUS_CONFIG_PATH, TARKUS_BASE_CONFIG_PATH)

    @property
    def config(self):
        return self._config

    @property
    def plugins_path(self):
        return os.path.join(self.config.ida_path, PLUGINS_DIR_NAME)

    def init(self, ida_path=None):
        if ida_path:
            if not os.path.exists(ida_path):
                print "Path does not exist."
                return

            with self.config:
                self.config.ida_path = ida_path

            print "IDA path successfully set."

        else:
            print "IDA Path: {}".format(self.config.ida_path)

    def repo(self, repo_path=None):
        if not repo_path:
            print "Repo Parg: {}".format(self.config.repo_path)
            return

        with self.config:
            self.config.repo_path = repo_path

        print "Repo path successfully set."

    def _install_from_git(self, url, name=None):
        temp_path = self._get_temp_path()
        print "Cloning plugin..."
        try:
            git.Repo.clone_from(url, temp_path)
        except git.GitCommandError:
            raise FailedCloningRepo("Failed cloning from {!r}".format(url))

        config_path = os.path.join(temp_path, PLUGIN_DEFINITION_NAME)

        self._install_plugin(config_path, url, name=name)

        remove_dir(temp_path)

    def _install_from_repo(self, name):
        temp_path = self._get_temp_path()
        try:
            git.Repo.clone_from(self.config.repo_path, temp_path)
        except git.GitCommandError:
            raise FailedCloningRepo("Failed cloning from {!r}".format(self.config.repo_path))

        # Read the repo
        with open(os.path.join(temp_path, "repo.yml")) as f:
            repo = yaml.safe_load(f)

        remove_dir(temp_path)

        try:
            url = repo[name]
        except KeyError:
            raise PluginNotInRepo("Plugin {!r} does not exist in repository.".format(name))

        print "Plugin found in repository: {}".format(url)

        self._install_from_git(url, name=name)

    def install(self, plugin_name, local, git):
        if local:
            print "Installing from local path {!r}".format(plugin_name)
            if os.path.exists(plugin_name):
                self._install_plugin(plugin_name)

        elif git:
            print "Installing plugin from git at {!r}".format(plugin_name)
            self._install_from_git(plugin_name)

        else:
            print "Looking for {!r} in repository".format(plugin_name)
            self._install_from_repo(plugin_name)

        print "Installation completed successfully."

    def _install_plugin(self, plugin_path, update_url=None, name=None):
        # Read the plugin definition
        print "Installing plugin..."
        with open(plugin_path, "rb") as f:
            plugin_definition = yaml.safe_load(f)

        try:
            plugin = AttrMap(plugin_definition)
            self._install_plugin_internal(plugin, plugin_path, update_url)
        except:
            if name:
                for temp_plugin in imap(AttrMap, plugin_definition):
                    if temp_plugin.name == name:
                        plugin = temp_plugin
                        break
                else:
                    raise PluginNotFoundError(
                        "Plugin names {!r} not found in {!r}.".format(name, update_url or plugin_path))

                self._install_plugin_internal(plugin, plugin_path, update_url)

            else:
                for plugin in imap(AttrMap(plugin_definition)):
                    self._install_plugin_internal(plugin, plugin_path, update_url)

    def _install_plugin_internal(self, plugin, plugin_path, update_url):
        # Make sure it is not already installed
        if plugin.name in self.config.plugins:
            raise PluginAlreadyInstalledError("Plugin {!r} already installed.".format(plugin.name))

        # Gather all plugin files
        paths = []
        plugin.root = os.path.join(os.path.dirname(plugin_path), plugin.root)
        for root, dirs, files in os.walk(plugin.root):
            for name in files:
                path = os.path.join(root, name)
                if name.endswith(".py") or os.path.relpath(path, plugin.root) in plugin.include:
                    paths.append(path)

        copy_map = {}
        for path in paths:
            rel_path = os.path.relpath(path, plugin.root)
            target_path = os.path.join(self.plugins_path, rel_path)
            copy_map[path] = target_path

        # Make sure they do not exist in IDA's plugins directory
        for target_path in copy_map.itervalues():
            if os.path.exists(target_path):
                rel_path = os.path.relpath(target_path, self.plugins_path)
                raise PluginFileExistsError("File {!r} already exists in the plugins directory.".format(rel_path))

        # Add all files to the config
        with self.config:
            self.config.plugins[plugin.name] = dict(
                path=plugin_path,
                files=copy_map.values(),
                name=plugin.name,
                update_url=update_url,
            )
            # TODO: add version logging here too
        # Copy all files to the plugins directory
        for source, target in copy_map.iteritems():
            shutil.copy(source, target)

        # Install dependencies
        if plugin.requirements:
            requirements = os.path.join(plugin.root, plugin.requirements)
            install_requirements(requirements)

    def freeze(self):
        for plugin in self.config.plugins.itervalues():
            plugin = AttrMap(plugin)
            print "{}: {}".format(plugin.name, plugin.path)

    def remove(self, name):
        print "Removing plugin {}".format(name)
        try:
            plugin = AttrMap(self.config.plugins[name])

            for path in plugin.files:
                os.unlink(path)

            with self.config:
                del self.config.plugins[name]

        except KeyError:
            raise PluginNotFoundError("Plugin {!r} not found.".format(name))

        print "Plugin successfully removed."

    def _get_temp_path(self):
        return mkdtemp("tarkus")

    def update(self, plugin_name):
        plugin = AttrMap(self.config.plugins[plugin_name])

        if plugin.update_url:
            self.remove(plugin_name)
            self._install_from_git(plugin.update_url, plugin.name)


def main():
    # Make sure the config exists
    if not os.path.exists(TARKUS_CONFIG_PATH):
        config_dir = os.path.dirname(TARKUS_CONFIG_PATH)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        open(TARKUS_CONFIG_PATH, "wb")

    args = docopt.docopt(__doc__)

    tarkus = Tarkus()

    if args["init"]:
        tarkus.init(args["<ida-path>"])

    if args["repo"]:
        tarkus.repo(args["<repo-path>"])

    elif args["install"]:
        config = args["<plugin-name>"]
        local = args["-l"]
        git = args["-g"]
        tarkus.install(config, local, git)

    elif args["remove"]:
        name = args["<plugin-name>"]
        tarkus.remove(name)

    elif args["freeze"]:
        tarkus.freeze()

    elif args["update"]:
        name = args["<plugin-name>"]
        tarkus.update(name)


if __name__ == '__main__':
    main()
