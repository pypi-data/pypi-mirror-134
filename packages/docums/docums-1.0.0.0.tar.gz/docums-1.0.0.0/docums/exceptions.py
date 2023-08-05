from __future__ import unicode_literals
from click import ClickException


class DocumsException(ClickException):
    """Base exceptions for all Docums Exceptions"""


class ConfigurationError(DocumsException):
    """Error in configuration"""
