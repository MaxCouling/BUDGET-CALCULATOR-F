import os
from tabulate import tabulate
i_item = []
i_money = []
i_time =  []
e_item = []
e_time = []#defining all the lists as a list
e_money=[]
incometable= []
expensetable = []
def inputs(item,money,time,topic):
  while True:#while this is running
    os.system("clear")#clears os
    print(topic,"item press enter to exit\n")
    useritem = input()
    if useritem == "":#if the user inputs an enter it breaks the while loop
     break

    else:
      item.append(useritem)#adds the income item to the income item(i_item) list
      money.append (int(input("money assoatied\n")))#asks for money for the
      time.append(input("time assoated\n"))#1 2 or 3
      continue
def fortables(item,money,time,table):

  for k in range(len(item)):
    table.append([item[k],money[k],time[k]],)
  table.append(["TOTAL",sum(money)])

inputs(i_item,i_money,i_time,"Income")
inputs(e_item,e_money,e_time,"Expense")
os.system("clear")
fortables(i_item,i_money,i_time,incometable)
fortables(e_item,e_money,e_time,expensetable)

#sorting the tables(it works so im not touching it)
print(incometable)
print(expensetable)

incometable.sort(reverse = True)

expensetable.sort(reverse = True)
print(incometable)
print(expensetable)
print('\nINCOME\n')
print(tabulate(incometable, headers=["Item","Money", "Time"]))
print("\nEXPENSES\n")
print(tabulate(expensetable, headers=["Item","Money", "Time"]))
print("\nWHAT'S LEFT\n")
print(tabulate([["total",sum(i_money)-sum(e_money)]],headers=()))