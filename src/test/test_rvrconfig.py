import unittest
import rvrbase

# Test query configfile


class TestRun(unittest.TestCase):

    def test_rvrconfig_q1(self):
        config = rvrbase.Rvrconfig('src/test/testdata/config.ini')
        self.assertEqual(config.q1('workspace_id'), 'some_id')


if __name__ == '__main__':
    unittest.main()
