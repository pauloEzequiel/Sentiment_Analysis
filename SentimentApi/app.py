from flask_restful import Api
from flask_cors import CORS
from flask import redirect,jsonify, json
from flask_openapi3 import Info,Tag
from flask_openapi3 import OpenAPI
from schema.sentiment_schema import ErrorSchema, SentimentAnalysisBody,SentimentAnalysisResponse
import jsonpickle


from Classifier.model import get_model

info = Info(title="Analisador de Sentimentos", version="1.0.0")
sentiment = Tag(name="Analisador de Sentimentos", description="Informe o texto que será classificado em positivo, negativo ou neutro")

app = OpenAPI(__name__, info=info)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_RESOURCES'] = {r"/sentiment/*": {"origins": "*"}}

@app.get('/',doc_ui=False)
def home():
    return redirect('/openapi')

@app.post('/sentiment',tags = [sentiment],responses={"200":SentimentAnalysisResponse,"400":ErrorSchema,"404":ErrorSchema})
def analysis_text(body:SentimentAnalysisBody):
    """
       Endpoint destinado a analise do texto informado

    """
    try:
        model = get_model()
        sentiment, confidence, probabilities = model.predict(body.text)

        result_analysis = SentimentAnalysisResponse(sentiment=sentiment, confidence= confidence, probabilities= probabilities)

        probabilities= {
            'positive': result_analysis.probabilities['positivo'],
            'neutral' : result_analysis.probabilities['neutro'],
            'negative': result_analysis.probabilities['negativo']
        }

        return jsonify(sentiment=result_analysis.sentiment, confidence= result_analysis.confidence, probabilities = probabilities )
    except:
        return {"message": "Falha ao analisar texto"}, 400


