from django.test import TestCase, Client

c = Client()
response = c.get("/enseignant")
assert response.status_code == 200
