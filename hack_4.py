"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    #Separando elstr en "rebanadas" para manipular solo la parte que queremos
    result = result[:-1] + result[-1].upper()
    return result

#Prueba interna
print(fn_hack_4())