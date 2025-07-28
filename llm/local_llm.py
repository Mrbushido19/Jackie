"""
Module pour charger et utiliser le modèle Ollama via LangChain
"""

from langchain_groq import ChatGroq
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class LocalLLM:
    def __init__(self, model_name="meta-llama/llama-4-scout-17b-16e-instruct"):
        """
        Initialise le modèle Ollama local
        """
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
        self.llm = ChatGroq(
            model=model_name,
            callback_manager=callback_manager,
            temperature=0.7,
        )  # Initialiser avec une liste vide de tools

    def generate_response(self, prompt):
        """
        Génère une réponse à partir du prompt
        """
        try:
            response = self.llm.invoke(prompt)
            return response
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse: {str(e)}")
            return None 

# llm = LocalLLM()
# response = llm.generate_response("Explique-moi les différences entre TCP et UDP.")
# print(response)