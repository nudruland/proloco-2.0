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
NOT_PLACED = 7

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

listaTavoli = [[], [], [], [], [], [], [], []]

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
len_MAX = len(MAX)

for i in range(len_MAX) :
  MIN_FIRST_ROUND[i] = MAX[i] - OFFSET_FIRST
  MIN_SECOND_ROUND[i] = MAX[i] - OFFSET_SECOND

for instance in sorted_list :
  i = 0
  inserted = False 
  while (i < len_MAX and inserted == False) :
    if(int(MAX[i]) >= int(instance.number) >= int(MIN_FIRST_ROUND[i])) :
       inserted = True
       listaTavoli[i].append(instance)
    else :
        i += 1
  if inserted == False :
        listaTavoli[NOT_PLACED].append(instance)

counter_top = 0
counter_down = 0

for counter_top in range(len(listaTavoli[NOT_PLACED])) : 
  placed = False
  for counter_down in range(len(listaTavoli[NOT_PLACED]) - 1, -1, -1) : 
    sum = int(listaTavoli[NOT_PLACED][counter_top].number) + int(listaTavoli[NOT_PLACED][counter_down].number)
    for i in range(len_MAX) : 
      if( MAX[i] >= sum >= MIN_SECOND_ROUND[i]) : 
        new_prenotazione = Prenotazione(str(listaTavoli[NOT_PLACED][counter_top].name) + " + " + str(listaTavoli[NOT_PLACED][counter_down].name), int(listaTavoli[NOT_PLACED][counter_top].number) + int(listaTavoli[NOT_PLACED][counter_down].number), str(listaTavoli[NOT_PLACED][counter_top].comment) + " + " + str(listaTavoli[NOT_PLACED][counter_down].comment))
        listaTavoli[i].append(new_prenotazione)
        listaTavoli[NOT_PLACED][counter_down].number = 100
        listaTavoli[NOT_PLACED][counter_top].number = 100
        placed = True
        break
    
    if (placed == True) :
       break
    
filtered_list = [inst for inst in listaTavoli[NOT_PLACED] if inst.number != 100]
listaTavoli[NOT_PLACED] = filtered_list

for i in range(len(listaTavoli)) : 
   print("TAVOLI CON " + str(int(i + 1)))
   for k in range(len(listaTavoli[i])) :
      print(listaTavoli[i][k].name, listaTavoli[i][k].number)
      

















          

          
          
        

      

      


    

