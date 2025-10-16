def fibonacci(n):
     if(n <= 1):
          return n
     else:
          return fibonacci(n-1) + fibonacci(n-2)

def main():
    while True:
        try:
            n = int (input("enter non-negative number : "))

            if n == -1:
                 break
            
            if n < 0:
                print("enter non-negative number")
                print()
                continue

        except ValueError:
                print("Invalid")
                continue


        print(f"The fiboncci number is : {fibonacci(n)}")


    print("progran is terminated")

if __name__ == "__main__":
    main()