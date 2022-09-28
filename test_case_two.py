import unittest
import application as tested_app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.application.config['TESTING'] = True
        self.app = tested_app.application.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello World!')

    def test_post_hello_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)


if __name__ == '__main__':
    unittest.main()

