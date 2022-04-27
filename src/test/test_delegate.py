import unittest
import mock

import rvrbase


class Testrvrconfig(unittest.TestCase):

    def test_rvrconfig_wrong_file(self):
        with self.assertRaises(FileNotFoundError):
            rvrbase.Mydelegate('filedoesnotexist.ini')

    @mock.patch('requests.post')
    def test_rvrconfig_q1_success(self, mock_requests_post):
        mock_requests_post.return_value = mock.Mock()
        mock_requests_post.return_value.status_code = 200

        config = rvrbase.Mydelegate('src/test/testdata/config.ini')
        self.assertEqual(config.q1('workspace_id'),
                         '7756814b-7720-4b6d-9fb6-0aa03fe97658')

    @mock.patch('requests.post')
    def test_rvrconfig_q1_non_existing_key(self, mock_requests_post):
        mock_requests_post.return_value = mock.Mock()
        mock_requests_post.return_value.status_code = 200

        config = rvrbase.Mydelegate('src/test/testdata/config.ini')
        self.assertEqual(config.q1('doesnotexist'), None)

    # Happy flow of all the functionality in delegate.
    @mock.patch('requests.post')
    @mock.patch('notify_run.Notify.send')
    @mock.patch('logging.info')
    @mock.patch('logging.warning')
    @mock.patch('logging.error')
    def test_log_application_event_success2(self, mock_logging_error, mock_logging_warning,
                                            mock_logging_info, mock_notify, mock_requests_post):
        mock_requests_post.return_value = mock.Mock()
        mock_requests_post.return_value.status_code = 200

        rvrlogger = rvrbase.Mydelegate('src/test/testdata/config.ini')
        rvrlogger.log_app_event(
            type='warning', message='No worries, just testing here.', notify_message=True)

        rvrlogger.log_app_event(
            type='error', message='No worries, just testing here.', notify_message=True)

        mock_requests_post.assert_called()
        mock_notify.assert_called()
        mock_logging_info.assert_called()  # should always be called with starting message
        mock_logging_warning.assert_called()
        mock_logging_error.assert_called()


if __name__ == '__main__':
    unittest.main()
