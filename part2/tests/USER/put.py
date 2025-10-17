import unittest
from app import create_app



class TestUserEndpoints(unittest.TestCase):     # creation class test (herite module test)

    @classmethod
    def setUpClass(cls):  ## exe une seule fois avant les tests indiv
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

    def setUp(self):   ## exe avant chaque test individuel
        self.app = self.__class__.app
        self.client = self.__class__.client
        self.user_id = self.__class__.user_id

################################################# PUT #############################################

    def test_update_valid(self):
        response = self.client.put(f'/api/v1/users/{self.user_id}', json={
            "first_name": "Barack",
            "last_name": "Obama",
            "email": "TheKing@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 200)

    def test_update_inexistant(self):
        response = self.client.put(f'/api/v1/users/1312', json={
            "first_name": "Barack",
            "last_name": "Obama",
            "email": "TheQueen@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 404)


    def test_update_invalide_name(self):
        response = self.client.put(f'/api/v1/users/{self.user_id}', json={
            "first_name": "",
            "last_name": "Obama",
            "email": "TheQueen@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 400)

    def test_update_long_surname(self):
        response = self.client.put(f'/api/v1/users/{self.user_id}', json={
        "first_name": "Michelle",
        "last_name": "Obamaohnoitstheposttestwithtoolongnamealloveragainpleasestopthatonsense",
        "email": "TheQueen@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 400)

    def test_update_invalid_mail(self):
        response = self.client.put(f'/api/v1/users/{self.user_id}', json={
        "first_name": "Michelle",
        "last_name": "Obama",
        "email": "WRONGMAIL"
        })
        self.assertEqual(response.status_code, 400)
