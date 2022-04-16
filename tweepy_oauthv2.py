import tweepy

#CLAVES DIEGO
#consumer_key = "9eoCAPNf9fVg2kzInNI5A8Uge"
#consumer_secret = "xwmeFMOHkMl35PSrXvMl0Bk0NhWTeSDaTKk2SP47DeQ24Th3GE"
#access_token = "1070028045938057217-zJHSSfPBahkwHrWSB7vZ5tsNbOrAbt"
#access_token_secret = "fgOGCKnMI2409tF09sgRYfvlQFFnUhPXNbg79xJ1xw93v"

#CLAVES NICO
consumer_key = "R7svH3XUt2HMAF1OaVJuIpmiI"
consumer_secret = "7aTTXIAlVkTFW0T6snH7gSwRPsOqtJ2q2MBew1Sxnh42F12Ufi"
access_token = "2957242798-Sc0zgTRK6H6V820R9e8cUDGq3VYBESPy0XObV8s"
access_token_secret = "PUkqSKm6UIkaaYmpydAVke8cZPZw0Srpw5kMOMlwr0CQx"

#Objeto con las claves de acceso
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
#pasamos las claves y accedemos a la API
api = tweepy.API(auth)

desde_fecha="202201030000"
hasta_fecha="202201040000"
query_ = "Tres Cantos"  #Búsqueda


#Realiza la búsqueda en la api
tweets = tweepy.Cursor(api.search_full_archive, #metodo para buscar todos los archivos
                   label="development", #entorno
                   query=query_,        #busqueda de ciudad
                   fromDate=desde_fecha,#fecha inicio
                   toDate=hasta_fecha,  #fecha fin
                   maxResults=100       #numero de resultados
                   )

#Iteramos entre lo recuperado
for tweet in tweets.items():
    print("ID TWEET: " + str(tweet.id))
    print(tweet.text)