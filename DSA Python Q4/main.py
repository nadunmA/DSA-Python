def insersionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1

        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1

        A[i + 1] = key


def findRange(A):
    range = A[-1] - A[0]
    return range


def findMedian(A):

    if(len(A) % 2 == 0):

        medain = (A[len(A) //2] + A[(len(A) //2) - 1]) / 2 

    else:
        medain = A[len(A) //2]

    return medain    

A = []

for i in range(9):

    num = int (input("Mark : "))
    A.append(num)


print("Before Sorting", A)
insersionSort(A)
print("After Sorting", A)

print("Range is : ", findRange(A))
print("Median is : ", findMedian(A))
