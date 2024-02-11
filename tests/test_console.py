import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self): #fix this to be matched with the console.py file
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue(), "")

    


    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            self.assertIn("** instance id missing **", fake_out.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel")
            self.assertIn("** instance id missing **", fake_out.getvalue())

    

    def test_all(self): #fix this to be matched with the console.py file
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all BaseModel")
            self.assertIn("[]", fake_out.getvalue())

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(fake_out.getvalue(), "")


if __name__ == '__main__':
    unittest.main()
