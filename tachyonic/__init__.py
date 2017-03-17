# -*- coding: utf-8 -*-
"""Tachyonic"""

from tachyonic import metadata


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright

__import__('pkg_resources').declare_namespace(__name__)
