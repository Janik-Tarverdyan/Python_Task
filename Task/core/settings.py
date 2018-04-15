# task/core/settings.py

import os
import binascii


class Base(object):
    """Base configuration."""
    SECRET_KEY = binascii.hexlify(os.urandom(24))
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APPLICATION_NAME = 'Task'
    APPLICATION_ROOT = os.path.dirname(os.path.abspath(__name__))
    APPLICATION_STATIC = os.path.join(
        APPLICATION_ROOT, '%s/static' % (APPLICATION_NAME))
    APPLICATION_TEMPLATE = os.path.join(
        APPLICATION_ROOT, '%s/templates' % (APPLICATION_NAME))


class Development(Base):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'
    DEBUG_TB_ENABLED = True


class Testing(Base):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    DEBUG_TB_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class Production(Base):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    DEBUG_TB_ENABLED = False
