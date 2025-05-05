print("Bienvenido, si quieres saber si una cancion es adecuada para \ntu playlist, ingresa los siguientes datos.")
duracion=float(input("Duración de la cancion en minutos: \n"))
gen=input("Género: \n")
gen=gen.lower()
year=int(input("Año de lanzamiento: \n"))

fy=""
fd=""
fg=""

if year<2010:
    fy="El año"

if duracion<2.5 or duracion>4.5:
    fd="La duración"

if  gen!="rock" and gen!="pop" and gen!="indie":
    fg="El genero"

if 2.5<=duracion<=4.5 and year>=2010 and (gen=="rock" or gen=="pop" or gen=="indie"):
    print("La canción es perfecta para tu Playlist! Cumple con todos los criterios.")
else:
    print("Esta canción no es adecuada para tu playlsit por los siguientes criterios:  "+ fy+" "+ fd +" "+ fg)
