#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the XFS resolver helper implementation."""

import unittest

from dfvfs.resolver_helpers import xfs_resolver_helper

from tests.resolver_helpers import test_lib


class XFSResolverHelperTest(test_lib.ResolverHelperTestCase):
  """Tests for the XFS resolver helper implementation."""

  def testNewFileObject(self):
    """Tests the NewFileObject function."""
    resolver_helper_object = xfs_resolver_helper.XFSResolverHelper()
    self._TestNewFileObject(resolver_helper_object)

  def testNewFileSystem(self):
    """Tests the NewFileSystem function."""
    resolver_helper_object = xfs_resolver_helper.XFSResolverHelper()
    self._TestNewFileSystem(resolver_helper_object)


if __name__ == '__main__':
  unittest.main()
