import unittest
from app import create_app
from app.services import facade
from app.models.user import User

class TestPutPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        # Créer un utilisateur réel pour les tests PUT
        user = User(first_name="Barack", last_name="Obama", email="barack@whitehouse.com")
        facade.user_repo.add(user)
        self.user_id = user.id

        # Créer une place initiale pour les tests de mise à jour
        self.place = facade.create_place({
            "title": "Old Title",
            "description": "Old Description",
            "price": 40.0,
            "latitude": 48.0,
            "longitude": 2.0,
            "owner_id": self.user_id
        })


    def test_update_place_success(self):
        """PUT /places/<id> avec données valides"""
        updated_data = {
            "title": "New Title",
            "description": "Updated Description",
            "price": 60.0
        }
        response = self.client.put(f'/api/v1/places/{self.place.id}', json=updated_data)
        self.assertEqual(response.status_code, 200)


    def test_update_place_partial(self):
        """PUT /places/<id> avec mise à jour partielle"""
        updated_data = {
            "title": "Partially Updated"
        }
        response = self.client.put(f'/api/v1/places/{self.place.id}', json=updated_data)
        self.assertEqual(response.status_code, 200)

    def test_update_place_invalid_title(self):
        """PUT /places/<id> avec titre invalide"""
        updated_data = {
            "title": ""
        }
        response = self.client.put(f'/api/v1/places/{self.place.id}', json=updated_data)
        self.assertEqual(response.status_code, 400)

    def test_update_place_not_found(self):
        """PUT /places/<id> pour un ID inexistant"""
        updated_data = {
            "title": "New Title"
        }
        response = self.client.put('/api/v1/places/nonexistent123', json=updated_data)
        self.assertEqual(response.status_code, 404)
