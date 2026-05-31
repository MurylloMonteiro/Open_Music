from services.Database import NoneParamsSQL, WithParamsSQL

def getAllLikeMusicsByUser(id_user):
    res = WithParamsSQL("CALL get_all_likeMusics_by_users(%s);", (id_user))
    return res

def createLikeMusic(id_user, id_yt_music):
    WithParamsSQL("CALL add_like_musics(%s, %s);", (id_user, id_yt_music))
    return None

def deleteLikeMusics(id_user, id_yt_music):
    WithParamsSQL("CALL delete_like_musics(%s, %s);", (id_user, id_yt_music))
    return None