while True:
	ar1=int( input("escribir el costo del       articulo:"))
    ar2=int( input("escribir el costo del       articulo:"))
    ar3=int( input("escribir el costo del articulo:"))
    ar4=int( input("escribir el costo del       articulo:"))
    ar5=int( input("escribir el costo del       articulo:"))
subtotal=ar1+ar2+ar3+ar4+ar5
iva=subtotal*0.16
total=subtotal+iva
print("el subtotal es:",subtotal)
print("el iva es:",iva)
print("el total es:",total)