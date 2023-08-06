# -*- coding: utf-8 -*-

"""
rdkit_step
A SEAMM plug-in for RDKit
"""

# Bring up the classes so that they appear to be directly in
# the rdkit_step package.

from rdkit_step.rdkit import Rdkit  # noqa: F401, E501
from rdkit_step.rdkit_parameters import RdkitParameters  # noqa: F401, E501
from rdkit_step.rdkit_step import RdkitStep  # noqa: F401, E501
from rdkit_step.tk_rdkit import TkRdkit  # noqa: F401, E501

# The metadata
from rdkit_step.metadata import properties  # noqa: F401

# Handle versioneer
from ._version import get_versions

__author__ = "Mohammad Mostafanejad"
__email__ = "sina.mostafanejad@gmail.com"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
