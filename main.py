import os#importing os
from tabulate import tabulate#importing table function
i_item = []
i_money = []
i_time =  []
e_item = []
e_time = []#defining all the lists as a list
e_money=[]
incometable= []
expensetable = []

def inputs(item,money,time,topic,io):
  while True:#while this is running
    os.system("clear")#clears os
    print("Household",topic, "\nMoney coming",io,"\nPress enter with nothing typed in to continue onto the next step\n")
    useritem = input()
    if useritem == "":#if the user inputs an enter it breaks the while loop
     break

    else:
      item.append(useritem)#adds the income item to the income item(i_item) list
      
      while True:

        try:
          money.append (int(input("money assoatied\n")))#asks for money for the
        except:
          print("Try Again")
        else:
          break
        
      time.append(input("time assoated\nPress 1 for weekly,2 for fortnightly,3 for monthly,4 for quarterly and 5 for yearly"))#1 2 or 3

      continue

def fortables(item,money,time,table):

  for k in range(len(item)):
    table.append([item[k],money[k],time[k]],)
  table.append(["TOTAL",sum(money)])




inputs(i_item,i_money,i_time,"Income","in")
inputs(e_item,e_money,e_time,"Expense","out")
os.system("clear")
fortables(i_item,i_money,i_time,incometable)
fortables(e_item,e_money,e_time,expensetable)
print(incometable)
print(expensetable)
#sorting the tables(it works so im not touching it NVMVMMVMVMVMV

print('\nINCOME\n')
print(tabulate(incometable, headers=["Item","Money", "Time"]))
print("\nEXPENSES\n")
print(tabulate(expensetable, headers=["Item","Money", "Time"]))
print("\nWHAT'S LEFT\n")
print(tabulate([["total",sum(i_money)-sum(e_money)]],headers=()))