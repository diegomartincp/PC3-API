from unittest import result
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

def sentiment_scores(sentence): #Le pasas la frase
    sid_obj = SentimentIntensityAnalyzer() #Construyes analizador
    sentiment_dict = sid_obj.polarity_scores(sentence) #Aplicas el método de polaridad a la frase
    return sentiment_dict['compound']   #Devuelves solo el compound
    
texto = "Hola no me gusta nada esto"
blob = TextBlob(texto)  #Objeto blob con el texto recogido
texto_traducido = str(blob.translate(to='en'))  #Se traduce el texto a 'en' inglés
resultado = sentiment_scores(texto_traducido)   #En resultado recogemos el compound del texto traducido
print(resultado)
