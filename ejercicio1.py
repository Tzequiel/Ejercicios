user="richi"
contra="seantojauncompleto"

userc=input("Ingrese su nombre de usuario: ")
contrac=input("Ingrese su contraseña: ")
userc=userc.lower()

if userc==user and contrac==contra:
    print("Has iniciado sesión.")
elif user==userc and contrac!=contra:
    print("Contraseña incorrecta. La contraseña empieza con: "+ contra[1])
else:
    print("El usuario no existe.")
