from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def sentiment_scores(sentence): 
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
    return sentiment_dict['compound']

@app.route('/api/analizar',methods = ['POST'])
@cross_origin()
def create_actividad():
    if not 'texto' in request.json:
        return make_response(jsonify({'error': 'No se encuentra un texto'}), 404) #esta es la mejor manera de manejar errores
    texto = request.json['texto']
    blob = TextBlob(texto)
    texto_traducido = str(blob.translate(to='en'))
    resultado = sentiment_scores(texto_traducido)
    return jsonify({'resultado': resultado})

if __name__=='__main__':
    app.run(debug = True)