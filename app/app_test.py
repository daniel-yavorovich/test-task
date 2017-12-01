from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        # assert request to the app on specified path
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_api(self):
        # assert the response data on the specified path
        tester = app.test_client(self)
        response = tester.get('/hello')
        self.assertEqual(response.data, "Hello Stranger")

if __name__ == '__main__':
    unittest.main()
