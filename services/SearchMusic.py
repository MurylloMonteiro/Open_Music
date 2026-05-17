from youtube_search import YoutubeSearch

def searchMusic(searchStr):

    ListMusic = []
    
    results = YoutubeSearch(searchStr, max_results=20).to_dict()

    for i in range(len(results)):
        
        ListMusic.append({
            "id": results[i]["id"],
            "thumbnails": results[i]["thumbnails"],
            "channel": results[i]["channel"],
            "views": results[i]["views"],
            "name": results[i]["title"],
            "duration": results[i]["duration"],
            "publish_time": results[i]["publish_time"]
        })
        
    return ListMusic
