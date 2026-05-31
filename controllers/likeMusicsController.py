from flask import jsonify

from repository import LikeMusicsRepository



#Correto e fazer todas as perquisas altomaticamente e retornar ja capa e link do youtube tudo em um array
#Se no front ele tiver mais de 20 musicas no likeMusics e tiverem 10 usuarios abrindo simultaneo ja são 200 requisiçõe ne meu patrão 
def getAllLikeMusicsByUser(id_user):
    try:
        res = LikeMusicsRepository.getAllLikeMusicsByUser(id_user)
        return jsonify(res), 200
    except:
        return "User not exist", 400

def createLikeMusic(response):
    try: 
        LikeMusicsRepository.createLikeMusic(response["idUser"], response["id_yt_music"])
        return "LikeMusic created", 201
    except:
        return "LikeMusic not created", 400

def deleteLikeMusic(response):
    try:
        LikeMusicsRepository.deleteLikeMusics(response["idUser"], response["id_yt_music"])
        return "LikeMusic by user deleted", 204
    except:
        return "LikeMusic not deleted", 400