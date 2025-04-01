"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    n=0
    while (n < 6):
        result.append(n)
        n += 1
    return result  

#Prueba interna
print(fn_hack_6())