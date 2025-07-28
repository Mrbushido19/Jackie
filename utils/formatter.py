"""
Fonctions utilitaires pour la mise en forme des données
"""
from datetime import datetime

def format_email(email_data):
    """Formate les données d'email pour l'affichage"""
    return {
        "sujet": email_data.get("subject", "Sans sujet"),
        "expéditeur": email_data.get("from", {}).get("emailAddress", {}).get("name", "Inconnu"),
        "date": format_date(email_data.get("receivedDateTime")),
        "contenu": email_data.get("bodyPreview", "Pas de contenu")
    }

def format_event(event_data):
    """Formate les données d'événement pour l'affichage"""
    return {
        "titre": event_data.get("subject", "Sans titre"),
        "début": format_date(event_data.get("start", {}).get("dateTime")),
        "fin": format_date(event_data.get("end", {}).get("dateTime")),
        "lieu": event_data.get("location", {}).get("displayName", "Non spécifié")
    }

def format_task(task_data):
    """Formate les données de tâche pour l'affichage"""
    return {
        "titre": task_data.get("title", "Sans titre"),
        "statut": task_data.get("status", "Non spécifié"),
        "date_limite": format_date(task_data.get("dueDateTime", {}).get("dateTime")),
        "importance": task_data.get("importance", "Normal")
    }

def format_date(date_str):
    """Formate une date ISO en format lisible"""
    if not date_str:
        return "Non spécifié"
    try:
        date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return date.strftime("%d/%m/%Y %H:%M")
    except:
        return date_str 