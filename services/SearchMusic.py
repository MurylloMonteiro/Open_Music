from youtube_search import YoutubeSearch
from flask import jsonify

def searchMusic(searchStr, requestMusicsQuantity):
    try:
        if int(requestMusicsQuantity) > 30:
            return "Ta achando que e bagunça, é Ai dento", 200


        results = YoutubeSearch(searchStr, max_results=int(requestMusicsQuantity)).to_dict()
        return jsonify(results), 200
    
    except Exception as err:
        return jsonify(str(err)), 400