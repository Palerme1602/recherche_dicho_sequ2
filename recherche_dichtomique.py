tableau=[7,9,12,15,17,78]
element_n=int(input("entrer la valeur recherchee:"))
deb=0
fin=len(tableau)-1
trouve=False
while deb <= fin and not trouve:
    milieu= (deb + fin) // 2
    if tableau[milieu] == element_n:
        trouve= True
    else:
        if tableau[milieu] < element_n:
            deb = milieu + 1
        else:
            fin = milieu - 1
if trouve:
    print("la valeur est presente dans le tableau a la position:",milieu)
else:
    print("la valeur",element_n,"n'existe pas.")
