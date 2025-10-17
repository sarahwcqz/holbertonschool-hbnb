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

        amenity2_originel = cls.client.post('/api/v1/amenities/', json={
            "name": "queso",
        })
        response_data2 = amenity2_originel.get_json()
        cls.amenity2_id = response_data2


    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

############################################## GET #####################################################

################### get one amenity by id ###############

    def test_valid_id(self):
        response = self.client.get(f'/api/v1/amenities/{self.amenity1_id}')
        self.assertEqual(response.status_code, 200)


    def test_invalid_id(self):
        response = self.client.get(f'/api/v1/amenities/1234')
        self.assertEqual(response.status_code, 404)


################### get list of all amenities ###############

    def test_valid_endpoint(self):
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
