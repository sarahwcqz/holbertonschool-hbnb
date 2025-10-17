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


