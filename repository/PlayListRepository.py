from services.Database import NoneParamsSQL, WithParamsSQL


def createPlaylist(name, id_user):
    WithParamsSQL("CALL create_playlist(%s,%s);",(name, id_user))
    return None

def deletePlaylist(playlistId):
    WithParamsSQL("CALL delete_playlist(%s);", (playlistId))
    return None

def getAllPlaylistByUser(id_user):
    res = WithParamsSQL("CALL get_all_playlist_by_user(%s);", (id_user))
    return res

def allMusicsByPlaylist(id_playlist):
    res = WithParamsSQL("CALL get_all_musics_by_playlist(%s);", (id_playlist))
    return res

def addMusicPlaylist(id_playlist, id_youtube_reference, name_music, name_artist):
    WithParamsSQL("CALL  add_music_in_playlist(%s,%s,%s,%s);", (id_playlist, id_youtube_reference, name_music, name_artist))
    return None
