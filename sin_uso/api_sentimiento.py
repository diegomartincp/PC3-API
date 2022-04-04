from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def sentiment_scores(sentence): #Le pasas la frase
    sid_obj = SentimentIntensityAnalyzer() #Construyes analizador
    sentiment_dict = sid_obj.polarity_scores(sentence) #Aplicas el método de polaridad a la frase
    return sentiment_dict['compound']   #Devuelves solo el compound

@app.route('/api/analizar',methods = ['POST'])  #Se definde la ruta de la api y el método
@cross_origin() #SOLUCIONA EL CORS

def analizar():
    if not 'texto' in request.json:
        return make_response(jsonify({'error': 'No se encuentra un texto'}), 404) #Si no se manda texto se devuelve error
    texto = request.json['texto'] #Si hay texto recogemos el texto
    blob = TextBlob(texto)  #Objeto blob con el texto recogido
    texto_traducido = str(blob.translate(to='en'))  #Se traduce el texto a 'en' inglés
    resultado = sentiment_scores(texto_traducido)   #En resultado recogemos el compound del texto traducido
    return jsonify({'resultado': resultado})    #Se devuelve el json con el compound

if __name__=='__main__':
    app.run(debug = True)