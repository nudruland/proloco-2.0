import csv
import operator

NUMBER_DIFFERENCE = 2
MAX_NUMBER_OF_FOUR_PLANCE = 3
MAX_NUMBER_OF_THREE_PLANCE = 5
MAX_NUMBER_OF_TWO_PLANCE = 30
MAX_NUMBER_OF_ONE_PLANCE = 20
TOTAL_NUMBER_OF_PLANCE = 50

ONE_PLANCIA = 0
TWO_PLANCE = 1
THREE_PLANCE = 2
FOUR_PLANCE = 3
FIVE_PLANCE = 4
SIX_PLANCE = 5
NOT_PLACED = 6

MAX = [8, 16, 24, 32, 40, 48, 56]
OFFSET_FIRST = 2
MIN_FIRST_ROUND = [0, 0, 0, 0, 0, 0, 0, 0]
OFFSET_SECOND = 2
MIN_SECOND_ROUND = [0, 0, 0, 0, 0, 0, 0, 0]

# Using a class
class Prenotazione:
    def __init__(self, myname, mynumber, mycomment):
        self.name = myname
        self.number = mynumber
        self.comment = mycomment

class Tavoli:
    def __init__(self, myname, mynumber, mycomment):
        self.name = myname
        self.number = int(mynumber)
        self.comment = mycomment

listaTavoli = [[], [], [], [], [], [], []]

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

print(len(listPrenotazione))

for x in listPrenotazione :
  if x.comment != "NULL" :
      
      match x.comment :
        case "salotto"  :
          listPrenotazioneSalotto.append(x)
          listPrenotazione.remove(x)
        case "Salotto" :
          listPrenotazioneSalotto.append(x)
          listPrenotazione.remove(x)

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
sorted_list = sorted(listPrenotazione, key=lambda x: x.number) #is sorted starting from the bigger [0] to the smaller [end]

for i in range(7) :
  MIN_FIRST_ROUND[i] = MAX[i] - OFFSET_FIRST
  MIN_SECOND_ROUND[i] = MAX[i] - OFFSET_SECOND

for instance in sorted_list :
  i = 0
  inserted = False 
  while (i < 7 and inserted == False) :
    if(int(MAX[i]) >= int(instance.number) >= int(MIN_FIRST_ROUND[i])) :
       inserted = True
       listaTavoli[i].append(instance)
    else :
        i += 1
  if inserted == False :
        listaTavoli[NOT_PLACED].append(instance)

listaPrenotati_not_placed_decreasing_order = []
listaPrenotati_not_placed_decreasing_order = sorted(listaTavoli[NOT_PLACED], key=lambda x: x.number, reverse=True) 

counter_decreasing = 0
counter_increasing = 0
print(len(listaTavoli[NOT_PLACED]))
#listaTavoli[NOT_PLACED] is in increasing order

for instance_increasing in listaTavoli[NOT_PLACED] : 
  placed = False

  for instance_decreasing in listaPrenotati_not_placed_decreasing_order : 
    sum = int(instance_decreasing.number) + int(instance_increasing.number)
    for i in range(len(MAX)) :
      if(int(MAX[i]) >= int(sum) >= int(MIN_SECOND_ROUND[i])) :
        #print(instance_decreasing.name, " + ", instance_increasing.name, "  ", instance_increasing.number , instance_decreasing.number, MAX[i], MIN_SECOND_ROUND[i])
        placed = True

        instance_decreasing.name += (" + " + str(instance_increasing.name))
        instance_decreasing.number += int(instance_increasing.number)
        
        listaTavoli[NOT_PLACED].remove(instance_increasing)
        listaPrenotati_not_placed_decreasing_order.remove(instance_increasing)

        listaTavoli[i].append(instance_decreasing)
        #print(listaTavoli[i][len(listaTavoli[i]) - 1].name, listaTavoli[i][len(listaTavoli[i]) - 1].number)
        
        listaPrenotati_not_placed_decreasing_order.remove(instance_decreasing)
        listaTavoli[NOT_PLACED].remove(instance_decreasing)
        
        break  
    if (placed == True) : 
      break

print(len(listaTavoli[NOT_PLACED]))
for i in listaTavoli[NOT_PLACED] :
  print(i.name, i.number)

















          

          
          
        

      

      


    

