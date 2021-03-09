print("Your Birthday")

birthdate = str( input("Please enter your birthday in DD-MM-YYYY format: ") )

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

index = int( birthdate[3:5] )-1
bulan_bd = months[index]

print("You were born in", bulan_bd)

