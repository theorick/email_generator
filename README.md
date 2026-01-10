📧 Name2Mail

Name2Mail est un outil OSINT permettant de rechercher et générer des adresses email potentielles à partir d’un nom/prénom et d’informations complémentaires, en utilisant des moteurs de recherche publics.

⚠️ Outil à but éducatif et légal uniquement.

🕵️‍♂️ Description

Name2Mail automatise la recherche d’adresses email visibles publiquement sur le web en utilisant :

🔍 Le moteur de recherche Ecosia

🌐 Playwright pour la navigation automatisée

🧠 BeautifulSoup pour l’analyse HTML

🧾 Extraction d’emails via Regex

Les résultats sont sauvegardés dans un fichier info.txt.

✨ Fonctionnalités

Recherche d’emails liés à :

- Prénom + Nom

- Informations supplémentaires (entreprise, pseudo, ville, etc.)

Support de plusieurs domaines :

- gmail.com

- hotmail.com

- outlook.com

- yahoo.com

- protonmail.com

- Détection et suppression des doublons

- Sauvegarde automatique des résultats

📦 Prérequis

Python 3.9+

Google Chromium (installé automatiquement par Playwright)

Modules Python requis

pip install playwright beautifulsoup4 pyfiglet


Puis installer le navigateur Playwright :


playwright install



📁 Structure du projet
Name2Mail/
│

├── name2mail.py

├── info.txt

├── README.md

⚠️ Avertissement légal

Ce projet est destiné exclusivement à :

- L’apprentissage

- La recherche OSINT

- Les audits de sécurité autorisés

- Les enquêtes légales


❌ Toute utilisation à des fins de :

- harcèlement

- spam

- phishing

- atteinte à la vie privée

- est strictement interdite.

- L’auteur décline toute responsabilité en cas de mauvaise utilisation.


👤 Auteur

Théorick

Projet OSINT personnel


⭐ Contribution

Les contributions sont les bienvenues !

- Fork le projet

- Crée une branche

- Commit tes modifications

- Ouvre une Pull Request
