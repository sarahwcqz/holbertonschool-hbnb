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

############################################## GET #####################################################

    def test_valid(self):
        response = self.client.get(f'/api/v1/amenities/{self.amenity1_id}')
        self.assertEqual(response.status_code, 200)


    def test_inexistant(self):
        response = self.client.get(f'/api/v1/amenities/1234')
        self.assertEqual(response.status_code, 404)
