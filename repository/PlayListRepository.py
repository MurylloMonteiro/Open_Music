from services.Database import NoneParamsSQL, WithParamsSQL


def createPlaylist(name, id_user):
    WithParamsSQL("CALL create_playlist(%s,%s)",(name, id_user))
    return None

def getAllPlaylistByUser(id_user):
    res = WithParamsSQL("CALL get_all_playlist_by_user(%s);", (id_user))
    return res
