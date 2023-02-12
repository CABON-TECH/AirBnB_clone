#!/usr/bin/python3
'''
Contains all tests for the base_model class
'''
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    '''
    Tests that the BaseModel works okay
    '''
    def setUp(self):
        '''
        Set up method
        Renames the file_storage file to avoid iterfering with data
        '''
        if os.path.isfile("file.json"):
            os.rename("file.json", "backup_file.json")

        self.model_1 = BaseModel()
        self.model_2 = BaseModel()

    def tearDown(self):
        '''
        Tear down method
        Does clean up
        '''
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("backup_file.json"):
            os.rename("backup_file.json", "file.json")

        del self.model_1
        del self.model_2

    def test_attributes_types(self):
        '''
        Test that all attributes are of the correct type
        '''
        self.assertTrue(type(self.model_1), BaseModel)
        self.assertTrue(type(self.model_1.id), str)
        self.assertTrue(type(self.model_1.created_at), datetime)
        self.assertTrue(type(self.model_1.updated_at), datetime)

    def test_isinstance(self):
        '''
        Check that the created instance is an instance of the BaseModel class
        '''
        self.assertIsInstance(self.model_1, BaseModel)

    def test_init_from_dict(self):
        '''
        Test that an instance is correctly created from a dict
        '''
        a_dict = self.model_1.to_dict()
        new_model = BaseModel(**a_dict)
        self.assertEqual(self.model_1.id, new_model.id)
        self.assertEqual(self.model_1.created_at, new_model.created_at)
        self.assertEqual(self.model_1.updated_at, new_model.updated_at)

    def test_str_represntation(self):
        '''
        Test that the object's string representation is correct
        '''
        msg = "[{}] ({}) {}".format(type(self.model_1).__name__,
                                    self.model_1.id, self.model_1.__dict__)
        self.assertEqual(str(self.model_1), msg)

    def test_save_method(self):
        '''
        Test that the save method works correctly
        '''
        original_date = self.model_1.updated_at
        self.model_1.save()
        self.assertNotEqual(original_date, self.model_1.updated_at)
        key = "BaseModel." + str(self.model_1.id)
        self.assertTrue(key in FileStorage.__objects)
        try:
            with open("file.json", "r", encoding="UTF-8") as f:
                saved_file = json.load(f)

            saved_dict = saved_file[key]
            self.assertEqual(saved_dict, self.model_1.to_dict())
        except FileNotFoundError:
            pass

    def test_to_dict_method(self):
        '''
        Test that the dictionary represntation of an object is good
        '''
        a_dict = self.model_1.to_dict()
        self.assertTrue(type(a_dict), dict)
        self.assertIn("__class__", a_dict)
        self.assertIn("id", a_dict)
        self.assertIn("created_at", a_dict)
        self.assertIn("updated_at", a_dict)

    def test_unique_id(self):
        '''
        Test that created objects have unique ids
        '''
        self.assertNotEqual(self.model_1.id, self.model_2.id)

if __name__ == "__main__":
    unittest.main()
