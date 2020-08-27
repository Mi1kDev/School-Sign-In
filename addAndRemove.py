import persistenceModule as persist

def option(choice):
    case = {
        "A": persist.addToFile,
        "R": persist.removeFromFile
    }
    func = case.get(choice, lambda: "Invalid")
    return func("Student-ID.json")

choice = input("Enter 'A' to add and Enter 'R' to remove\n")
option(choice)




