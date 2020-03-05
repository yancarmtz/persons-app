from flask_restplus import Resource
from app import ns, personDAO, api
from model.request import PersonModel

@ns.route('/')
class PersonController(Resource):

    personModel = PersonModel()

    '''Shows a list of all persons, and lets you POST to add new persons'''
    @ns.doc('list_persons')
    @ns.marshal_list_with(personModel.person)
    def get(self):
        '''List all persons'''
        print(personDAO.persons)
        return personDAO.persons

    def options(self):
        return

    @ns.doc('create_person')
    @ns.expect(personModel.person)
    @ns.marshal_with(personModel.person, code=201)
    def post(self):
        '''Create a new Person'''
        return personDAO.create(api.payload), 201

