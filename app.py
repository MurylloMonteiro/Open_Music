from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import HomeController, PlaylistsController, UserController
from services import CreateMusicLink, SearchMusic 


app = Flask(__name__)

CORS(app)
#vai ser apagado
# @app.route("/", methods=["GET"])
# def home():
#     return HomeController.Home()

@app.route("/user", methods=["POST"])
def createUser():
    return UserController.CreateUser(request.get_json())

@app.route("/user", methods=["PUT"])
def updatePassword():
    return UserController.updatePassword(request.get_json())

@app.route("/login", methods=["POST"])
def loginUser():
    return UserController.login(request.get_json())

#Vai existir o metodo de deleção de usuario, mas com uma logica mais robusta, so com o ID e brincadeira
# @app.route("/user/<int:id>", methods=["DELETE"])
# def deleteUser(id):
#     return UserController.deleteUser(id)


@app.route("/playlists/<int:id_user>", methods=["GET"])
def AllPlaylistByUser(id_user):
    return PlaylistsController.AllPlaylistByUser(id_user)





@app.route("/playlists", methods=["POST"])
def createPlaylist():
    return  PlaylistsController.createPlaylist(request.get_json())





@app.route("/search/<string:name>", methods=["GET"])
def searchVideo(name):
    musics = SearchMusic.searchMusic(str(name))
    return jsonify({"musics": musics})

@app.route("/play/<string:id>", methods=["GET"])
def playMusic(id):
    urlVideo  = CreateMusicLink.musicLink(id)
    return jsonify({"musicId": urlVideo}), 200


if __name__ == "__main__":
    app.run(debug=True)


# tratar para lives o codigo do front quebra!

