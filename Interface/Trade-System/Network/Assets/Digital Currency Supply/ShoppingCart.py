


#Shopping Cart Program / Tranfer System

#Shop / Digital Pricings / Settings = Long Logs / Interface First = Protection Center

	account = []
	
	amount = []
	
	total = 0
     
    
        while True:
            account = input("Enter Tranfer Amount (q to quit): ")
            if account.lower() == "q" :
                break
                
            else:
                amount = float(input("Enter the price of a {account}: #"))
                accounts.append(account)
                amounts.append(amount)
                
                
                
    print("---- YOUR CART ----")
    
    
    for account in accounts:
        print(account)
        
    for amount in amounts
        total += amount
    
    print()
    print("Your total is: #{total}")
    
    