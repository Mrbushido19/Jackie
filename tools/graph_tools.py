"""
Outils pour interagir avec Microsoft Graph API
"""
import requests
from utils.utils import nettoyer, download_file, clean_filename
from bs4 import BeautifulSoup
from config.graph_config import GRAPH_ENDPOINT, ENDPOINTS



class GraphTools:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def get_user_info(self, _input: str):
        """Récupère les informations de l'utilisateur"""
        try:
            response = requests.get(
            f"{GRAPH_ENDPOINT}{ENDPOINTS['me']}",
            headers=self.headers
            )
            return response.json()
        except requests.exceptions.HTTPError as e:
            Errormessage = "Erreur lors de la récupération des informations utilisateur: {e}"
            return Errormessage
    def get_emails_bysearch(self, _input: str):
        """retourne une liste d'emails contenant le mot-clé de recherche"""
        response = requests.get(
            f"{GRAPH_ENDPOINT}{ENDPOINTS['messages']}?$search={_input}",
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json().get('value', [])

        emails = []

        for email in data:
            subject = email.get('subject', '(Sans sujet)')
            sender = email.get('sender', {}).get('emailAddress', {}).get('address', '(Sans expéditeur)')
            body = email.get('body', {})
            content_type = body.get('contentType', '').lower()
            content = body.get('content', '')

            if content_type == 'html':
                soup = BeautifulSoup(content, 'html.parser')
                content = soup.get_text()

            content = nettoyer(content)
            emails.append({
                "subject": subject,
                "content": content,
                "sender": sender
            })

        return emails
    def get_emails(self, _input: str = None):
        """Retourne une liste d'emails depuis la messagerie de l'utilisateur"""
        response = requests.get(
            f"{GRAPH_ENDPOINT}{ENDPOINTS['messages']}",
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json().get('value', [])

        emails = []

        for email in data:
            subject = email.get('subject', '(Sans sujet)')
            sender = email.get('sender', {}).get('emailAddress', {}).get('address', '(Sans expéditeur)')
            body = email.get('body', {})
            content_type = body.get('contentType', '').lower()
            content = body.get('content', '')

            if content_type == 'html':
                soup = BeautifulSoup(content, 'html.parser')
                content = soup.get_text()

            content = nettoyer(content)
            emails.append({
                "subject": subject,
                "content": content,
                "sender": sender
            })

        return emails

    def get_reportings(self, _input: str = None):
        """Télécharge les fichiers du dossier Reporting dans SharePoint et les sauvegarde dans le dossier ./downloads"""
        response = requests.get(
            f"{GRAPH_ENDPOINT}{ENDPOINTS['reporting']}",
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json().get('value', [])


        for item in data:
            name = item.get('name', '(Sans nom)')
            clean_name = clean_filename(name) + ".pdf"
            web_url = item.get('webUrl', '')
            id = item.get('id', '')
            download_url = item.get('@microsoft.graph.downloadUrl', '')

            file_path = f"./downloads/{clean_name}"
            download_file(download_url, file_path)
        