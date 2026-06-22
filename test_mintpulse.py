# test_mintpulse.py
"""
Tests for MintPulse module.
"""

import unittest
from mintpulse import MintPulse

class TestMintPulse(unittest.TestCase):
    """Test cases for MintPulse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintPulse()
        self.assertIsInstance(instance, MintPulse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintPulse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
