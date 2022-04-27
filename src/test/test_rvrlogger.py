import unittest
import mock

import rvrbase


class Testrvrlogger(unittest.TestCase):

    # Happy flow of all the functionality in rvrlogger
    @mock.patch('requests.post')
    @mock.patch('notify_run.Notify.send')
    @mock.patch('logging.info')
    @mock.patch('logging.warning')
    @mock.patch('logging.error')
    def test_log_application_event_success2(self, mock_logging_error, mock_logging_warning,
                                            mock_logging_info, mock_notify, mock_requests_post):
        mock_requests_post.return_value = mock.Mock()
        mock_requests_post.return_value.status_code = 200

        rvrlogger = rvrbase.Rvrlogger()
        rvrlogger.log_application_event(
            type='warning', message='No worries, just testing here.', notify_message=True)

        rvrlogger.log_application_event(
            type='error', message='No worries, just testing here.', notify_message=True)

        mock_requests_post.assert_called()
        mock_notify.assert_called()
        mock_logging_info.assert_called()  # should always be called with starting message
        mock_logging_warning.assert_called()
        mock_logging_error.assert_called()


if __name__ == '__main__':
    unittest.main()
