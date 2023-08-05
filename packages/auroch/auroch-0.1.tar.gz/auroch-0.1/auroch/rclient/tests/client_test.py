import os
import os.path as op
import unittest
import shutil

import mock 
import mox
import jarvis.rclient.client as client
from jarvis.commands import debug, testunit_result

this_dir = op.dirname(__file__)
data_dir = op.join(this_dir, "data")
tmp_dir = op.join(this_dir, "tmp")

class IncrementalObjectStoreTest(unittest.TestCase):
    def setUp(self):
        # Refresh the temporary directory
        try:
            shutil.rmtree(tmp_dir, True)
        except:
            pass
        os.makedirs(tmp_dir)

        try:
            os.makedirs(data_dir)
        except:
            pass
        
        self.mox = mox.Mox()
        
    def data_file_name(self, filename):
        return op.join(data_dir, filename)
    
    def get_tst_file_name(self, filename):
        return op.join(tmp_dir, filename)

    def test_main(self):
        # TODO
        c = client.RClient("prefix")
        s = client.RClientString(c, "mystring")
        
        debug(s)
    
    def tearDown(self):
        self.mox.UnsetStubs()
        
        try:
            shutil.rmtree(tmp_dir, True)
        except:
            pass

        
def main():
    prefix = "test_"
    suite = unittest.TestLoader().loadTestsFromTestCase(IncrementalObjectStoreTest)
    suite = filter(lambda x : str(x).startswith(prefix), suite)
    suite = unittest.TestLoader().suiteClass(suite)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    testunit_result(result)
