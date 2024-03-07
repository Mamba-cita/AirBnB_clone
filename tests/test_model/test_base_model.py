#!/usr/bin/python3
import unittest
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)


    def test_save(self):
        model = BaseModel()

        initial_update = model.updated_at
        model.save()
        updated_time = model.updated_at

        self.assertGreater(updated_time, initial_update)


    def test_to_dict(self):
        model = BaseModel()

        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())


    def test_str(self):
        model = BaseModel()

        string_representation = str(model)
        self.assertIsInstance(string_representation, str)
        self.assertIn('BaseModel', string_representation)
        self.assertIn(model.id, string_representation)
        self.assertIn(str(model.__dict__), string_representation)






if __name__ == '__main__':
    unittest.main()
