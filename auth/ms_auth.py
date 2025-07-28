"""
Module d'authentification Microsoft avec MSAL
"""
import os
from msal import PublicClientApplication
from dotenv import load_dotenv
from config.graph_config import SCOPES

load_dotenv()

class MSAuthenticator:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.tenant_id = os.getenv("TENANT_ID")
        self.authority = f"https://login.microsoftonline.com/{self.tenant_id}"
        self.app = PublicClientApplication(
            client_id=self.client_id,
            authority=self.authority
        )

    def initiate_device_flow(self):
        """
        Initialise le device flow et retourne le message à afficher à l'utilisateur ainsi que le flow complet
        """
        try:
            flow = self.app.initiate_device_flow()
            if "user_code" not in flow:
                raise ValueError("Erreur lors de l'initialisation du device flow")
            return flow["message"], flow
        except Exception as e:
            print(f"Erreur d'initialisation du device flow: {str(e)}")
            return None, None

    def acquire_token_by_flow(self, flow):
        """
        Récupère le token d'accès à partir d'un flow existant
        """
        try:
            result = self.app.acquire_token_by_device_flow(flow)
            print(result)
            if "access_token" in result:
                return result["access_token"]
            else:
                raise ValueError("Erreur lors de l'obtention du token")
        except Exception as e:
            print(f"Erreur d'authentification: {str(e)}")
            return None 
        

