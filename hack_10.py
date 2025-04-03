"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    transformaciones = {
        'o': '0',
        'i': '1',
        'a': '@'
    }
    lista = [] #crea la lista a devolver
    for char in result:  #recorre todo el string
        if char in transformaciones:
            lista.append(transformaciones[char])  #Toma del diccionario el reemplazo
        else:
            lista.append(char.upper())  #Las que no se reemplazan, las pone mayusculas
            
    result = lista #iguala a result, para hacer el return
    return result  

#prueba interna
print(fn_hack_10())