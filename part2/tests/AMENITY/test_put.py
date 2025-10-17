import unittest
from app import create_app



class TestAmenityEndpoints(unittest.TestCase):


    @classmethod
    def setUpClass(cls):  ## exe une seule fois avant les tests indiv
        cls.app = create_app()
        cls.client = cls.app.test_client()
        amenity1_originel = cls.client.post('/api/v1/amenities/', json={
            "name": "nachos",
        })
        response_data = amenity1_originel.get_json()
        if amenity1_originel.status_code != 201:
            raise Exception(f"Failed to create amenity 1. Status: {amenity1_originel.status_code}, Response: {response_data}")
        cls.amenity1_id = response_data["id"]


    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

#################################################### PUT #######################################################

    def test_valid_id(self):
        response = self.client.get(f'/api/v1/amenities/{self.amenity1_id}', json={
            "name": "queso"
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_id(self):
        response = self.client.get(f'/api/v1/amenities/12345', json={
            "name": "queso"
        })
        self.assertEqual(response.status_code, 404)

    def test_empty_input(self):
        response = self.client.get(f'/api/v1/amenities/{self.amenity1_id}', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_too_long_input(self):
        response = self.client.get(f'/api/v1/amenities/{self.amenity1_id}', json={
            "name": "this is a very long name for an amenity again, i am running out of ideas to write down"
        })
        self.assertEqual(response.status_code, 400)