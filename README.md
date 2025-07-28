# Assistant IA Personnel

Un assistant IA personnel intelligent qui s'intègre avec Microsoft Graph pour gérer vos emails, événements et tâches. L'application utilise Streamlit pour l'interface utilisateur et Ollama pour le traitement du langage naturel.

## 🚀 Fonctionnalités

- **Authentification Microsoft** : Connexion sécurisée via Microsoft Graph
- **Gestion des emails** : Lecture et formatage des emails
- **Gestion des événements** : Consultation et formatage des événements du calendrier (à venir)
- **Gestion des tâches** : Accès aux tâches Microsoft To Do (à venir)
- **Interface intuitive** : Interface web moderne avec Streamlit
- **IA Cloud** : Utilisation de Groq (Llama 4) pour le traitement du langage naturel

## 📋 Prérequis

- Python 3.10 ou supérieur
- Compte Microsoft

## 🛠️ Installation

### Option 1 : Installation locale

1. **Cloner le repository**

   ```bash
   git clone https://github.com/Mrbushido19/AI_Lab.git
   cd AI_Lab
   ```

2. **Créer un environnement virtuel**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement**
   Créer un fichier `.env` à la racine du projet :

   ```env
   CLIENT_ID=votre_client_id_microsoft
   CLIENT_SECRET=votre_client_secret_microsoft
   TENANT_ID=votre_tenant_id
   ```

<!-- 5. **Installer et configurer Ollama**

   ```bash
   # Installer Ollama (voir https://ollama.ai)
   ollama pull llama2  # ou un autre modèle de votre choix
   ``` -->

5. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

## 📁 Structure du projet

```
assistant-ia-personnel/
├── app.py                 # Application principale Streamlit
├── requirements.txt       # Dépendances Python
├── docker-compose.yml     # Configuration Docker Compose
├── DockerFile            # Configuration Docker
├── .env                  # Variables d'environnement (à créer)
├── agents/               # Agents IA
│   └── assistant_agent.py
├── auth/                 # Authentification Microsoft
│   └── ms_auth.py
├── tools/                # Outils d'intégration Microsoft Graph
│   └── graph_tools.py
├── utils/                # Utilitaires
├── config/               # Configuration
└── llm/                  # Intégration LLM
```

## 🎯 Utilisation

1. **Démarrer l'application** selon votre méthode d'installation
2. **Se connecter** avec votre compte Microsoft
3. **Poser des questions** à l'assistant, par exemple :
   - "Montre-moi mes derniers emails"
   - "Quels sont mes événements de cette semaine ?" (à venir)
   - "Liste mes tâches en cours" (à venir)

## 🔒 Sécurité

- L'authentification utilise le flux Device Code de Microsoft
- Les tokens sont stockés en session uniquement
- Aucune donnée sensible n'est persistée localement

## 🐛 Dépannage

### Problèmes d'authentification

- Vérifier que les variables d'environnement sont correctement configurées
- S'assurer que l'application Azure a les bonnes permissions

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 📞 Support

Pour toute question ou problème, veuillez ouvrir une issue sur le repository GitHub.
