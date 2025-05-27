


#Shopping Cart Program / Tranfer System 

#Shop / Digital Pricings / Settings = Long Logs / Interface First = Protection Center

	account = []
	
	saving = []
	
		# Python compound interest calculator
			
			
				principle = 0
				
				rate = 0.02
				
				time = 1
				
				
					while principle <=0
						principle = float(input("Enter the principle amount:"))
						
							if principle <=0:
								print("principle can't be less than or equal to zero")
								
							print(principle)
							
							else:
								break
							
					
					while rate <=0
						rate = float(input("Enter the interest rate:"))
						
							if rate <=0:
								print("Interest rate can't be less than or equal to zero")
								
							print(principle)
							
							else:
								break
							
							
					while time <=0
						time = int(input("Enter the time in years:"))
						
							if time <=0:
								print("time can't be less than or equal to zero")
								
							print(principle)
								
							else:
								break
							
							
					print(principle)
					
					print(rate)
					
					print(time)
					
					total = principle * pow(1 + rate / 100), time)
					
						print("balance after {time} year/s : #{total:}")
	
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
        
    print("Your total is: #{total}")
    
    
