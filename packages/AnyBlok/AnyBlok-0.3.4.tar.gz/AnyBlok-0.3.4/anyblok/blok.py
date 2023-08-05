# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok project
#
#    Copyright (C) 2014 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from pkg_resources import iter_entry_points
import anyblok
from anyblok._imp import ImportManager
from .logging import log
from anyblok.environment import EnvironmentManager
from time import sleep
from sys import modules
from os.path import dirname
from logging import getLogger
from os.path import join

logger = getLogger(__name__)


@anyblok.Declarations.register(anyblok.Declarations.Exception)
class BlokManagerException(Exception):
    """ Simple exception to BlokManager """

    def __init__(self, *args, **kwargs):
        EnvironmentManager.set('current_blok', None)
        super(BlokManagerException, self).__init__(*args, **kwargs)


class BlokManager:
    """ Manage the bloks for one process

    A blok has a `setuptools` entrypoint, this entry point is defined
    by the ``bloks_groups`` attribute in the first load

    The ``bloks`` attribute is a dict with all the loaded entry points

    Use this class to import all the bloks in the entrypoint::

        BlokManager.load('AnyBlok')

    """

    bloks = {}
    bloks_groups = None
    ordered_bloks = []
    auto_install = []
    importers = {}

    @classmethod
    def list(cls):
        """ Return the ordered bloks

        :rtype: list of blok name ordered by loading
        """
        return cls.ordered_bloks

    @classmethod
    def has(cls, blok):
        """ Return True if the blok is loaded

        :param blok: blok name
        :rtype: bool
        """
        return blok and blok in cls.ordered_bloks or False

    @classmethod
    def get(cls, blok):
        """ Return the loaded blok

        :param blok: blok name
        :rtype: blok instance
        :exception: BlokManagerException
        """
        if not cls.has(blok):
            raise BlokManagerException('%r not found' % blok)

        return cls.bloks[blok]

    @classmethod
    def set(cls, blokname, blok):
        """ Add a new blok

        :param blokname: blok name
        :param blok: blok instance
        :exception: BlokManagerException
        """
        if cls.has(blokname):
            raise BlokManagerException('%r already present' % blokname)

        cls.bloks[blokname] = blok
        cls.ordered_bloks.append(blokname)

    @classmethod
    @log(logger)
    def reload(cls):
        """ Reload the entry points

        Empty the ``bloks`` dict and use the ``bloks_groups`` attribute to
        load bloks
        :exception: BlokManagerException
        """
        if cls.bloks_groups is None:
            raise BlokManagerException(
                """You must use the ``load`` classmethod before using """
                """``reload``""")

        bloks_groups = []
        bloks_groups += cls.bloks_groups
        cls.unload()
        cls.load(*bloks_groups)

    @classmethod
    @log(logger)
    def unload(cls):
        """ Unload all the bloks but not the registry """
        cls.bloks = {}
        cls.ordered_bloks = []
        cls.bloks_groups = None
        cls.auto_install = []

    @classmethod
    @log(logger)
    def load(cls, *bloks_groups):
        """ Load all the bloks and import them

        :param bloks_groups: Use by ``iter_entry_points`` to get the blok
        :exception: BlokManagerException
        """
        if not bloks_groups:
            raise BlokManagerException("The bloks_groups mustn't be empty")

        cls.bloks_groups = bloks_groups

        if EnvironmentManager.get('current_blok'):
            while EnvironmentManager.get('current_blok'):
                sleep(0.1)

        EnvironmentManager.set('current_blok', 'start')

        bloks = []
        for bloks_group in bloks_groups:
            count = 0
            for i in iter_entry_points(bloks_group):
                count += 1
                try:
                    blok = i.load()
                    cls.set(i.name, blok)
                    blok.name = i.name
                    bloks.append((blok.priority, i.name))
                except Exception as e:
                    raise BlokManagerException(str(e))

            if not count:
                raise BlokManagerException(
                    "Invalid bloks group %r" % bloks_group)

        # Empty the ordered blok to reload it depending on the priority
        cls.ordered_bloks = []
        bloks.sort()

        def get_need_blok(blok):
            if cls.has(blok):
                return True

            if blok not in cls.bloks:
                return False

            for required in cls.bloks[blok].required:
                if not get_need_blok(required):
                    raise BlokManagerException(
                        "Not %s required bloks found" % required)

            for optional in cls.bloks[blok].optional:
                get_need_blok(optional)

            cls.ordered_bloks.append(blok)
            EnvironmentManager.set('current_blok', blok)

            if not ImportManager.has(blok):
                # Import only if not exist don't reload here
                mod = ImportManager.add(blok)
                mod.imports()
            else:
                mod = ImportManager.get(blok)
                mod.reload()

            if cls.bloks[blok].autoinstall:
                cls.auto_install.append(blok)

            return True

        try:
            while bloks:
                blok = bloks.pop(0)[1]
                get_need_blok(blok)

        finally:
            EnvironmentManager.set('current_blok', None)

    @classmethod
    def getPath(cls, blok):
        """ Return the path of the blok

        :param blok: blok name in ``ordered_bloks``
        :rtype: absolute path
        """
        blok = cls.get(blok)
        return dirname(modules[blok.__module__].__file__)

    @classmethod
    def add_importer(cls, key, cls_name):
        """ Add a new importer

        :param key: key of the importer
        :param cls_name: name of the model to import
        """
        cls.importers[key] = cls_name

    @classmethod
    def has_importer(cls, key):
        """ Check if an importer  """
        return True if key in cls.importers else False

    @classmethod
    def get_importer(cls, key):
        """ Get the importer class name

        :param key: key of the importer
        :rtype: name of the model to import
        :exception: BlokManagerException
        """
        if not cls.has_importer(key):
            raise anyblok.Declarations.Exception.BlokManagerException(
                "No importer found for the key %r" % key)

        return cls.importers[key]

    @classmethod
    def remove_importer(cls, key):
        """ Remove the importer class name

        :param key: key of the importer
        :exception: BlokManagerException
        """
        if not cls.has_importer(key):
            raise anyblok.Declarations.Exception.BlokManagerException(
                "No importer found for the key %r" % key)

        del cls.importers[key]


class Blok:
    """ Super class for all the bloks

    define the default value for:

    * priority: order to load the blok
    * required: list of the bloks needed to install this blok
    * optional: list of the bloks to be installed if present in the blok list
    * conditionnal: if all the bloks of this list are installed then install
      this blok
    """

    autoinstall = False
    priority = 100
    required = []
    optional = []
    conditional = []
    name = None  # filled by the BlokManager

    def __init__(self, registry):
        self.registry = registry

    @classmethod
    def import_declaration_module(cls):
        """ Do the python import for the Declaration of the model or other
        """

    def update(self, latest_version):
        """ Call at the installation or update

        :param latest_version: latest version installed, if the blok have not
                               been installing the latest_version will be None
        """

    def uninstall(self):
        """ Call at the uninstallation
        """

    def load(self):
        """ Call at the launch of the application
        """

    def import_cfg_file(self, importer_name, model, *file_path, **kwargs):
        """ Import data file

        :param importer_name: Name of the importer (need installation of the
                              Blok which have the importer)
        :param model: Model of the data to import
        :param \*file_path: relative path of the path in this Blok
        :param \*\*kwargs: Option for the importer
        :rtype: return dict of result
        """
        blok_path = BlokManager.getPath(self.name)
        _file = join(blok_path, *file_path)
        logger.info("import %r file: %r", importer_name, _file)
        Importer = self.registry.get(BlokManager.get_importer(importer_name))
        file_to_import = None
        with open(_file, 'rb') as fp:
            file_to_import = fp.read()

        importer = Importer.insert(
            model=model, file_to_import=file_to_import, **kwargs)
        res = importer.run()
        logger.info("Create %d entries, Update %d entries",
                    len(res['created_entries']), len(res['updated_entries']))
        if res['error_found']:
            for error in res['error_found']:
                logger.error(error)

        return res
