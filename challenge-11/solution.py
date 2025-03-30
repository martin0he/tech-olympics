def filter_transactions(transactions):
  filtered_list = []
  for tran in transactions:
    if tran["TransactionAmount"] > 100.0:
      filtered_list.append(tran)
      
  return filtered_list

def find_unique_customers(transactions):
  unique_customers = []
  for t in transactions:
    if t["Name"] not in unique_customers:
      unique_customers.append(t["Name"])
      
  return unique_customers


def unique_customers_spend_over_100(t):
  filtered = filter_transactions(t)
  un = find_unique_customers(filtered)
  return len(un)

def total_money(t):
  filtered = filter_transactions(t)
  unique = find_unique_customers(filtered)
  names = []
  for u in unique:
    names.append(u["Name"])
    
  
  counter = 0
  
  for tr in t:
    if tr["Name"] in names:
      counter += tr["TransactionAmount"]
      
  return counter

transactions = [{"Name":"Erika", "CustomerID": "C001", "TransactionAmount":120.00},
                         {"Name":"Amelia", "CustomerID": "C002", "TransactionAmount":75.00}, 
                         {"Name":"Jules", "CustomerID": "C003", "TransactionAmount":180.50}, 
                         {"Name":"Erika", "CustomerID": "C001", "TransactionAmount":90.00}, 
                         {"Name":"Quinn", "CustomerID": "C004", "TransactionAmount":55.00},
                         {"Name":"Amelia", "CustomerID": "C005", "TransactionAmount":50.00},
                         {"Name":"Frani", "CustomerID": "C003", "TransactionAmount":200.00}, 
                         {"Name":"Jules", "CustomerID": "C003", "TransactionAmount":50.00}, 
                         {"Name":"Henry", "CustomerID": "C006", "TransactionAmount":250.00}, 
                         {"Name":"Cookies", "CustomerID": "C007", "TransactionAmount":300.00},
                         {"Name":"Erika", "CustomerID": "C001", "TransactionAmount":110.00},
                         {"Name":"Jules", "CustomerID": "C003", "TransactionAmount":220.00}, 
                         {"Name":"Frani", "CustomerID": "C005", "TransactionAmount":125.00}, 
                         {"Name":"Quinn", "CustomerID": "C004", "TransactionAmount":95.00}, 
                         {"Name":"Amelia", "CustomerID": "C002", "TransactionAmount":250.00},
                         {"Name":"Easha", "CustomerID": "C015", "TransactionAmount":55.00},
                         {"Name":"Ayla", "CustomerID": "C009", "TransactionAmount":90.00}, 
                         {"Name":"Will", "CustomerID": "C017", "TransactionAmount":30.00}, 
                         {"Name":"Lorelei", "CustomerID": "C018", "TransactionAmount":25.00}, 
                         {"Name":"Kevin", "CustomerID": "C019", "TransactionAmount":75.00},
                         {"Name":"Owen", "CustomerID": "C020", "TransactionAmount":50.00}, 
                         {"Name":"Liz", "CustomerID": "C021", "TransactionAmount":80.00}]
    
ans1 = unique_customers_spend_over_100(transactions)
ans2 = total_money(transactions)
    
print(f"Unique Customers: {ans1}" )
print(f"Total Money Spent: {ans2}")
    
    
  
  
    
    
    
    
                         


   

                         

                         
                         
