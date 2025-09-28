"""
Module pour charger et utiliser le modèle Ollama via LangChain (Chat interface)
"""

from langchain_community.chat_models import ChatOllama
# from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.messages import HumanMessage

class LocalLLM:
    def __init__(self, model_name: str = "mistral"):
        """
        Initialise le modèle Ollama local via l'interface Chat
        """
        callback_manager = [StreamingStdOutCallbackHandler()]
        
        self.llm = ChatOllama(
            base_url="http://172.16.10.92:11434",
            model=model_name,
            callback_manager=callback_manager,
            temperature=0.7,
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
# llm = LocalLLM("mistral")  # ou "llama2", "phi3", etc.
# response = llm.generate_response("Explique-moi les différences entre TCP et UDP.")
# print(response)
