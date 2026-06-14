# Isso e um teste para fazer cache de musica. Pretendo mudar para o REDIS. um banco chave valor utilizado principalmente para cache, mas isso e um teste
# para saber como criar um implementação de cache com o proprio python usando "hashMap" agora não vou criar uma estrutura de hashMap vou utilizar dicionario python.
# que utiliza HahsMap por tras.

#O problema dessa minha implementação e que qunado o app e desligado todo o cache e perdito, e fazendo utilização do redis posso modificar o tempo de exclução do cache.
#Segundo problema se modificar um caracter da pesquisa não busca o cache ja existente

HashTableMusic = {}

def get(search):
    print(search)
    print(HashTableMusic)
    return HashTableMusic.get(search)

    
def put(cacheKey, value):
    HashTableMusic[cacheKey] = value
    return True

def delete():
    None

def exist(Key):
    return get(Key)

