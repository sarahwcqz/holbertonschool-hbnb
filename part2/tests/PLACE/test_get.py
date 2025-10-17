import unittest
from app import create_app
from app.services import facade
from app.models.user import User

class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        # Créer un utilisateur fictif pour être propriétaire des places
        user = User(first_name="Barack", last_name="Obama", email="barack@whitehouse.com")
        facade.user_repo.add(user)
        self.user_id = user.id

    def test_get_all_places(self):
        # Créer une place pour tester
        facade.create_place({
            "title": "Test Get Place",
            "description": "Testing GET all",
            "price": 70.0,
            "latitude": 48.0,
            "longitude": 2.0,
            "owner_id": self.user_id,
        })
        response = self.client.get('api/v1/places/')
        self.assertEqual(response.status_code, 200)

    def test_get_place_by_id(self):
        place = facade.create_place({
            "title": "Specific Place",
            "description": "For GET by ID",
            "price": 80.0,
            "latitude": 48.0,
            "longitude": 2.0,
            "owner_id": self.user_id,
        })
        response = self.client.get(f'api/v1/places/{place.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_place_not_found(self):
        response = self.client.get('api/v1/places/nonexistent123')
        self.assertEqual(response.status_code, 404)
