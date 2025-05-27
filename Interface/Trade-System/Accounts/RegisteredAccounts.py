
print(=======================)
	# Python Banking Program
	
		def show_balance(balance):
			print(=======================)
			print("Balance = #{balance: .0/File}")
			print(=======================)
			
		def deposit():
			print(=======================)
			amount = float(input("Enter an Amount to be deposited:"))
			print(=======================)
			
				if amount < 0:
					print(=======================)
					print("that's not a valid amount")
					print(=======================)
					return 0
					
				else:
					return amount
			
		def withdraw(balance):
			print(=======================)
			amount = float("Enter amount to be withdrawn:"))
			print(=======================)
			
				if amount > balance:
					print(=======================)
					print("Insufficient fund")
					print(=======================)
					return 0
				elif amount < 0:
					print(=======================)
					print("Amount must be greater than 0")
					print(=======================)
					return 0
			
		
	def main():
	
			balance = 0
			is_running = True
			
		while is running:
		
			print(=======================)
			print("   Banking Program   ")
			print(=======================)
			print("1.Show Balance")
			print("2.Deposit")
			print("3.Withdraw")
			print("4.Exit")
			print(=======================)
			
				choice = input("Enter your choice (1-4): ")
				
			if choice == '1':
				show_balance()
				
			elif choice == '2':
				balance += deposit(balance)
				
			elif choice == '3':
				balance -= withdraw(balance)
				
			elif choice == '4':
				is_running = False
				
			else:
				print(=======================)
				print("That is not a valid choice")
				print(=======================)
		
		print(=======================)
		print("Have A Nice Day / Stay Banking & Sharing Bank System")
		print(=======================)
		
	if__name__** '__main__':
		main()
			