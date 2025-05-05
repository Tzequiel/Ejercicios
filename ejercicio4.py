print("Bienvenido al conversor, ¿Que conversión desea realizar?\nIngrese el numero correspondiente\n1.-Kilometros a Millas.\n2.-Millas a Kilometros.\n3.-Celsius a Fahrenheit.\n4.-Fahrenheit a Celsius.")
op=int(input())

if op==1:
    con=float(input("Ingrese el número en kilometros: "))
    if con<0:
        print("Digito invalido. La distancia no puede ser negativa")
    else:
        val= con*0.621371
        print(f"Equivale a {val} millas")


elif op==2:
    con=float(input("Ingrese el número en millas: "))
    if con<0:
        print("Digito invalido. La distancia no puede ser negativa")
    else:
        val=con/0.621371
        print(f"Equivale a {val} millas")


elif op==3:
    con=float(input("Ingrese el número en celsius: "))
    val= con*9/5 + 32
    print(f"{con}°C equivalen a {val}°F.")
    if con < 0:
        print("Está bajo cero.")
    elif 15 <= con <= 25:
        print("Está a temperatura ambiente.")
    else:
        print("Hace calor.")


elif op==4:
    con=float(input("Ingrese el número en fahrenheit: "))
    val= (con-32)*5/9
    print(f"{con}°C equivalen a {val}°F.")
    if val < 0:
        print("Está bajo cero.")
    elif 15 <= val <= 25:
        print("Está a temperatura ambiente.")
    else:
        print("Hace calor.")

else:
    print("Digito invalido, se cierra el programa.")