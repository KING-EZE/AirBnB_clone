#!/usr/bin/python3
"""module for testing the HBNBCommand Class"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """Test the HBNBCommand Console"""

#   def test_help(self):
#   '''test the help command'''
#   with patch('sys.stdout', new=StringIO()) as f:
#    HBNBCommand().onecmd("help")
#   string = """
# Docoumented commands (type help <topic>):
# =========================================
# EOF all count create destory help quit show update
# """
#       msg = f.getvalue()
#       self.assertEqual(string, msg)

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            s = """
Documented commands (type help <topic>):
========================================
EOF all count create destory help quit show update\n
"""
        self.assertEqual(s, f.getvalue())

    # Test cases for quit

    def test_do_quit(self):
        """Tests the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        # modellimg what happens when someone types 'quit'
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        # modelling when user types 'quit anything'
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for EOF
    def test_do_EOF(self):
        """Tests the EOF commnad"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        # modelling what happends when user types 'quit'
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        # modelling when user types 'EOF anything'
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

    # Tests cases for emptylines
    def test_do_emptyline(self):
        """Tests the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        # modelling what happens when user doesnt type anything
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                      \n")
        # modelling when user types lots of whitespaces & enter
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for do_all
    def test_do_all(self):
        """Tests the do all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

    # Test cases for do_count
    # Test cases for do_show
    # Test cases for do_create
    # Test cases for do_update
    # Test cases for do_destory


if __name__ == "__main__":
    unittest.main()
