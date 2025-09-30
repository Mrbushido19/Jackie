"""
Module pour charger et utiliser le modèle Ollama via LangChain (Chat interface)
"""
import os
from langchain_core import callbacks
from langchain_groq import ChatGroq
# from langchain_ollama.chat_models import ChatOllama
# from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
class LocalLLM:
    def __init__(self, model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"):
        """
        Initialise le modèle Ollama local via l'interface Chat
        """
        callback_manager = [StreamingStdOutCallbackHandler()]
        api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(
            api_key=api_key,
            model=model_name, 
            callback_manager=callback_manager, 
            temperature=0.7
        )

    def generate_response(self, prompt: str) -> str | None:
        """
        Génère une réponse à partir du prompt
        """
        try:
            # ChatOllama attend une liste de messages (HumanMessage, SystemMessage, etc.)
            response = self.llm.invoke([HumanMessage(content=prompt)])
            return response.content
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse: {str(e)}")
            return None


# Exemple d'utilisation
# llm = LocalLLM()  # ou "llama2", "phi3", etc.
# response = llm.generate_response("Explique-moi les différences entre TCP et UDP.")
# print(response)
