import sys
import os

if sys.version_info >= (2, 7):
    import unittest
else:
    import unittest2 as unittest

from storlever.mngr.fs.fsmgr import fs_mgr
from storlever.mngr.fs import xfs
from utils import get_block_dev


class TestMkfs(unittest.TestCase):

    def test_mkfs_no_option(self):
        mgr = fs_mgr()
        dev_file = get_block_dev()
        if dev_file == "":
            return
        mgr.mkfs_on_dev("xfs", dev_file)


class TestFsMgr(unittest.TestCase):

    def test_type_list(self):
        mgr = fs_mgr()
        self.assertTrue("xfs" in mgr.fs_type_list())

    def test_add_fs(self):
        mgr = fs_mgr()
        dev_file = get_block_dev()
        if dev_file == "":
            return
        mgr.mkfs_on_dev("xfs", dev_file)
        mgr.add_fs("test_xfs", "xfs", dev_file, comment="test")
        for fs in mgr.get_fs_list():
            if fs.name == "test_xfs":
                break;
        else:
            raise Exception("there is no file system name test_xfs")

        f = mgr.get_fs_by_name("test_xfs")
        self.assertEquals(f.fs_conf["dev_file"], dev_file)
        self.assertEquals(f.fs_conf["comment"], "test")
        self.assertTrue(f.is_available())
        self.assertTrue(f.usage_info()["total"] > 0)
        self.assertTrue(len(f.fs_meta_dump()) != 0)
        f.grow_size()
        with open("/etc/fstab", "r") as fstab:
            self.assertTrue("/mnt/test_xfs" in fstab.read())
        mgr.del_fs("test_xfs")








