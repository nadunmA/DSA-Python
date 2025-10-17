def T(num):

    if num == 1:
        return 1
    
    else:
        return T(num-1) + (num)

def main():

    while True:
        try:
            num = int(input("enter number : "))

            if num == -1:
                break
            else:
                result = T(num)
                print("Output:", result) 


        except ValueError:
            print("invalid input")
            continue    


if __name__ == "__main__":
    main()