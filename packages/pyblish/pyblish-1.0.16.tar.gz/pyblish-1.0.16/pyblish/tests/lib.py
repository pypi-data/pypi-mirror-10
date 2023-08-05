import os

import pyblish
import pyblish.cli
import pyblish.plugin


# Setup
HOST = 'python'
FAMILY = 'test.family'

REGISTERED = pyblish.plugin.registered_paths()
PACKAGEPATH = pyblish.lib.main_package_path()
PLUGINPATH = os.path.join(PACKAGEPATH, 'tests', 'plugins')
ENVIRONMENT = os.environ.get("PYBLISHPLUGINPATH", "")


def ctx():
    """Return current Click context"""
    return pyblish.cli._ctx


def context():
    """Return current context"""
    return ctx().obj["context"]


def setup():
    """Disable default plugins and only use test plugins"""
    pyblish.config = pyblish.plugin.Config()
    pyblish.config['paths'] = []

    pyblish.plugin.deregister_all()
    pyblish.plugin.register_plugin_path(PLUGINPATH)


def setup_failing():
    """Expose failing plugins to discovery mechanism"""
    setup()

    # Append failing plugins
    failing_path = os.path.join(PLUGINPATH, 'failing')
    pyblish.plugin.register_plugin_path(failing_path)


def setup_duplicate():
    """Expose duplicate plugins to discovery mechanism"""
    pyblish.plugin.deregister_all()

    config = pyblish.plugin.Config()
    config['paths'] = []

    for copy in ('copy1', 'copy2'):
        path = os.path.join(PLUGINPATH, 'duplicate', copy)
        pyblish.plugin.register_plugin_path(path)


def setup_wildcard():
    pyblish.plugin.deregister_all()

    config = pyblish.plugin.Config()
    config['paths'] = []

    wildcard_path = os.path.join(PLUGINPATH, 'wildcards')
    pyblish.plugin.register_plugin_path(wildcard_path)


def setup_invalid():
    """Expose invalid plugins to discovery mechanism"""
    pyblish.plugin.deregister_all()
    failing_path = os.path.join(PLUGINPATH, 'invalid')
    pyblish.plugin.register_plugin_path(failing_path)


def setup_full():
    """Expose a full processing chain for testing"""
    setup()
    pyblish.plugin.deregister_all()
    path = os.path.join(PLUGINPATH, 'full')
    pyblish.plugin.register_plugin_path(path)


def setup_echo():
    """Plugins that output information"""
    pyblish.plugin.deregister_all()

    config = pyblish.plugin.Config()
    config['paths'] = []

    path = os.path.join(PLUGINPATH, 'echo')
    pyblish.plugin.register_plugin_path(path)


def teardown():
    """Restore previously REGISTERED paths"""

    # Clear singletons
    pyblish.plugin.Config._instance = None

    pyblish.plugin.deregister_all()
    for path in REGISTERED:
        pyblish.plugin.register_plugin_path(path)

    os.environ["PYBLISHPLUGINPATH"] = ENVIRONMENT


# CLI Fixtures


def setup_cli():
    os.environ["PYBLISHPLUGINPATH"] = PLUGINPATH


def setup_failing_cli():
    """Expose failing plugins to CLI discovery mechanism"""
    # Append failing plugins
    failing_path = os.path.join(PLUGINPATH, 'failing_cli')
    os.environ["PYBLISHPLUGINPATH"] = failing_path
