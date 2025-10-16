
def T(n):
    if n == 1:
        return 1
    else:
        return T(n-1) + (n-1)
    

def main():
    while True:
        try:
            n = int(input("Enter a number : "))

            if n == -1:
                 break
            
            if n < 1:
                print("enter a number grater than 0 : ")
                continue

        except ValueError:
            print("invalid input")
            continue
        
        print(f"The sum of the first {n} natural numbers is {T(n)}")

if __name__ == "__main__":
    main()  