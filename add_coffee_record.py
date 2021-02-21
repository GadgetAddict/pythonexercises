#Michael King
#This program adds coffee inventory to a text file.


def main():
    another = "y"
    try:
        
    #Open coffee file in Append Mode
        coffee_file = open('coffee.txt', 'a')
        while another == 'y' or another =="Y":
        	#get coffee record Data
        	print("Enter the following Coffee Details:")
        	descr = input("Coffee Name\n")
        	qty = int(input("Quantity in pounds: \n"))
        	
        	#Append the data to the file
        	coffee_file.write(descr + "\n")
        	coffee_file.write(str(qty) + "\n")
        	
        	#Determine if there's more coffee to input
        	print("Do you want to enter another record?")
        	another = input("Type y For Yes or Any other key for No\n")
        	another = another.lower()
        	
		#Finally block closes the file
			
    except IOError:
        print("AN Error Occurred")
         

    finally:
        if not coffee_file.closed:
            coffee_file.close()
            print("Closed or Not    : ",coffee_file.closed)
main()
        
