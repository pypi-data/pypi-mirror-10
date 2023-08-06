"""
storlever.web.webconfig
~~~~~~~~~~~~~~~~

This module implements index web page of storlever

:copyright: (c) 2014 by OpenSight (www.opensight.cn).
:license: AGPLv3, see LICENSE for more details.

"""

import os
import errno
import hashlib
from storlever.mngr.system.cfgmgr import STORLEVER_CONF_DIR
from storlever.lib.config import Config, yaml, ConfigError
from storlever.lib.schema import Schema, Use


class WebConfig(Config):
    """
    default password is 123456,
    fc91f9f874d2ef4d48fdde151271716f268977c1f77241d5321b61fda137ac3c is sha256 hash of result of PBKDF2 to 123456
    """
    CONF_FILE = os.path.join(STORLEVER_CONF_DIR, 'web.yaml')
    DEFAULT_CONF = {'password': 'e4fa4c9565a834048be7f233ed6c618e03143b69e3c4aa6de4f98851f79bb889',
                    'language': 'chinese'}
    SCHEMA = Schema({
        'password': Use(str),     # filesystem type
        'language': Use(str),     # dev file
    })

    def __init__(self, conf=None):
        self.conf_file = self.CONF_FILE
        self.conf = conf
        self.schema = self.SCHEMA

    def parse(self):
        if self.conf_file is not None and self.conf_file != "":
            try:
                with open(self.conf_file, "r") as f:
                    self.conf = yaml.load(f)
                if self.schema:
                    self.conf = self.schema.validate(self.conf)
                return self.conf
            except IOError as e:
                if e.errno == errno.ENOENT:
                    self.conf = self.DEFAULT_CONF
                    self.write()
                    return self.conf
                else:
                    raise ConfigError(str(e))
            except Exception:
                raise ConfigError(str(Exception))
        else:
            raise ConfigError("conf file absent")

    @classmethod
    def from_file(cls):
        conf = cls()
        conf.parse()
        return conf

    @classmethod
    def to_file(cls, conf):
        conf = cls(conf=conf)
        conf.write()
        return conf


class WebPassword(object):
    PBKDF2_SALT = 'OpenSight2013'
    def __init__(self):
        self._web_conf = WebConfig.from_file()
        self._saved_password = self._web_conf.conf['password']

    def check_password(self, login, password):
        if login == 'admin' and self._saved_password == hashlib.sha256(password).hexdigest():
            return True
        return False

    def change_password(self, login, old_password, new_password):
        if self.check_password(login, old_password):
            self._web_conf.conf['password'] = hashlib.sha256(new_password).hexdigest()
            self._web_conf.write()
            return True
        return False

