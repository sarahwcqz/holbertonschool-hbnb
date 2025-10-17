import unittest
from app import create_app


class TestReviewEndpoints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    #creer un user originel
        user_originel = cls.client.post(f'/api/v1/users/', json={
            "first_name": "Michelle",
            "last_name": "Obama",
            "email": "TheQueen@WhiteHouse.com"
        })
        response_data_renter = user_originel.get_json()
        print("Response status:", user_originel.status_code)
        print("Response data:", response_data_renter)
        if user_originel.status_code != 201:
            raise Exception(f"Failed to create initial user. Status: {user_originel.status_code}, Response: {response_data_renter}")
        cls.renter_id = response_data_renter["id"]

    #creer une place owned par ce user
        place_originel = cls.client.post('/api/v1/places/', json={
            "title": "Beautiful suite in a classy house",
            "description": "Come enjoy the luxury yet classy place and feel the responsibilities upon the shoulders of the person on which an entire nation depends",
            "price": 1000.0,
            "latitude": 38.8977,
            "longitude": -77.0365,
            "owner_id": cls.renter_id
                    })
        response_data_place = place_originel.get_json()
        cls.place_id = response_data_place["id"]

    # creer un user qui rent la place
        reviewer_originel = cls.client.post(f'/api/v1/users/', json={
            "first_name": "Donald",
            "last_name": "Trump",
            "email": "IamAbigBaby@Disaster.com"
        })
        response_data_reviewer = reviewer_originel.get_json()
        cls.reviewer_id = response_data_reviewer["id"]

    # creer une review laissee par le user
        review_originel = cls.client.post(f'api/v1/reviews/', json={
            "text": "I'm going to make that place great again.",
            "rating": 1,
            "user_id": cls.reviewer_id,
            "place_id": cls.place_id
            })
        response_data_review = review_originel.get_json()
        cls.review_id = response_data_review["id"]
     

##################################################### PUT #########################################

    def test_update_valid(self):
        response = self.client.put(f'api/v1/reviews/{self.review_id}', json={
            "text": "Actually I'm buying that place",
            "rating": 4,
            })
        self.assertEqual(response.status_code, 200)

    def test_update_empty_review(self):
        response = self.client.put(f'api/v1/reviews/{self.review_id}', json={
            "text": "",
            "rating": 4,
            })
        self.assertEqual(response.status_code, 400)

    def test_update_invalid_rating(self):
        response = self.client.put(f'api/v1/reviews/{self.review_id}', json={
            "text": "Overratted",
            "rating": -5,
            })
        self.assertEqual(response.status_code, 400)

    def test_update_invalid(self):
        response = self.client.put(f'api/v1/reviews/12345', json={
            "text": "Actually I'm buying that place",
            "rating": 4,
            })
        self.assertEqual(response.status_code, 404)
