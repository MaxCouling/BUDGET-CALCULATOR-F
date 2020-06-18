import os#importing os
from tabulate import tabulate#importing table function
import json
import time
i_item = []
i_money = []
i_time =  []
e_item = []
e_time = []#defining all the lists as a list
e_money=[]
incometable= []
expensetable = []
fileworr = False
#Make it easier to use
#ability for one offs
#export and import
#

import json
def write_to_file():
  
  file_name= '{}_budget.txt'.format(user)
  with open(file_name, 'w+') as file:
    data = [incometable, expensetable,total]# writes the income and all that to the file
    file.write(json.dumps(data))
    file.close


#try and exept if file not found raise an error





def timesboy(money, amount):
  #times the money list by the amount chosen in the function
  for i in range(len(money)):
    money[i] = money[i] * amount

def timeframe(comment, is_dividing, money, moneylist):#times or divide
  global maintime
  while True:
    try: 
      timeinput = int(input(comment + "\nPress 1 for weekly\n2 for fortnightly\n3 for monthly\n4 for quarterly\n5 for yearly\n"))#1 2 or 3 4 or 5
    except:
      print("Try again")
    else:
      break
  
  print(timeinput)
  #WEEKLY
  if timeinput == 1:
    if is_dividing:
      money /= 1
      moneylist.append(money)
      return
    else:
      maintime = "Weekly"
      timesboy(i_money, 1)
      timesboy(e_money, 1)
      return
  #WEEKLY    
  elif timeinput == 2:
    
    if is_dividing:
      money /= 2
      moneylist.append(money)
      return
    else:
      maintime = "Fortnightly"
      timesboy(i_money, 2)
      timesboy(e_money, 2)
      return
  #MONTHLY
  elif timeinput == 3:
    if is_dividing:
      money /= 4 
      moneylist.append(money)
      return
    else:#if not dividing we are multipying
      maintime = "Monthly"
      #as there is 4 weeks in a month, we times it by 4 to make it monthly
      timesboy(i_money, 4)
      timesboy(e_money, 4)
      return
  #QUARTERLY
  elif timeinput == 4:
    if is_dividing:
      money /= 12 
      moneylist.append(money)
      return
    else:
      maintime = ("Quarterly")
      #times the money by 12 to make the money quarterly
      timesboy(i_money, 12)
      timesboy(e_money, 12)
      return
  #YEARLY
  elif timeinput == 5:
    if is_dividing:
      money /= 52
      moneylist.append(money)
      return
    else:
      maintime = ("Yearly")
      #gives the functions 52 as that times the weekly by 52 to make a year
      timesboy(i_money, 52)
      timesboy(e_money, 52)
  else:
    print("Please input either 1,2,3,4 or 5")

def fortables(item,money,time,table):

  for k in range(len(item)):
    #adds the item money and the time the table for it to be graphed
    table.append([item[k],money[k],time])
    #sorts the 2nd ([1]), in a array aka money. from highest to lowest
    table.sort(reverse = True, key=lambda x: x[1])
  table.append(["TOTAL",sum(money)])

def inputs(item,moneylist,time,topic,io):
  money = 0
  timeinput = 0
  while True:#while this is running
    os.system("clear")#clears os
    print("Household",topic, "\nMoney coming",io,"\nPress enter with nothing typed in to continue onto the next step\n")
    useritem = input("Name of Item: ")
    if useritem == "":#if the user inputs an enter it breaks the while loop
     break

    else:
      item.append(useritem)#adds the income item to the income item(i_item) list
      
      while True:

        try:
          money = int(input("Money assoatied with "+useritem+" $"))#asks for money for the
        except:
          print("Try Again")
        else:
          timeframe("Please input the timeframe for your money", True, money,moneylist)
          break
        
      continue
def e_or_i_table():
  print('\nINCOME\n')
  print(tabulate(incometable, headers=["Item","Money", "Time"]))
  print("\nEXPENSES\n")
  print(tabulate(expensetable, headers=["Item","Money", "Time"]))
  print("\nWHAT'S LEFT\n")
  print(tabulate([["total",total]],headers=())) 

#TWO BRANCHES FOR BOTH SVAING AND EDITING A FILE OR MAKING A NEW ONE
user = input("What is your name? ")
while True:
    user_read_write = input("Write to file or read from existing file\n").upper()
    print(user_read_write)
    time.sleep(3)
    if user_read_write == "WRITE" and "W":
      file_w_or_r = True
      break
    elif user_read_write == "READ" and "LOAD" and "R":
      file_w_or_r = False
      file_name= '{}_budget.txt'.format(user)
      with open(file_name, 'r') as file:
        data = json.loads(file.read())
        incometable = data[0]#setting the income and expense table as the file
        expensetable = data[1]
        total = data[2]
       
      break
    else:
      os.system("clear")
      print("Please either put in 'WRITE' or 'READ'")
print(file_w_or_r)
time.sleep(3)
if file_w_or_r:#if file is write or read. if it is true it is write, if it is false it is readprint("welcome to maxs loading files and budget calculaor"
  
  inputs(i_item,i_money,i_time,"Income","in")# programming for input.
  inputs(e_item,e_money,e_time,"Expense","out")
  #code for the timeframe
  timeframe("What timeframe do you want your table to be?", False, "error", "error")
#for tables for both income and expenses. Maintime is the time put in from the question
  fortables(i_item,i_money,maintime,incometable)
  fortables(e_item,e_money,maintime,expensetable)
  total = sum(i_money)-sum(e_money)#making the total

  write_to_file()
  #code makes the table that is shown to the user
  e_or_i_table()
elif not file_w_or_r:#if the code is on reading / loading mode
  e_or_i_table()
  time.sleep(3)
  while True:
    editfile = input("Would you like to edit the budget calculator?\n").upper()
    if editfile == "YES" or "Y":
      #edit file
      print("FILE EDITED")
    elif editfile == "NO" or "N":
      #leave file as is and exit program
      print("FILE NOT EDITED")
    else:
      os.system("clear")
      print("Please input either Yes or No")

