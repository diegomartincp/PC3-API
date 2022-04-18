import requests
from bs4 import BeautifulSoup

#Indicamos la ciudad, reemplazamos espacion por - y convertimos a minuscula
print("introduzca la ciudad")
ciudad = input().replace (" ", "-").lower()

#En la web se puede hacer varias operaciones:
operacion= ["comprar", "alquiler", "compartir"]
#En que estamos interasados:
lugar = ["viviendas", "locales", "oficinas"]
#Almacenara el resultado final con el numero de viviendas de cada tipo
total = []

#Para cada operacion y para cada tipo
import pandas as pd  
df = pd.DataFrame(columns = ['Operacion', 'Lugar', 'Total'])
print(len(operacion))

for oper in operacion:
    for lug in lugar:
        #Accedemos a la url
        url = "https://www.fotocasa.es/es/"+oper+"/"+lug+"/"+ciudad+"/todas-las-zonas/l"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        #buscamos las etiquetas que contienen el numero y la informacion
        numero = soup.find('span', {'class': 're-SearchTitle-count'})
        texto = soup.find('h1', {'class': 're-SearchTitle-text'})
        #unimos ambas etiquetas y las insertamos en el array final
        info = numero.text + " " + texto.text
        total.insert(0, info)
        #rellenamos el dataframe
        new_row = {'Operacion':oper, 'Lugar':lug, 'Total':info}
        df=df.append(new_row, ignore_index=True)

#mostramos el resultado
#print(total)

# Print the output.  
print(df)  

#Exportar a .csv
df.to_csv("fotocasa.csv", encoding="utf-8") 


#print(totalExtra)

############################################## EXTRA
#print("Tipo de operacion. 1 Compra // 2 Alquiler // 3 Compartir")
#numOper= input()
#print("Tipo de lugar. 1 Vivienda // 2 Locales // 3 Oficinas")
#numLug= input()

#totalExtra = []
#Accedemos a la url
#url = "https://www.fotocasa.es/es/"+str(operacion[int(numOper)-1])+"/"+str(lugar[int(numLug)-1])+"/"+ciudad+"/todas-las-zonas/l"
#r = requests.get(url)
#soup = BeautifulSoup(r.content, "html.parser")
#buscamos las etiquetas que contienen el numero y la informacion
#numero = soup.find('span', {'class': 're-SearchTitle-count'})
#texto = soup.find('h1', {'class': 're-SearchTitle-text'})
#unimos ambas etiquetas y las insertamos en el array final
#info = numero.text + " " + texto.text
#totalExtra.insert(0, info)
#print(totalExtra)