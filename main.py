import os
i_item = i_money = i_time = e_item = e_money = e_time = []#defining all the lists as a list
while True:#while this is running
  os.system("clear")#clears os
  incomeitem = input("income item press enter to exit\n")
  if incomeitem == "":
    
    
    break
  else:
    
    
    i_item.append(incomeitem)

   
    i_money.append (int(input("money assoatied\n")))
    i_time.append(input("time assoated\n"))#1 2 or 3
    continue