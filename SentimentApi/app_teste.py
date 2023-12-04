from Classifier.model import get_model

model = get_model()
sentiment, confidence, probabilities = model.predict('Eu gostaria de fazer uma avaliação sincera aqui e ver se o modelo vai identificar. Mas esse é só um teste,           então nao consigo dizer se gosto ou nao gosto. Pode ser bom ou pode ser ruim :):(:')

print(sentiment)
print(confidence)
print(probabilities)