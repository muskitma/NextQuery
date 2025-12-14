# test_nextquery.py
"""
Tests for NextQuery module.
"""

import unittest
from nextquery import NextQuery

class TestNextQuery(unittest.TestCase):
    """Test cases for NextQuery class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextQuery()
        self.assertIsInstance(instance, NextQuery)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextQuery()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
