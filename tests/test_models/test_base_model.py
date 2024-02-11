import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(self.base_model.to_dict(), dict)

    def test_to_dict_contains_class_name(self):
        self.assertEqual(self.base_model.to_dict()["__class__"], "BaseModel")

    def test_to_dict_contains_created_at(self):
        self.assertIn("created_at", self.base_model.to_dict())

    def test_to_dict_contains_updated_at(self):
        self.assertIn("updated_at", self.base_model.to_dict())


if __name__ == '__main__':
    unittest.main()
