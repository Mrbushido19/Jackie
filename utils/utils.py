import wget
import re
import os

def download_file(url, file_name):
    """
    Télécharge un fichier depuis une URL et le sauvegarde à l'emplacement spécifié.
    
    :param url: URL du fichier à télécharger   """

    if os.path.exists(file_name):
        print(f"Le fichier existe déjà : {file_name}. Téléchargement annulé.")
        return
    try:
        wget.download(url, out=file_name)
        print(f"\nFichier téléchargé avec succès : {file_name}")
    except Exception as e:
        print(f"Erreur lors du téléchargement du fichier : {str(e)}")


def nettoyer(text):
    """
    Coupe le texte au niveau du motif suspect (avant les longues suites d'espaces insécables + "De").
    """
    # Pattern : beaucoup de \xa0 ou espaces classiques suivis de "De"
    match = re.search(r"(.+?)(?:[\s\xa0]{5,}De)", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text.strip()

def clean_filename(name):
    """Nettoie le nom de fichier pour éviter les caractères invalides"""
    name = re.sub(r'[\\/*?:"<>|]', "", name)  # Supprime les caractères interdits
    name = name.replace(" ", "_")
    return name