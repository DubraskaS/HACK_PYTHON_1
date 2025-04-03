"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    length = len(result)
    n=1 #Para que empiece a insertar luego del primer elemento
    while n<=length+2:
        result.insert(n,"@")
        n+=2
    return result  

#prueba interna
print(fn_hack_9())