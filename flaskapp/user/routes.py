import random
from flask_restx import Resource, Namespace, fields
from flask import request
from flaskapp.models import User
from flaskapp import db

ns = Namespace("User", "User Details")

User_model = ns.model('user_model',{
    'id': fields.String,
    'name': fields.String
})

@ns.route("/")
class UserInfo(Resource):
    def __generate_password(self):
        lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
        upper_case_leeters = lower_case_letters.upper()
        special_characters = '!@#$%^&*()'

        all = lower_case_letters + upper_case_leeters + special_characters
        password_length = 9

        password = "".join(random.sample(all, password_length))
        return password

    @ns.marshal_with(User_model)
    @ns.response(400, 'Validation Error')
    def get(self):
        try:
            user_data = User.query.all()
            users = [{'id': user.id, 'name': user.name} for user in user_data]
            return users, 200
        except Exception as e:
            print("Exception Raised: {}".format(e))
            return "Exception Raise: {}".format(e), 400
    
    @ns.expect(User_model)
    @ns.response(400, 'Validation Error')
    def post(self):
        try:
            user_data = request.get_json()
            id = user_data['id']
            name = user_data['name']
            password = self.__generate_password()
            user_obj = User(id=id, name=name, password=password)
            db.session.add(user_obj)
            db.session.commit()
            return {'Message': "Registration Completed!!", 'password': password}, 201
        except Exception as e:
            print("Exception Raised: {}".format(e))
            return "Exception Raise: {}".format(e), 400

@ns.route('/<id>')
class SpecificUser(Resource):
    @ns.marshal_with(User_model)
    @ns.response(400, 'Validation Error')
    def get(self, id):
        try:
            user_info = {}
            user = User.query.get(id)
            user_info['id'] = user.id
            user_info['name'] = user.name
            return user_info, 200
        except Exception as e:
            print("Exception Raised: {}".format(e))
            return "Exception Raise: {}".format(e), 400
    
    @ns.expect(User_model)
    @ns.response(400, 'Validation Error')
    def put(self, id):
        try:
            user = User.query.get(id)
            user_data = request.get_json()
            id = user_data['id']
            name = user_data['name']
            user.name = name
            db.session.commit()
            return {'Message': "Successfully Updated!!"}, 201
        except Exception as e:
            print("Exception Raised: {}".format(e))
            return "Exception Raise: {}".format(e), 400
    
    @ns.response(400, 'Validation Error')
    def delete(self, id):
        try:
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return {'Message': "Successfully Deleted!!"}, 201
        except Exception as e:
            print("Exception Raised: {}".format(e))
            return "Exception Raise: {}".format(e), 400
