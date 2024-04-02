#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.city1 = City(state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa",
                          name="San_Francisco")

    def test_state_id(self):
        """ """
        self.assertEqual(type(self.city1.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.city1.name), str)
