import mysql.connector as mysql

db = mysql.connect(
  host="localhost",
  user="student",
  password="simplon"
)

cursor = db.cursor()

cursor.execute("USE parcours_combattant")

# cursor.execute("""INSERT INTO Soldat (id_soldat, nom, prenom, grade)
#                VALUES(1, 'Dupont', 'Jean', 'Caporal'),
#                     (2, 'Durant', 'François', 'Soldat'),
#                     (3, 'Dutronc', 'Fabrice', 'Caporal-chef'),
#                     (4, 'Fabre', 'Lilian', 'Soldat'),
#                     (5, 'Dupond', 'Hervé', 'Sergent');
#                """)
#
# cursor.execute("""INSERT INTO Mail(id_mail, id_soldat, mail)
#                VALUES(1, 1, 'j.dupont@gmail.com'),
#                     (2, 2, 'f.durant@gmail.com'),
#                     (3, 3, 'f.dutronc@gmail.com'),
#                     (4, 4, 'l.fabre@gmail.com'),
#                     (5, 5, 'h.dupond@gmail.com');
#                """)
#
# cursor.execute("""INSERT INTO Obstacle
#                VALUES(1, 'poutres jumelées', 0, 1),
#                     (2, 'gué', 1, 1),
#                     (3, 'chicane', 2, 1),
#                     (4, 'espalier', 3, 2),
#                     (5, 'grimper de corde', 5, 2);
#                """)
#
# cursor.execute("""INSERT INTO Examen
#                VALUES(1, '2018-04-16', 1, 1, 0, 1, '2018-04-16 9:05:00', '2018-04-16 9:36:36', 1),
#                     (2, '2018-04-16', 1, 2, 1, 4, '2018-04-16 09:37:00', '2018-04-16 10:01:06', 1),
#                     (3, '2018-07-14', 2, 1, 1, 4, '2018-07-22 11:25:00', '2018-07-22 11:53:42', 1),
#                     (4, '2018-07-14', 2, 2, 1, 6, '2018-07-22 11:55:26', '2018-07-22 12:21:42', 1),
#                     (5, '2019-02-23', 2, 4, 3, 2, '2018-07-22 12:52:11', '2018-07-22 13:22:42', 2);
#                """)
# db.commit()

## Affichage des tables
# cursor.execute("SHOW TABLES")
# print([table for table in cursor.fetchall()])

# Affichage des colonnes de la table Soldat
print(cursor.execute("""SELECT * FROM Soldat"""))
print([column for column in cursor.fetchall()])

# Modification du nom, du prenom et du grade du soldat possédant l'id 1
cursor.execute("""UPDATE Soldat
                  SET nom='Dupont', prenom='Jean', grade = 'Caporal'
                  WHERE id_soldat = 1""")
db.commit()

print(cursor.execute("""SELECT * FROM Soldat"""))
print([column for column in cursor.fetchall()])

# Suppression des éléments concernant le soldat avec l'id 1
cursor.execute("""
                DELETE FROM Soldat
                WHERE id_soldat = 1
                """)
db.commit()

print(cursor.execute("""SELECT * FROM Soldat"""))
print([column for column in cursor.fetchall()])