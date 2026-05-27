from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from flask import jsonify
from repository import UserRepository
from services import LoginVerification
from services import MailService
import bcrypt

def CreateUser(Request):
    try:
        password_hash = bcrypt.hashpw(
            Request["password"].encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        UserRepository.createUser(
            Request["name"],
            Request["datebirth"],
            Request["email"],
            password_hash
        )

        return "User created successfully", 201

    except:
        return "User not created", 404

def recoverPassword(Request):
    try:
        if MailService.verifyCode(Request["email"], Request["recoveryCode"]):
            UserRepository.updateUser(Request["email"], Request["password"])    
            return "Password recovery success", 200
        
        return "Incorrect code", 400
    except:
        return "Password not updated" , 404

def deleteUser(Response):
    try:
        UserRepository.deleteUser(Response)
        return "User deleted", 200
    except:
        return "User not deleted", 404

def login(Response):
    #Por enquando o front vai validar login usando o codigo de resposta se for 200 ele libera
    #ja tem coisa demais
    #Isso tem que ser refatorado ta uma nojenteza
    try:
        if LoginVerification.loginVerification(Response):
            token = create_access_token(identity=Response['email'])

            #Ta buscando duas vezez no banco isso ta uma nojeira
            res = UserRepository.getUser(Response["email"])

            return jsonify({
                "id": res[0],
                "name": res[1],
                "login": "True",
                "access_token": token
            }), 200

        return "login error", 403

    except:
        return "User not exist", 404
    
