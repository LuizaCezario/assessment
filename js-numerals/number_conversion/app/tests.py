from blueprint import calculate_distance, api, validate_coordinates
from nose.tools import assert_true
import unittest
import requests

class TestCalculateRoute(unittest.TestCase):
    def test_coordinates(self):
        #Testing if the api is returning the right value
        self.assertAlmostEqual(calculate_distance('50,50'),1048.4448699320176)
    def test_out_of_boundary_coordinates(self):
        #Testing if the api returns the boundary message
        self.assertEqual(calculate_distance('500,500'),'Latitude must be in the [-90; 90] range and Longitude must be in the [-180; 180] range.')
    def test_MKAD_coordinates(self):
        #Testing if the api is returning the right value when puting mkad corrdinates
        self.assertEqual(calculate_distance('37.841217,55.739103'), 'The coordinates are inside MKAD')
    def test_right_coordinates(self):
         #Testing validation of right coordinates
        self.assertEqual(validate_coordinates('37.841217,55.739103'), True)
    def test_validate_wrong_coordinates(self):
         #Testing validation of wrong coordinates
        self.assertEqual(validate_coordinates('500,500'), False)
    def test_url_get(self):
         #Testing access to the webpage
        response = requests.get('http://127.0.0.1:5000/')
        assert_true(response.ok)