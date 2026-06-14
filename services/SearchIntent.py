from unidecode import unidecode

# Search Intent simplesmente padroniza a busca exemplo {Melhores musicas do manoel gomes official} depois do search intent {musicas populares manoel gomes} 
# Fazendo isso ele aumenta a chance de aproveitamento de cache.


synonyms = {
    "novidades" : "novas musicas",
    "novos" : "novas musicas",
    "novo" : "novas musicas" ,
    "lancamento" : "novas musicas" ,
    "lancamentos" : "novas musicas" ,
    "ultimos" : "novas musicas" ,
    "recente"  : "novas musicas" ,

    "top" :      "musicas populares", 
    "top rits" : "musicas populares",
    "popular" : "musicas populares",
    "populares" : "musicas populares",
    "hits" : "musicas populares",
    "hit" : "musicas populares",
    "melhor" :   "musicas populares",
    "melhores" : "musicas populares",
    "tocada" : "musicas populares",
    "tocado" : "musicas populares",
    "tocadas" : "musicas populares",
    "tocados" : "musicas populares",
    "todos" : "musicas populares",
    "todas" : "musicas populares",
    "todo" : "musicas populares",
    "toda" : "musicas populares",
    "mais ouvidas" : "musicas populares",
    "topada" :   "musicas populares",
    "ouvidos" :   "musicas populares",
    "sucesso" :   "musicas populares",
    "sucessos" :   "musicas populares",

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
    "official" : "",


    #Generos musicais
    "sertanejos" : "sertanejo",
    "sertanejo" : "sertanejo",
    "funks" : "funk",
    "funk" : "funk",
    "pops" : "pop",
    "pop" : "pop",
    "mpbs"  : "mpb",
    "mpb"  : "mpb",
    "regaees" : "regaee",
    "regaee" : "regaee",
    "hip hops" : "hip hop",
    "hip hop" : "hip hop",
    "traps" : "trap",
    "trap" : "trap", 
    "raps" : "rap",
    "rap" : "rap",
    "gospel" : "gospels",
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




