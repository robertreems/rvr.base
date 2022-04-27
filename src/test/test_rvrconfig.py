import unittest
import rvrbase


class Testrvrconfig(unittest.TestCase):

    def test_rvrconfig_wrong_file(self):
        with self.assertRaises(FileNotFoundError):
            rvrbase.Rvrconfig('filedoesnotexist.ini')

    def test_rvrconfig_q1_success(self):
        config = rvrbase.Rvrconfig('src/test/testdata/config.ini')
        self.assertEqual(config.q1('workspace_id'), 'some_id')

    def test_rvrconfig_q1_non_existing_key(self):
        config = rvrbase.Rvrconfig('src/test/testdata/config.ini')
        self.assertEqual(config.q1('keydoesnotexist'), None)


if __name__ == '__main__':
    unittest.main()
