from services import CacheMusics, SearchIntent
from youtube_search import YoutubeSearch
from flask import jsonify

def youtubeSearch(searchStr, requestMusicsQuantity):
    result = YoutubeSearch(searchStr, max_results=int(requestMusicsQuantity)).to_dict()
    CacheMusics.put(cacheKey=SearchIntent.createIntentSearch(searchStr), value=result)
    return result

def searchMusic(searchStr, requestMusicsQuantity):
    try:
        if int(requestMusicsQuantity) > 30 or int(requestMusicsQuantity) <= 0:
            return "Ta achando que e bagunça e,  Ai dento!", 200
        
        if CacheMusics.exist(SearchIntent.createIntentSearch(searchStr)) != None:
            Cache = CacheMusics.get(SearchIntent.createIntentSearch(searchStr))
            if int(requestMusicsQuantity) > int(len(Cache)):
                return youtubeSearch(searchStr, requestMusicsQuantity)
            return Cache, 200
        
        result = youtubeSearch(searchStr, requestMusicsQuantity)
        return jsonify(result), 200

    except Exception as err:
        return jsonify(str(err)), 400