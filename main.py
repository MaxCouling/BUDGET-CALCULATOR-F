import os
from tabulate import tabulate
i_item = []
i_money = []
i_time =  []
e_item = []
e_time = []#defining all the lists as a list
e_money=[]
while True:#while this is running
  os.system("clear")#clears os
  incomeitem = input("income item press enter to exit\n")
  if incomeitem == "":#if the user inputs an enter it breaks the while loop
    break

  else:
    i_item.append(incomeitem)#adds the income item to the income item(i_item) list
    i_money.append (int(input("money assoatied\n")))#asks for money for the item
    i_time.append(input("time assoated\n"))#1 2 or 3
    continue

while True:
  os.system("clear")
  expenseitem = input("expense item press enter to exit\n")

  if expenseitem == "":
    break

  else:
    
    e_item.append(expenseitem)
    e_money.append(int(input("money assoatied\n")))
    e_time.append(input("time assoated\n"))#1 2 or 3
    continue
os.system("clear")

incometable= []
expensetable = []
for k in range(len(i_item)):
  incometable.append([i_item[k],i_money[k],i_time[k]],)
incometable.append(["TOTAL",sum(i_money)])

#incometable.append("TOTAL",sum(i_money))
for i in range(len(e_item)):
  expensetable.append([e_item[i],e_money[i],e_time[i]],)
expensetable.append(["TOTAL",sum(e_money)])



print(incometable.sort(reverse = True))

print('\nINCOME\n')
print(tabulate(incometable, headers=["Item","Money", "Time"]))
print("\nEXPENSES\n")
print(tabulate(expensetable, headers=["Item","Money", "Time"]))
print("\nWHAT'S LEFT\n")
print(tabulate([["total",sum(i_money)-sum(e_money)]],headers=()))