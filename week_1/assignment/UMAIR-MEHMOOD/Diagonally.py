
space = 0
#function to print diagonally
def to_diagonally(name):
    global space
    for letter in name:
        print(f"{' '*space} {letter}")
        space+=1
    else: space = 0

#main function 
def main():
    #Diagonal name printi
    name = "UMAIR MEHMOOD"

    print(f"Name is : {name}")
    print("Diagonally it become :")
    to_diagonally(name)

    #diagonal name print in reverse

    print(f"\n\nName is : {name}")
    print("Reverse Diagonally it become :")
    to_diagonally(name[::-1])

if __name__== "__main__":
    main()