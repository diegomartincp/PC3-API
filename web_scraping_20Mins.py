import requests
from bs4 import BeautifulSoup


print("introduzca la ciudad")
ciudad = input().replace (" ", "+").lower() # = "tres+cantos"
print("introduzca la fecha inicio año-mes-dia")
fechaIni = input().replace (" ", "-") # = "2022-03-01"
print("introduzca la fecha fin año-mes-dia")
fechaFin = input().replace (" ", "-")# = "2022-03-15"
lista_links=[]

url="https://www.20minutos.es/busqueda/?q="+ciudad+"&sort_field=publishedAt&category=&publishedAt%5Bfrom%5D="+fechaIni+"&publishedAt%5Buntil%5D="+fechaFin
r = requests.get(url)
#print(r.status_code) #200 bueno / 404 error

numero = 1
while (r.status_code == 200):
    url="https://www.20minutos.es/busqueda/"+str(numero)+"/?q="+ciudad+"&sort_field=publishedAt&category=&publishedAt%5Bfrom%5D="+fechaIni+"&publishedAt%5Buntil%5D="+fechaFin
    r = requests.get(url)

    ##Utilizamos beautfulSoup
    soup = BeautifulSoup(r.content, "html.parser")
    h1 = soup.findAll('div', {'class': 'media-content'})
    for element in h1:
        link = element.findChildren("a" , href=True)
        #Para cada uno de los links de los h2 extraemos SOLO el atributo href
        for i in link:
            link_completo=i['href'] #Extraemos atributo href
            #print( link_completo)
            lista_links.insert(0,link_completo)
    
    
    numero = numero + 1
    url="https://www.20minutos.es/busqueda/"+str(numero)+"/?q="+ciudad+"&sort_field=publishedAt&category=&publishedAt%5Bfrom%5D="+fechaIni+"&publishedAt%5Buntil%5D="+fechaFin
    r = requests.get(url)


print(len(lista_links))

noticiaCompleta = []
tituloNoticia = []
textoNoticia = []

for url in lista_links:
    r1 = requests.get(url)
    soup1 = BeautifulSoup(r1.content, "html.parser")
    
    titulo = soup1.find('h1', {'class': 'article-title'})
    parrafos = soup1.find('div', {'class': 'article-text'})
    texto = parrafos.findAll('p')
    
    contenidoTag = []
    for i in range(len(texto)):
            contenidoTag.append((texto[i].text).strip())
    tag = " ".join(contenidoTag)
    
    parrafosCont = tag.lower()
    tituloCont = titulo.text.lower()

    noticiaCompleta.insert(0,[url,tituloCont,parrafosCont])
    tituloNoticia.insert(0,tituloCont)
    textoNoticia.insert(0,parrafosCont)

print(textoNoticia)  
