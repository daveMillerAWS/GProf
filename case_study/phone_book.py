"""
GROUP PROFESSORS CASESTUDY_2

About: Bash scripting and python coding

Author: Miller, Dave

"""
import getpass
user = getpass.getuser().upper()

phonebook = {"Matt":{"Name":"Matt", "Surname":"Demon", "Number":5234255423},
          "Dave":{ "Name":"Dave", "Surname":"Miller", "Number":5234255423},
          "Tim":{"Name":"Tim", "Surname":"Hinnes", "Number":52123255423}
         }


# FUNCTIONS for operations

def addToBook():
    
    temp = {"Name": input("Enter name: "), "Surname": input("Enter Surname: "), "Number":input("Enter number: ")}
    print([*temp.values()])
    if (input("Are you sure to add to phone book [y/n]") == 'y'):
        phonebook[temp["Name"]] = temp
        print([*phonebook.values()])
        temp.clear()
    else: 
        print("No entry to phone book")
        
    # print(*temp.values())
    # print( [k for k in temp.values()])

def delfromBook():
    print('whom are you going to delete from book',[*phonebook.keys()])
    del phonebook[input("Enter name to delete: ")]
    print("process ended successfully")


def updateBook():
    print('whom are you going to update info',[*phonebook.keys()])
    name  = input("Enter the name: ")
    phonebook[name] = {"Name": name, "Surname": input("surname: "), "Number": int(input("enter number: "))}


def main():

    while True:
        print()
        print(">>>>>>>>>>>>> Good to See you", user," <<<<<<<<<<<<<")
        print()
        print("##########       Welcome DAVE Phone Book (Casestudy_2)       ###########")
        print()
        
        print("List operation               -----> Press 1")
        print("New Entry operation          -----> Press 2")
        print("Delete operation             -----> Press 3")
        print("Update operation             -----> Press 4")
        print("Exit operation               -----> Press any button") 
        print()
        option = input("What is your intention:")
        print()

        if (option == "1"):
                print([*phonebook.values()])
        elif (option == "2"):
            addToBook()
        elif (option == "3"):
            delfromBook()
        elif (option == "4"):
            updateBook()
        else:
            print("See you then")
            break

if __name__ == "__main__":
    main()
