import unittest
from app import create_app



class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

################################################# POST #############################################
################################################# PUT #############################################
################################################# GET #############################################
