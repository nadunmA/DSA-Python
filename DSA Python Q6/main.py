def bubleSort(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]

A = []
for i in range(8):
    num = int (input("Numbers : "))
    A.append(num)


print("Before : ", A)
bubleSort(A)
print("After : ", A)

# BUBBLE_SORT(A)
    #for i=1 to A.length  
        #for j=i+1 to A.length
            #if A[i] > A[j]
                #exchange A[i] with A[j]