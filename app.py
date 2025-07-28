"""
Interface utilisateur Streamlit pour l'agent IA
"""
import streamlit as st
from auth.ms_auth import MSAuthenticator
from tools.graph_tools import GraphTools 
# from tools.pow_bi_tools import BiTools
from agents.assistant_agent import AssistantAgent
from utils.formatter import format_email, format_event, format_task

def initialize_session_state():
    """Initialise les variables de session"""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "agent" not in st.session_state:
        st.session_state["agent"] = None
    if "auth_flow" not in st.session_state:
        st.session_state["auth_flow"] = None
    if "auth_message" not in st.session_state:
        st.session_state["auth_message"] = None


def authenticate():
    """Gère l'authentification Microsoft via device flow"""
    authenticator = MSAuthenticator()
    # Si aucun flow n'est en cours, on l'initie
    if st.session_state["auth_flow"] is None:
        message, flow = authenticator.initiate_device_flow()
        if flow is not None:
            st.session_state["auth_flow"] = flow
            st.session_state["auth_message"] = message
        else:
            st.session_state["auth_message"] = "Erreur lors de l'initialisation du device flow."
        return False
    # Sinon, on tente d'obtenir le token
    token = authenticator.acquire_token_by_flow(st.session_state["auth_flow"])
    if token:
        st.session_state.authenticated = True
        graph_tools = GraphTools(token)
        # bi_tools = BiTools(token)
        st.session_state.agent = AssistantAgent(graph_tools)
        st.session_state["auth_message"] = "Authentification réussie !"
        st.session_state["auth_flow"] = None
        return True
    return False


def main():
    """Fonction principale de l'application"""
    st.title("Assistant IA Personnel")
    initialize_session_state()

    if not st.session_state.authenticated or st.session_state.agent is None:
        st.write("Veuillez vous authentifier pour continuer")
        if st.session_state["auth_message"]:
            st.info(st.session_state["auth_message"])
            # Tentative automatique de récupération du token
            if authenticate():
                st.success("Authentification réussie!")
                st.rerun()
            # Pas de bouton, on attend juste que l'utilisateur termine l'authentification côté Microsoft
        else:
            if st.button("Se connecter"):
                authenticate()
                st.rerun()
    else:
        # Interface de chat
        st.write("Comment puis-je vous aider aujourd'hui?")
        
        # Zone de saisie
        user_input = st.text_input("Votre message:", key="user_input")
        
        if user_input:
            try:
                # Traitement de la requête
                response = st.session_state.agent.process_query(user_input)
                
                # Affichage de la réponse
                st.write("Réponse:", response)
            except AttributeError:
                st.error("Une erreur s'est produite. Veuillez vous reconnecter.")
                st.session_state.authenticated = False
                st.session_state.agent = None
                st.rerun()

if __name__ == "__main__":
    main() 