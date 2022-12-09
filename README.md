
# ExcelCar PAM ECAM Rennes 2022

Il s'agit d'un projet réalisé dans le cadre de notre dernière année d'école d'ingénieur. Ce projet n'est pas la version finale mais une première version initiale qui sera ensuite reprise par de prochains groupes d'élèves qui amélioreront cette version et implémenteront de nouvelles choses. Par exemple, nous avons pensé à l'hébergement de la base de données dans le cloud, le déploiement du projet du projet via un conteneur docker ou encore l'automatisation de l’installation de mysql et python par un fichier exécutable, etc…


## Explication du projet
Ce projet a pour but de reproduire une chaine de montage de portière avant et arrière de voitures. Les étudiants de dernières années du module génie industriel seront amenés a utilisé cette IHM afin de simuler le montage de ces portières comme s'ils étaient sur la ligne de production et ainsi de proposer des améliorations pouvant être mises en place sur le site PSA Peugeot de Rennes.

En effet, chaque portière passe par 4 machines et nous affichons les données suivantes sur l'IHM réalisé : leurs vitesses, la distance qu’elles parcourent, le nombre de pièce sur chaque poste ainsi que les techniciens qui y travaillent. 


## Screenshots de l'IHM

![App Screenshot](https://raw.githubusercontent.com/Labechamel/PAM_CODE/master/screenshot/ihm.png)


## Installation & Run

1 - Clonez ou téléchargez en zip le projet

```bash
  git clone https://github.com/Labechamel/PAM_CODE
```

2 - Allez dans le dossier tuto_installation [ou cliquez ici](https://github.com/Labechamel/PAM_CODE/tree/master/Tutoriel)

```bash
  Suivez les deux tutoriels pour installer Mysql ainsi que Python 
```

3 - Une fois MySQL installé et python installé, nous allons installer les librairies python nécessaires pour exécuter le programme

```bash
  Ouvrez l invité de commande depuis le dossier du projet et executez la commande ci-dessous :

  pip install -r requirements.txt
```

4 - Enfin, executez le programme

```bash
  Ouvrez l invité de commande depuis le dossier du projet et executez la commande ci-dessous :

  python Start.py
```

## Documentation

Suivez les deux tutoriels pour installer Mysql ainsi que Python depuis le dossier téléchargé ou depuis le lien ci-dessous

- [Tuto installation MySQL](https://github.com/Labechamel/PAM_CODE/blob/master/Tutoriel/Guide%20d'installation%20MySQL%20Windows%20Version%20Finale.pdf)
N'oubliez pas de cliquer sur "more pages" en bas de la page pour voir la suite du tuto

- [Tuto installation Python](https://github.com/Labechamel/PAM_CODE/blob/master/Tutoriel/Guide%20d'installation%20python%203.11.pdf)

## Télécharger les installer

- [Installer MySQL](https://dev.mysql.com/downloads/file/?id=514518/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.31.0.msi)
  Cliquez sur "No thanks, just start my download."

- [Installer Python 3.11](https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe)


## Technologies

**Langage:** Python

**BDD:** MySQL

**IHM:** Qtdesigner

## Methodologies 

- Pseudo-agile 

- Sprint de 2 à 3 semaines


## Améliorations envisageables

- Hébergement de la base de données dans le cloud (AWS par exemple)
- Automatisation de l’installation de mysql et python (par un fichier exécutable)
- Déploiement du projet via un conteneur Docker



## Authors

- [@Labechamel](https://github.com/Labechamel)
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://simonbechu.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bechu-simon/)
- [@pierre-mhx](https://github.com/pierre-mhx)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pierremahieux-sales/)
- [@KolyaGud](https://github.com/KolyaGud)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kolya-gudenkauf-6807b5195/)
- Nathan_vds
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nathan-vanderschelden-35ab54173/)
## Used By

This project is used by the following companie:

- [ECAM RENNES Louis De Broglie](https://www.ecam-rennes.fr/)

