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

    def test_create_valid_place(self):
        """POST /places/ avec données valides"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Cozy Apartment",
            "description": "Nice and cozy",
            "price": 100.0,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": self.user_id
        })
        self.assertEqual(response.status_code, 201)


    def test_create_place_empty_title(self):
        """POST /places/ avec titre vide"""
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "Missing title",
            "price": 50.0,
            "latitude": 48.0,
            "longitude": 2.0,
            "owner_id": self.user_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_negative_price(self):
        """POST /places/ avec prix négatif"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Cheap Place",
            "description": "Negative price",
            "price": -10.0,
            "latitude": 48.0,
            "longitude": 2.0,
            "owner_id": self.user_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_latitude(self):
        """POST /places/ avec latitude invalide"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Weird Place",
            "description": "Invalid latitude",
            "price": 50.0,
            "latitude": 100.0,  # invalide
            "longitude": 2.0,
            "owner_id": self.user_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_longitude(self):
        """POST /places/ avec longitude invalide"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Weird Place",
            "description": "Invalid longitude",
            "price": 50.0,
            "latitude": 48.0,
            "longitude": 200.0,  # invalide
            "owner_id": self.user_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_user_not_found(self):
        """POST /places/ avec propriétaire inexistant"""
        response = self.client.post('/api/v1/places/', json={
            "title": "Orphan Place",
            "description": "Owner does not exist",
            "price": 50.0,
            "latitude": 48.0,
            "longitude": 2.0,
            "owner_id": "nonexistent_user"
        })
        self.assertEqual(response.status_code, 404)