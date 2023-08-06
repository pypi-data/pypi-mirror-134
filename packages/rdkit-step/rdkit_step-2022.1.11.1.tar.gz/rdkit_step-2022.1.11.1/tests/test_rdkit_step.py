#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rdkit_step` package."""

import pytest  # noqa: F401
import rdkit_step  # noqa: F401


def test_construction():
    """Just create an object and test its type."""
    result = rdkit_step.Rdkit()
    assert str(type(result)) == "<class 'rdkit_step.rdkit.Rdkit'>"
