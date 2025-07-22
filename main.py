print("******************************************")
print("*   Welcome to Number Range Printer ❤️    *")
print("*       Made with 🇳🇵 by Aayush Singh     *")
print("******************************************\n")


f1=int(input("Enter starting number : "))
f2=int(input("Enter ending number   : "))
f3=int(input("Enter the step value (gap between numbers): "))

if (f3 <= 0):
	print("Step must be a positive number!")
elif (f2 <= 0):
	print("Ending number must be greater than 0")
	
else:
		for num in range(f1,f2+1,f3):
			print(num)
		
print(f"\nPRINTED NUMBERS FROM {f1} TO {f2} ")
	
