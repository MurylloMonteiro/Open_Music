from repository import PlayListRepository
from flask import jsonify


def createPlaylist(response):
    try:
        PlayListRepository.createPlaylist(response["name"], response["id_user"])
        return "Playlist created", 201
    except:
        return "Playlist not created", 400

def deletePlaylist(response):
    try:
        PlayListRepository.deletePlaylist(response["playlistId"])
        return "playlist delete", 204
    except:
        return "Playlist not deleted", 400

def allPlaylistByUser(id_user):
    try:
        res = PlayListRepository.getAllPlaylistByUser(id_user)
        return jsonify(res)
    except:
        return "Error finding playlist", 400

def allMusicsByPlaylist(id_playlist):
    try:
        res = PlayListRepository.allMusicsByPlaylist(id_playlist)
        musics = []
        for i in range(len(res)):
            musics.append({
                "music_name": res[i][0],
                "artist_name": res[i][1],
                "id_youtube": res[i][2],
                "id_playlist": res[i][3],
                "name_playlist": res[i][4],
                "id_user_create_Playlist": res[i][5]
            })
        return jsonify(musics)
    except:
        return "Error finding Musics", 400
    

def addMusicPlaylist(request):
    try:
        PlayListRepository.addMusicPlaylist(request["id_playlist"], request["id_youtube_reference"], request["name_music"], request["name_artist"])
        return (f"Music add success in playlist {request["id_playlist"]} "),200
    except:
        return "Music not created", 400