import codeServer
import unittest
import os

"""
Test if codeServer flask endpoint routing runs properly.
"""


class CodeServerTestCase(unittest.TestCase):

    def setUp(self):
        codeServer.app.testing = True
        self.app = codeServer.app.test_client()

    """
    Calling GET method
    implemented by: jabhuiyan
    """
    def test_get(self):
        rv = self.app.get('/')
        # assert if GET request body is returned
        assert b'<textarea name="codestuff" id="coding" rows="25" cols="80">ENTER CODE HERE</textarea>' in rv.data

        
    """
    Checks if the numpy solutions page is returned
    implemented by: jabhuiyan
    """
    def test_numpySolPage(self):
        rv = self.app.get('/numpy_prac')
        # assert if the GET request returns the numpy solution page
        assert b'<h1>Numpy Practice Code Solutions</h1>' in rv.data
    
    """
    implemented by: Carson
    attributions: Jubaer, prof Brown's moleflask example
    """
    def test_template(self):
        rv = self.app.post('/run_code', data=dict(userfound="username", codestuff="print('hi whats up')"), follow_redirects=True)
        assert b'hi whats up' in rv.data

    """
    Calls the check_code function which should create a file if it does not exist based on the given param.  
    
    Implemented by: Aneesh
    """
    def test_shouldsavefile(self):
        username = "testusername"
        codeServer.check_code(username)
        self.assertEqual(True, os.path.exists(f"{username}.txt"))
        os.remove(f"{username}.txt")
    """
    If a username does exist then the check_call function should open, read and return its contents
    
    Implemented by: Aneesh
    """
    def test_revert(self):
        setup_username = "testusername.txt"
        f = open(setup_username, "w")
        f.write("hello world!!")
        f.close()

        username = "testusername"
        result = codeServer.check_code(username)
        self.assertEqual("hello world!!", result)
        os.remove(f"{username}.txt")


if __name__ == '__main__':
    unittest.main()
