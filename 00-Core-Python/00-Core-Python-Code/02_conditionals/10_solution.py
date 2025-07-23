species = input("Enter your pet (Dog/Cat): ")
age = int(input("Enter the age of your pet (in years): "))

if species == "Dog":
    if age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")

elif species == "Cat":
    if age > 5:
        print("Senior cat food")
    else:
        print("Regular cat food")

else:
    print("Unknown pet! Please enter Dog or Cat.")
