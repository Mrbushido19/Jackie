"""
Configuration pour Microsoft Graph API
"""

# Scopes d'autorisation pour Microsoft Graph
SCOPES = [
"https://analysis.windows.net/powerbi/api/.default"
]

ID_DSI = "b!f3O0faShx0iwk0R2JI5WXzN__sQNH8tKqCROBvxQL6nqoIFE2Rd0R5TdiELtmG-K"
SHAREPOINT_SITE = "lcrci.sharepoint.com,7db4737f-a1a4-48c7-b093-4476248e565f,c4fe7f33-1f0d-4acb-a824-4e06fc502fa9"
# Configuration de l'API Microsoft Graph
GRAPH_ENDPOINT = "https://graph.microsoft.com/v1.0"
GRAPH_BETA_ENDPOINT = "https://graph.microsoft.com/beta"

# Endpoints spécifiques
ENDPOINTS = {
    "me": "/me",
    "messages": "/me/messages",
    "events": "/me/events",
    "tasks": "/me/todo/lists",
    "reporting" : f"/sites/{SHAREPOINT_SITE}/drives/{ID_DSI}/root:/PDF REPORTING/FICHIER PDF FABRIC:/children"
} 
