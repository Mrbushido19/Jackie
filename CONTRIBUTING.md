# Guide de Contribution

Merci de votre intérêt pour contribuer à l'Assistant IA Personnel ! Ce document fournit les informations nécessaires pour contribuer au projet.

## 🎯 Comment Contribuer

### Signaler un Bug

1. **Vérifiez les issues existantes** pour éviter les doublons
2. **Créez une nouvelle issue** avec le template "Bug Report"
3. **Fournissez des détails complets** :
   - Description du problème
   - Étapes pour reproduire
   - Comportement attendu vs observé
   - Version de Python, OS, etc.

### Proposer une Amélioration

1. **Créez une issue** avec le template "Feature Request"
2. **Décrivez clairement** la fonctionnalité souhaitée
3. **Expliquez le bénéfice** pour les utilisateurs

### Soumettre du Code

1. **Forkez le repository**
2. **Créez une branche** pour votre fonctionnalité :
   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   ```
3. **Développez votre code** en suivant les conventions
4. **Testez votre code** localement
5. **Commitez vos changements** avec des messages clairs
6. **Poussez vers votre fork**
7. **Créez une Pull Request**

## 📋 Standards de Code

### Style de Code

- **Python** : Suivez PEP 8
- **Commentaires** : En français, clairs et concis
- **Noms de variables/fonctions** : En anglais, descriptifs
- **Docstrings** : Pour toutes les fonctions publiques

### Structure des Commits

Utilisez des messages de commit conventionnels :

```
type(scope): description courte

Description détaillée si nécessaire
```

Types acceptés :

- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage
- `refactor` : Refactoring
- `test` : Tests
- `chore` : Maintenance

### Tests

- **Ajoutez des tests** pour les nouvelles fonctionnalités
- **Assurez-vous** que tous les tests passent
- **Testez** sur différents environnements si possible

## 🛠️ Configuration de l'Environnement de Développement

### Prérequis

- Python 3.10+
- Git
- Compte Microsoft (pour les tests d'authentification)

### Installation

1. **Clonez votre fork** :

   ```bash
   git clone https://github.com/votre-username/AI_Lab.git
   cd AI_Lab
   ```

2. **Créez un environnement virtuel** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Installez les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez les variables d'environnement** :
   Créez un fichier `.env` :

   ```env
   CLIENT_ID=votre_client_id_microsoft
   CLIENT_SECRET=votre_client_secret_microsoft
   TENANT_ID=votre_tenant_id
   ```

5. **Testez l'installation** :
   ```bash
   streamlit run app.py
   ```

## 📁 Structure du Projet

Comprendre l'architecture pour contribuer efficacement :

- `app.py` : Point d'entrée de l'application Streamlit
- `agents/` : Agents IA et logique métier
- `auth/` : Authentification Microsoft
- `tools/` : Intégrations Microsoft Graph
- `utils/` : Utilitaires et helpers
- `config/` : Configuration de l'application
- `llm/` : Intégration des modèles de langage

## 🔍 Processus de Review

### Avant de Soumettre

- [ ] Code conforme aux standards
- [ ] Tests ajoutés et passants
- [ ] Documentation mise à jour
- [ ] Variables d'environnement documentées
- [ ] Pas de données sensibles dans le code

### Processus de Review

1. **Automatique** : Vérifications CI/CD
2. **Manuel** : Review par les maintainers
3. **Feedback** : Commentaires et suggestions
4. **Mise à jour** : Corrections si nécessaire
5. **Merge** : Intégration après approbation

## 🐛 Dépannage

### Problèmes Courants

**Erreur d'authentification Microsoft** :

- Vérifiez les variables d'environnement
- Assurez-vous que l'app Azure a les bonnes permissions

**Erreur de dépendances** :

- Mettez à jour pip : `pip install --upgrade pip`
- Recréez l'environnement virtuel

**Problèmes Streamlit** :

- Vérifiez la version de Streamlit
- Consultez les logs pour plus de détails

## 📞 Support

- **Issues GitHub** : Pour les bugs et demandes de fonctionnalités
- **Discussions GitHub** : Pour les questions générales
- **Email** : Pour les questions privées (si fourni)

## 🎉 Reconnaissance

Toutes les contributions sont appréciées ! Les contributeurs seront mentionnés dans :

- Le fichier README.md
- Les releases GitHub
- La documentation du projet

## 📄 Licence

En contribuant, vous acceptez que votre code soit sous la même licence que le projet (MIT).

---

Merci de contribuer à l'Assistant IA Personnel ! 🚀
