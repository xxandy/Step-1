import numpy, time
import matplotlib.pyplot as plt

#ALEXNOTE: you'll want to comment on whether A,B,C are passed by reference ore by value.
#          -> and in this case, reference is definetely better, and that's python's default
#            see https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
def multiple(A,B,C):
    n = len(A)
    if len(A) != n or len(B) != n: return 'Input Error'
    for x in A + B:
        if len(x) != n: return 'Input Error'

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    # ALEXNOTE: return the same parameter you modified is rather unusual.
    #           it leads to one of two consequences: 
    #               -> if C is passed by refererence:  the return operation causes unnecessary copying
    #                  (possibly destroy a temp array just to create a new one with the same value), so
    #                   better not to return it.
    #               -> if C is passed by value:  unnecessary copying both in and out.
    return C

# x and y are for the picture.
x = []
y = []

for n in range(70):

    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    c = multiple(a,b,c)

    end = time.time()
    print(n, "time: %.6f sec" % (end - begin))

    # Print C for debugging. Comment out the print before measuring the execution time.
    total = 0
    for i in range(n):
        for j in range(n):
            # print c[i, j]
            total += c[i, j]
    # Print out the sum of all values in C.
    # This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
    print("sum: %.6f" % total)
    
    # for pircture.
    x.append(n)
    y.append(end - begin)


plt.scatter(x, y, label='matrix multiplication')
plt.legend()
plt.show()
