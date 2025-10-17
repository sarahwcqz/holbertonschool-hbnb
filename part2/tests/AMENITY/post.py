import unittest
from app import create_app



class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

################################################# POST #############################################
    def test_creat_valid(self):
        response = self.client.post('api/v1/amenities/', json={
            "name": "nachos"
        })
        self.assertEqual(response.status_code, 201)


    def test_empty_name(self):
        response = self.client.post('api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_name_over_50(self):
        response = self.client.post('api/v1/amenities/', json={
            "name": "this is a very long name for an amenity i can't even think of anything that would take that long to write"
        })
        self.assertEqual(response.status_code, 400)
