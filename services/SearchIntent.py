synonyms = {
    "novidades" : "new_song",
    "novos" : "new_song",
    "novo" : "new_song" ,
    "lancamento" : "new_song" ,
    "lancamentos" : "new_song" ,
    "ultimos" : "new_song" ,
    "recente"  : "new_song" ,

    "top" :      "popular_song", 
    "top rits" : "popular_song",
    "popular" : "popular_song",
    "populares" : "popular_song",
    "hits" : "popular_song",
    "hit" : "popular_song",
    "melhor" :   "popular_song",
    "melhores" : "popular_song",
    "tocada" : "popular_song",
    "tocado" : "popular_song",
    "tocadas" : "popular_song",
    "tocados" : "popular_song",
    "todos" : "popular_song",
    "todas" : "popular_song",
    "todo" : "popular_song",
    "toda" : "popular_song",
    "mais ouvidas" : "popular_song",
    "topada" :   "popular_song",
    "ouvidos" :   "popular_song",
    "sucesso" :   "popular_song",
    "sucessos" :   "popular_song",

    "album" : "album",
    "discos" : "album",
    "disco" : "album",
    "faixa" : "album",
    "faixas" : "album",
    "playlist" : "album",

    # Remove partes que não agregão na pesquisa
    "ouvir" : "",
    "cancoes" : "",
    "musicas" : "",
    "as" : "",
    "os" : "",
    "a" : "",
    "o" : "",
    "do" : "",
    "da"  : "",
    "das" : "",
    "du" : "",
    "dos" : "",
    "de" : "",
    "des" : "",
    "mais"  : "",
    "mas" : "",
    "muito" : "",
    "muitos" : "",
    "muitas" : "",
    "muita" : "",
    "para" : "",


    # #Generos musicais
    # "sertanejos"
    # "sertanejo"
    # "funks"
    # "funk"
    # "pop"
    # "mpb"
    # "regaee"
    # "bossa nova",
    # "hip hop"
    # "trap"
    # "rap"
    # "gospel"
}



def _normalizeString(normalizeStr):
    normalizeStr = unidecode(normalizeStr)
    normalizeStr = normalizeStr.lower()

    return normalizeStr.split( )



def _verifySynonyms(search):


    def removeArrayDuplicates(array):
        result = []

        for item in array:
            if item not in result:
                result.append(item)

        return result
    
    priority = []
    last_word = []

    for i in range(len(search)):

        if None != synonyms.get(search[i]):
            priority.append(synonyms.get(search[i]))
        else :
            last_word.append(search[i])

    
    priority = removeArrayDuplicates(priority)

    search = " ".join(priority + last_word)
    search = search.split()

    return " ".join(search)


def createIntentSearch(search):
    search = _normalizeString(search) 
    search = _verifySynonyms(search)

    return search




