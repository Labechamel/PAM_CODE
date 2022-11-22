#ceci est un programme pour tester l'import de données d'une table MySQL dans une liste python
#--------------------------------------------------------------------------------------------------------------------------#
#import des modules utiles
import mysql.connector

#création liste vide 
Listetest = [] 

connection_params = {
    'host': "127.0.0.1",
    'user': "root",
    'password': "Pierre_11021999",
    'database': "Ecole",
}

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pierre_11021999",
    database="Ecole"
)

# faire quelque chose d'utile avec la connexion

#----------------------------------------
#insérer des nouvelles données dans la table 
#with mysql.connector.connect(**connection_params) as db :
    #with db.cursor() as c:
        #c.execute("insert into data (id, name, country, age, salary) \
                   #values (101, 'bechamel', 'listenbourg', 44, '111.1111117421836')")
        #db.commit()
# faire quelque chose d'utile avec le curseur

#selectionner des données de la BDD ------------------
request = "select id, name, country, age, salary from data where name = 'bechamel' "


with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c:
        c.execute(request)
        resultats = c.fetchall()
        for data in resultats:
            print(data)

#fermer la connexion à la base de donnée
#db.close()