from Classifier.model import get_model

model = get_model()


def test_sentimento_positivo_1():
    predict = model.predict("Eu amo este produto, é incrível!")
    sentiment = predict[0]
    assert sentiment == 'positivo'

def test_sentimento_positivo_2():
    predict = model.predict('c')
    sentiment = predict[0]
    assert sentiment == 'positivo'

def test_sentimento_positivo_3():
    predict = model.predict('No início, não gostei muito deste produto, mas depois de usá-lo por um tempo, percebi que era excelente!')
    sentiment = predict[0]
    assert sentiment == 'positivo'

def test_sentimento_negativo_1():
    predict = model.predict(':(')
    sentiment = predict[0]
    assert sentiment == 'negativo'

def test_sentimento_negativo_2():
    predict = model.predict('Merda de site. ')
    sentiment = predict[0]
    assert sentiment == 'negativo'
    
def test_frase_sentimento_negativo_3():
    predict = model.predict('Estou muito decepcionado com o serviço, não recomendo.')
    sentiment = predict[0]
    assert sentiment == 'negativo'

def test_frase_sentimento_negativo_4():
    predict = model.predict('poderia ser melhor')
    sentiment = predict[0]
    assert sentiment == 'negativo'

def test_frase_sentimento_negativo_5():
    predict = model.predict('Eu estava muito satisfeita até pouco tempo, as compras que fazia nos mercados vinham certinhas, agora elas sempre vem faltando item, tenho que ficar solicitando reembolso, dão um prazo de 30 dias para retornar para o cartão')
    sentiment = predict[0]
    assert sentiment == 'negativo'

def test_frase_sentimento_neutro_6():
    predict = model.predict('O produto é bom, mas o atendimento ao cliente deixou a desejar')
    sentiment = predict[0]
    assert sentiment == 'negativo'

def test_frase_sentimento_negativo_sacasmo():
    predict = model.predict('Ótimo serviço, realmente adoro quando as coisas não funcionam, muito bug, lento, trava.')
    sentiment = predict[0]
    assert sentiment == 'negativo'

def test_frase_sentimento_neutro_1():
    predict = model.predict('Satisfatório apenas.')
    sentiment = predict[0]
    assert sentiment == 'neutro'

def test_frase_sentimento_neutro_2():
    predict = model.predict('A intenção é muito boa, mas é um dos piores aplicativos que eu já usei na vida. Até tem potencial mas quando saíram, esqueceram dentro da gaveta.')
    sentiment = predict[0]
    assert sentiment == 'neutro'

def test_frase_sentimento_neutro_3():
    predict = model.predict('App razoável')
    sentiment = predict[0]
    assert sentiment == 'neutro'

def test_frase_sentimento_neutro_4():
    predict = model.predict('Não sei ao certo o que pensar sobre isso.')
    sentiment = predict[0]
    assert sentiment == 'neutro'







