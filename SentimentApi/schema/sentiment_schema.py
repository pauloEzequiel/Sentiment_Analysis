from pydantic import BaseModel,Field
from typing import Dict

class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    message: str

class SentimentAnalysisBody(BaseModel):
    text: str = Field(None, min_lenght=2, description ="Texto a ser analisado")

class SentimentAnalysisResponse(BaseModel):
    """ Resultado do texto analisado
    """
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float



   
