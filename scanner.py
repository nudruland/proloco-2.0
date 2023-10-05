import csv
import operator

NUMBER_DIFFERENCE = 2
MAX_NUMBER_OF_FOUR_PLANCE = 3
MAX_NUMBER_OF_THREE_PLANCE = 5
MAX_NUMBER_OF_TWO_PLANCE = 30
MAX_NUMBER_OF_ONE_PLANCE = 20


# Using a class
class Prenotazione:
    def __init__(self, myname, mynumber, mycomment):
        self.name = myname
        self.number = mynumber
        self.comment = mycomment

class Tavoli:
    def __init__(self, myname, mynumber, mycomment):
        self.name = myname
        self.number = mynumber
        self.comment = mycomment

listaTavoliìQuadrupli = [] 
listaTavoliTripli = [] 
listaTavoliDoppi = [] 
listaTavoliSingoli = []
listaTavoli = []

listPrenotazione = [] 
listPrenotazioneSalotto = []
listaPasseggino = []

with open("./proloco/prenotati1.csv", "r") as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    x = str(row)
    x = x.strip()
    first = x.find(";")
    first_name = x[2:first]
    second = x.find(";", first + 1,  len(x))
    number_of_person = x[first + 1 : second]

    if ((second + 1) <  (len(x) - 2)) :
      comment = str(x[second + 1 : len(x) - 2])
      myPrenotazione = Prenotazione(first_name, int(number_of_person), comment)   
    else :
      myPrenotazione = Prenotazione(first_name, int(number_of_person), "NULL") 

    listPrenotazione.append(myPrenotazione)

for x in listPrenotazione :
  if x.comment != "NULL" :
      
      match x.comment :
        case "salotto"  :
          listPrenotazioneSalotto.append(x)
        case "Salotto" :
          listPrenotazioneSalotto.append(x)

      if x.comment.find("passeggin") >= 0 or x.comment.find("Passeggin") >= 0 : 
        listaPasseggino.append(x)
      elif x.comment.find("Vicino a ") >= 0 or x.comment.find("vicino a ") >= 0 :
        offset = x.comment.find("Vicino a ") + x.comment.find("vicino a ") + 1
        name_to_be_neared = x.comment[(len("Vicino a ") + offset) :]
        for k in listPrenotazione : 
          if k.name == name_to_be_neared :
            k.name = k.name + " + " + name_to_be_neared 
            temp = k.number
            k.number = temp + x.number
            k.number
        listPrenotazione.remove(x)

#custom function to get number info
sorted_list = sorted(listPrenotazione, key=lambda x: x.number, reverse=True)
#sorted_x = sorted(listPrenotazione, key=operator.attrgetter('number'))

for obj in sorted_list:
    print(obj.name, obj.number)


          

          
          
        

      

      


    

