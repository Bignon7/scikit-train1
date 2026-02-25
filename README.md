# 📁 Extensions de fichiers en Machine Learning (Résumé)

## 🐍 .py
Fichier Python classique.
- Contient du code exécutable.
- Utilisé pour scripts, entraînement de modèles, applications.
- Exécution : `python fichier.py`
- Format professionnel pour les projets.

---

## 📓 .ipynb
Fichier Jupyter Notebook.
- Code exécuté cellule par cellule.
- Permet d’ajouter texte, graphiques, explications.
- Très utilisé en data science et apprentissage.
- Idéal pour exploration et prototypage.

---

## 📊 .csv
Fichier de données (tableau).
- Peut être ouvert avec Excel.
- Utilisé pour stocker datasets.
- Chargé en Python avec pandas.

---

## 📦 .pkl
Fichier pickle.
- Sert à sauvegarder un modèle entraîné.
- Permet de recharger le modèle sans réentraîner.

---

## 📝 .md
Fichier Markdown.
- Sert à écrire documentation (README).
- Utilisé sur GitHub.
- Permet formatage simple (titres, listes, etc.).

---

# 🎯 Résumé rapide

| Extension | Utilité principale |
|------------|-------------------|
| .py | Script Python |
| .ipynb | Notebook interactif |
| .csv | Données |
| .pkl | Modèle sauvegardé |
| .md | Documentation |

---

# 🏆 Conseil débutant

- Apprendre → utiliser `.ipynb`
- Projet propre → utiliser `.py`
- Toujours documenter avec `.md`







































# 🌐 Déployer un modèle ML gratuitement

## 1️⃣ Streamlit
- Framework Python pour créer des apps interactives.
- Gratuit via [Streamlit Community Cloud](https://streamlit.io/cloud)
- Avantages :
  - Simple à utiliser
  - Intègre graphiques et widgets
- Idée : charger ton modèle `.pkl` et créer une interface utilisateur pour entrer des données et afficher la prédiction.

---

## 2️⃣ Gradio
- Interface web rapide pour modèles ML.
- Gratuit
- Avantages :
  - Crée des démos interactives en quelques minutes
  - Supporte images, texte, audio
- Idée : interface pour upload d’images ou texte et prédiction instantanée.

---

## 3️⃣ Hugging Face Spaces
- Hébergement gratuit pour modèles ML et apps Streamlit/Gradio
- Publie ton projet avec un lien public
- Idéal pour partager des projets en ligne rapidement.

---

## 4️⃣ Google Colab
- Notebook Python dans le cloud
- Gratuit
- Avantages :
  - Partage ton notebook directement
  - Exécution du modèle sans serveur dédié
- Limitation : ce n’est pas une vraie app web, juste un notebook interactif.

---

## 5️⃣ GitHub Pages + API
- Déployer un frontend web et connecter ton modèle via une API (ex : Flask, FastAPI)
- Gratuit mais plus technique
- Idéal pour projets plus avancés.

---

# 🎯 Résumé rapide

| Option | Type | Facilité | Gratuit |
|--------|------|----------|---------|
| Streamlit Cloud | Web app Python | ⭐⭐⭐ | Oui |
| Gradio | Web app Python | ⭐⭐⭐⭐ | Oui |
| Hugging Face Spaces | Web app + modèle | ⭐⭐⭐ | Oui |
| Google Colab | Notebook interactif | ⭐⭐ | Oui |
| GitHub Pages + API | Web + backend | ⭐ | Oui (technique) |

---

💡 Conseil débutant : **Streamlit** ou **Gradio** → lien partageable en moins de 30 minutes.