a = int(input("Enter age: "))
g = input("Enter gender (m/f): ") 

if g == "m":
    if a > 20:
        print("Pay tax or you will be in jail.")
    else:
        print("We will wait until 20.")
elif g == "f":
    if 18 < a < 35:
        print("You will pay tax.")
    else:
        print("Sorry, we will wait.")
else:
    print("Wrong input.")
