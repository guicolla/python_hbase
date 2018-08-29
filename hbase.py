#Script que conecta no hbase e cria uma "tabela" com os valores de um arquivo.
from starbase import Connection

c = Connection("192.168.56.13","8000")

ratings = c.table("ratings")

if (ratings.exists()):
   print("drop rattings table")
   ratings.drop()

ratings.create('ratings')

ratingFile = open("/tmp/ml-100k/u.data","r")

batch = ratings.batch()

for line in ratingFile:
   (userID,movieID,rating,timestamp) = line.split()
   print(userID, movieID, rating, timestamp)
   batch.update(userID, {'ratings': {movieID: rating}})
   print(batch.update(userID, {'ratings': {'50': '1'}}))

ratingFile.close()

batch.commit(finalize=True)
