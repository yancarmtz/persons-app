
from flask_restplus import fields
from app import api

class PersonModel(object):
    def __init__(self):
        self.person = api.model('Person', {
            'email': fields.String(required=True,description='The person\'s email, a unique identifier.'),
            'name': fields.String(required=True, description='The person\'s name.')
        })

