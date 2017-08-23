def magic_number():
    while(1):
        answer = input("Enter a number in the range 0-10 : ")
        if answer == 1:
            print ("Corect, you won!")
            break
        else:
            print "You lost, Try again"
    
def main():
    magic_number()

if __name__ == "__main__":
    main()            
