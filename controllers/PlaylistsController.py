from repository import PlayListRepository
from flask import jsonify


def createPlaylist(response):
    try:
        PlayListRepository.createPlaylist(response["name"], response["id_user"])
        return "Playlist created", 201
    except:
        return "Playlist not created", 400

def AllPlaylistByUser(id_user):
    try:
        res = PlayListRepository.getAllPlaylistByUser(id_user)
        return jsonify(res)
    except:
        return "Error finding playlist", 400

