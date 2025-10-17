import unittest
from app import create_app


class TestUserEndpoints(unittest.TestCase):     # creation class test (herite module test)

    def setUp(self):    ### init l'env de test 
        self.app = create_app()     # appli flask
        self.client = self.app.test_client()    # simule un navigateur pou client HTTP (permet les requetes sans lancer reellement le serveur)
        

################################################# POST #############################################

    def test_create_valid(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Barack",
            "last_name": "Obama",
            "email": "TheKing@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 201) # format: (resultat obtenu, resultat attendu)


    def test_empty_name(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "Obama",
            "email": "TheQueen@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 400)

    
    def test_empty_surname(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Michelle",
            "last_name": "",
            "email": "TheQueen@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 400)


    def test_invalid_mail_format(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Michelle",
            "last_name": "Obama",
            "email": "INVALIDE_MAIL"
        })
        self.assertEqual(response.status_code, 400)


    def test_long_name(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Michellebutmynameissolongitisbarelypossibletoreaditihadsomuchpainlearningitwheniwasakid",
            "last_name": "Obama",
            "email": "TheQueen@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 400)


    def test_long_surname(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Michelle",
            "last_name": "Obamabutitisthesameproblemewithmysurnameidontknowwhodoesthisbutishastostoptobehonnesticanttakeitanymore",
            "email": "TheQueen@WhiteHouse.com"
        })
        self.assertEqual(response.status_code, 400)

