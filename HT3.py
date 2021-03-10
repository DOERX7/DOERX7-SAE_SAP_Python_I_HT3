
def aplicar_descuento(precio,descuento):
    return(precio-(precio*(descuento/100)))

def aplicar_iva(precio, iva=12):
    return(precio+(precio*iva/100))
#diccionario que es la cesta

def primer_inciso(cesta, func):
    print("-----------Ejercicio 1-----------")
    print("cesta original")
    print(cesta)
    total_original = 0
    total = 0

    for key in cesta:
        total+=func(key,cesta[key])
        total_original+=key
    print("Total original:"+str(total_original))
    print("Total con descuento:"+str(total))

#Ejercicio 2

def aplicar_cuadrado_a_lista(lista):
    lista_result = []
    for a in lista:
        lista_result.append(pow(a,2))
    return lista_result

def segundo_inciso(lista,func):
    print("-----------Ejercicio 2-----------")
    print("Lista original")
    print(lista)
    print("Lista al cuadrado")
    print(
        func(lista)
    )

#Ejecucion
dict = {
    100:20,
    200:40,
    500:10
}
primer_inciso(dict,aplicar_descuento)


lista = [1,2,3,4,5]
segundo_inciso(lista,aplicar_cuadrado_a_lista)


