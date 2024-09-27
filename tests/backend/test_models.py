import unittest
from django.test import TestCase
from backend.models import YourModel

class YourModelTestCase(TestCase):
    def setUp(self):
        # Setup initial data for the tests
        YourModel.objects.create(name="Test Name", value=123)

    def test_model_creation(self):
        """Test that a model instance can be created successfully"""
        instance = YourModel.objects.get(name="Test Name")
        self.assertEqual(instance.value, 123)

    def test_model_str(self):
        """Test the string representation of the model"""
        instance = YourModel.objects.get(name="Test Name")
        self.assertEqual(str(instance), "Test Name")

if __name__ == '__main__':
    unittest.main()