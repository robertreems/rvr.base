import unittest
import mock

from rvrbase.api import Azure_reader_api


class Testrvrconfig(unittest.TestCase):

    @mock.patch('requests.post')
    def test_initialize_happy(self, mock_requests_post):
        mock_requests_post.return_value = mock.Mock()
        mock_requests_post.return_value.status_code = 200
        mock_requests_post.return_value.content = b'{"access_token":"bsaccessToken"}'

        tenant = '13ebf573-f6a0-4a5a-a14e-578ba97ec355'
        sp_id = '274cef59-fa12-4b39-92f7-5175bc279424'
        sp_secret = '3p78Q~pLBhy.dsafjowieup_xoafasfwea89.'
        Azure_reader_api(tenant, sp_id, sp_secret)

        mock_requests_post.assert_called()


if __name__ == '__main__':
    unittest.main()
