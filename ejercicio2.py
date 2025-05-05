descest=0.15
descfr=0.10
descpts=0.20

price=input("Ingrese el valor del articulo: ")
price=float(price)

pts=input("Cuantos pts tiene el cliente: \n")
pts=int(pts)

est=input("Es estudiante: Si/No \n")
est=est.lower()

fr=input("Cuantas compras realiza al año el cliente: \n")
fr=int(fr)

if pts>= 500:
    fprice= price-(price*descpts)
    print("El precio final es: $"+str(fprice))
elif pts<= 500 and est=="si":
    fprice= price- (price*descest)
    print("El precio final es $:"+str(fprice))
elif pts<= 500 and est=="no" and fr >= 15:
    fprice= price-(price*descfr)
    print("El precio final es: $"+str(fprice))
else:
    print("El precio final es: $"+str(price))