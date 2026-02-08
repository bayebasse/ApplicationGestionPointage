import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root", 
    password="1234",
    database="GestionApprenant"
)
curseur=connection.cursor()
while True:
    print("*********Voici le Menu*********")
    print("1.Ajouter un Apprenant : ")
    print("2. Enregister un Apprenant comme Présent: ")
    print("3. La liste des Apprenants Présents: ")
    print("4. Rechercher un Apprenant: ")
    print("9: Quitter le Programme :")
    print("")
    print("                             ")
    choix=input("Choississez une option : ")
    match choix:
        case "1":
            Nom_Apprenant=input("Entrez votre nom SVP: ")
            Prenom_Apprenant=input("Entrez votre prénom: ")
            Promo_Apprenant=input("Entrez vootre promo: ")
            sql="""
    insert into Apprenants(Nom_Apprenant, Prenom_Apprenant, Promo_Apprenant)
    values (%s, %s, %s)
    """
            curseur.execute(sql,(Nom_Apprenant, Prenom_Apprenant,Promo_Apprenant))
            connection.commit()
            print("Apprenant ajouté avec succès")
        case "2":
            curseur.execute("select * from Apprenants")
            resultats=curseur.fetchall()
            print("Voici la liste de tous les Apprenants : ")
            for ligne in resultats:
                print(ligne)
            choix2=int(input("Entrez l'ID de L'apprenant que tu veux marquer Présent: "))
            sql="update Apprenants set Presence_Apprenant='Présent' where ID_Apprenant=%s"
            curseur.execute(sql,(choix2,))
            connection.commit()
            curseur.execute("select * from Apprenants")
            resultats=curseur.fetchall()
            print("Voici  Maintenant la liste des Apprenants, Ce qui sont présents ou Absents : ")
            for ligne in resultats:
                print(ligne)
        case "3":
            sql="select * from Apprenants where Presence_Apprenant=%s"
            curseur.execute(sql,('Présent',))
            resultats=curseur.fetchall()
            print("*** La liste des Apprenants Présents: *** " )
            for ligne in resultats:
                print(ligne)
        case "4":
            recherche=int(input("Entrez l'ID de l'Apprenant SVP  :"))
            sql="select * from Apprenants where ID_Apprenant=%s"
            curseur.execute(sql,(recherche,))
            resultats=curseur.fetchall()
            print("L'Apprenant que vous recherchez est :   ")
            for ligne in resultats:
                print(ligne)
        case "9":
            print("Vous avez quitté le Programme")
            break
        
        
            
    
