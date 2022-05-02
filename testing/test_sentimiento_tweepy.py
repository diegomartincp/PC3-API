#Tratamiento de sentimiento
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from googletrans import Translator

textos = ["Hola no me gusta nada lo que haces","Hola me encanta lo que haces", "Juegos de ordenador", "Estudiar informática"]

translator=Translator()
sid_obj = SentimentIntensityAnalyzer() #Construyes analizador

for texto in textos:
    traduccion=translator.translate(texto)
    print(traduccion.text)
    sentiment_dict = sid_obj.polarity_scores(traduccion.text) #Aplicas el método de polaridad a la frase
    resultado=sentiment_dict['compound']
    print(resultado)   #Devuelves solo el compound