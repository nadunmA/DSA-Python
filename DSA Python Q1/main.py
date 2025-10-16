def multiply(m, n):
     if n == 1:
         return m
     else:
         return m + multiply(m, n-1)


def main():
    while True:

        try:
            m = int (input("enter 1st integer (enter -1 to exit) : "))
            if m == -1:
                break
        except ValueError:
            print("Invalid")
            continue
        
        try:
            n = int (input("enter 2nd integer (enter -1 to exit) : "))
            if n == -1:
                break  
        except ValueError:
            print("Invalid")
            continue

        x = multiply(m, n)
        print(f"The output of {m} x {n} is {x}")

    print ("program terminate")    

if __name__ == "__main__":
    main()