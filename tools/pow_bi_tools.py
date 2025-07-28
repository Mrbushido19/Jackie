import msal
import requests


class BiTools:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
    
    def get_user_workspaces(self, _input: str = None):
        """
        Récupère les espaces de travail Power BI de l'utilisateur.
        Retourne une liste de workspaces.
        """
        url = "https://api.powerbi.com/v1.0/myorg/groups"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
                workspaces = response.json().get('value', [])
                # Extraction des infos utiles
                return [
                    {
                        "id": ws.get("id"),
                        "name": ws.get("name"),
                        "type": ws.get("type"),
                    }
                    for ws in workspaces
                ]
        else:
                raise Exception(f"Erreur lors de la récupération des espaces de travail: {response.status_code} - {response.text}")
# def requete_power_bi(endpoint, methode="GET", params=None, data=None):
#     """
#     Effectue une requête à l'API Power BI avec authentification.
#     endpoint: chemin relatif de l'API (ex: 'groups')
#     methode: 'GET', 'POST', etc.
#     params: paramètres de requête (dict)
#     data: données à envoyer (dict)
#     """
#     token = obtenir_token_access()
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json"
#     }
#     url = POWER_BI_API_URL + endpoint
#     response = requests.request(methode, url, headers=headers, params=params, json=data)
#     if response.status_code >= 200 and response.status_code < 300:
#         return response.json()
#     else:
#         raise Exception(f"Erreur API Power BI: {response.status_code} - {response.text}")

# # Exemple d'utilisation :
# # result = requete_power_bi("groups")
# # print(result)
