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




def inputs(item,moneylist,time,topic,io):
  money = 0
  timeinput = 0
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
          money = int(input("money assoatied\n"))#asks for money for the
        except:
          print("Try Again")
        else:
          break
        
      
      while timeinput != 1 or 2 or 3 or 4 or 5:
        timeinput = int(input("time assoated\nPress 1 for weekly\n2 for fortnightly\n3 for monthly\n4 for quarterly\n5 for yearly\n"))#1 2 or 3 4 or 5
        print(timeinput)
        if timeinput == 1:
          time.append("Weekly")
          money = money / 1
          print(money)#testing
          moneylist.append(money)
          break
        elif timeinput == 2:
          time.append("Fortnightly")
          money = money / 2
          print(money)#testing
          moneylist.append(money)
          break
        elif timeinput == 3:
          time.append("Monthly")
          money = money / 4
          print(money)#testing
          moneylist.append(money)
          break
        elif timeinput == 4:
          time.append("Quarterly")
          money = money / 12
          print(money)#testing
          moneylist.append(money)
          break
        elif timeinput == 5:
          time.append("Yearly")
          money = money / 52
          print(money)#testing
          moneylist.append(money)
          break
        else:
          print("Please input either 1,2,3,4 or 5")
      continue




def timesboy(item, amount):
  for i in range(len(item)):
    item[i] = item[i] * amount







def fortables(item,money,time,table):

  for k in range(len(item)):
    table.append([item[k],money[k],time],)
    table.sort(reverse = True, key=lambda x: x[1])
  table.append(["TOTAL",sum(money)])




inputs(i_item,i_money,i_time,"Income","in")
inputs(e_item,e_money,e_time,"Expense","out")
os.system("clear")
while True:

  maintime = int(input("What would you like the timeframe of the table to be\nPress 1 for weekly\n2 for fortnightly\n3 for monthly\n4 for quarterly\n5 for yearly"))


  if maintime == 1:
    maintime = "Weekly"
    timesboy(i_money, 1)
    timesboy(e_money, 1)
    break
    
  elif maintime == 2:
    maintime = ("Fortnightly")
    timesboy(i_money, 2)
    timesboy(e_money, 2)
    break
  elif maintime == 3:
    maintime = ("Monthly")
    timesboy(i_money, 4)
    timesboy(e_money, 4)
    break
  elif maintime == 4:
    maintime = ("Quarterly")
    timesboy(i_money, 12)
    timesboy(e_money, 12)
    break
  elif maintime == 5:
    maintime = ("Yearly")
    timesboy(i_money, 52)
    timesboy(e_money, 52)
    break
  else:
    print("Please input either 1,2,3,4 or 5")

fortables(i_item,i_money,maintime,incometable)
fortables(e_item,e_money,maintime,expensetable)

#sorting the tables(it works so im not touching it NVMVMMVMVMVMV

print('\nINCOME\n')
print(tabulate(incometable, headers=["Item","Money", "Time"]))
print("\nEXPENSES\n")
print(tabulate(expensetable, headers=["Item","Money", "Time"]))
print("\nWHAT'S LEFT\n")
print(tabulate([["total",sum(i_money)-sum(e_money)]],headers=()))