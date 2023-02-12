#!/usr/bin/python3
"""
Defines unittests for base_model.py
"""

# Imports
import unittest	# Required to run unittests
from models.base_model import BaseModel # Import Module to be tested

# Test class for BaseModel
class TestBaseModelInstatioation(unittest.TestCase):
	"""
	Tests for BaseModel class instantiation
	A subclass of unittest.TestCase or inherits from unittest.TestCase
	"""
	# Test function
	def test_instance_id_is_unique(self):
		bm1 = BaseModel()
		bm2 = BaseModel()

		self.assertNotEqual(bm1.id, bm2.id)

	def test_instance_creation_from_dict_repsentation(self):
		bm1 = BaseModel()
		bm2 = BaseModel(**bm1.to_dict())

		self.assertEqual(bm1.id, bm2.id)
