from .nba_data import teams, allstars 


command = ""



def nba_executer():
    print("Stats for 24/25 NBA season: ")

    print(" *PLEASE NOTE THESE ARE STARTERS ONLY* ")

    print( "Type allstars for the 24/25 allstars") 

    print ("Type 'stop' to exit the program")

    while True:
        command = input("team> ").lower()
        if command == "stop":
            print("Exiting the program.")
            break 
        elif command == "allstars":
            print(allstars)
        elif command in teams:
            print(teams[command])    
        else:
            print("Invalid command. Please try again")   