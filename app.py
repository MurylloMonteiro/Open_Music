from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from controllers import PlaylistsController, UserController
from services import CreateMusicLink, SearchMusic , MailService
from flask_mail import Mail
from FlaskConfiguration import Configuration



app = Configuration(Flask(__name__))

#modificar o CORS esta liberado para qualquer requisição
CORS(app)


jwt = JWTManager(app)
mail = Mail(app)

@app.route("/user", methods=["POST"])
def createUser():
    return UserController.CreateUser(request.get_json())

@app.route("/auth/login", methods=["POST"])
def loginUser():
    return UserController.login(request.get_json())

@app.route("/auth/forgot", methods=["POST"])
def forgotPassword():
    MailService.sendMail(mail ,request.get_json())
    return "email send"

@app.route("/auth/recover", methods=["PUT"])
def recoverPassword():    
    return UserController.recoverPassword(request.get_json())

#Vai existir o metodo de deleção de usuario, mas com uma logica mais robusta, so com o ID e brincadeira
# @app.route("/user/<int:id>", methods=["DELETE"])
# def deleteUser(id):
#     return UserController.deleteUser(id)

@app.route("/playlists/<int:id_user>", methods=["GET"])
# @jwt_required()
def allPlaylistByUser(id_user):
    return PlaylistsController.allPlaylistByUser(id_user)

@app.route("/playlists/musics/<int:id_playlist>", methods=["GET"])
# @jwt_required()
def allMusicsByPlaylist(id_playlist):
    return PlaylistsController.allMusicsByPlaylist(id_playlist)

@app.route("/playlists/musics", methods=["POST"])
# @jwt_required()
def addMusicPlaylist():
    return PlaylistsController.addMusicPlaylist(request.get_json())

@app.route("/playlists", methods=["POST"])
# @jwt_required()
def createPlaylist():
    return  PlaylistsController.createPlaylist(request.get_json())

@app.route("/playlists", methods=["DELETE"])
# @jwt_required()
def deletePlaylist():
    return PlaylistsController.deletePlaylist(request.get_json())


@app.route("/search/<string:name>", methods=["GET"])
# @jwt_required()
def searchVideo(name):
    musics = SearchMusic.searchMusic(str(name))
    return jsonify({"musics": musics})

@app.route("/play/<string:id>", methods=["GET"])
# @jwt_required()
def playMusic(id):
    urlVideo  = CreateMusicLink.musicLink(id)
    return jsonify({"musicId": urlVideo}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



