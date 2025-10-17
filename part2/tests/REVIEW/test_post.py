import unittest
from app import create_app


class TestReviewEndpoints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        user_originel = cls.client.post('/api/v1/users/', json={
            "first_name": "Michelle",
            "last_name": "Obama",
            "email": "TheQueen@WhiteHouse.com"
        })
        response_data = user_originel.get_json()
        print("Response status:", user_originel.status_code)
        print("Response data:", response_data)
        if user_originel.status_code != 201:
            raise Exception(f"Failed to create initial user. Status: {user_originel.status_code}, Response: {response_data}")
        cls.user_id = response_data["id"]


    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

################################################# POST #############################################

