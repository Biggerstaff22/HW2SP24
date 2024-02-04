from copy import deepcopy

#I used ChatGPT to help me write this code. This was a hard code to figure out how to explain,
#to ChatGPT. I asked ChatGPT to explain the steps to me.

def GaussSeidel(Aaug, x, Niter=15):
    """
    Implements the Gauss-Seidel method for solving a system of equations.
    :param Aaug: Augmented Matrix from Ax=b to [A|b]
    :param x: Initial guess for the x vector. x is nx1 if A is nxn.
    :param Niter:Number of iterations needed to run the Gauss-Seidel method.
    :return:
    """
    n = len(x)

    for k in range(Niter):
        x_old = deepcopy(x)

        for i in range(n):
            sigma = sum(Aaug[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (Aaug[i][-1] - sigma) / Aaug[i][i]

        return x
def MakeDiagDominant(Aaug):
    """
    This is used to swap rows to make matrix diagonally dominant
    :param Aaug: Matrix that is being modified
    :return:
    """
    n = len(Aaug)

    for i in range(n):
        max_row = max(range(i, n), key=lambda j: abs(Aaug[j][i]))
        Aaug[i], Aaug[max_row] = Aaug[max_row], Aaug[i]

    return Aaug

def main():
    """
    :return: This is the main function that will perform all the math to execute the code and get the answer.
    """
    #this is for the 4x4 matrix A:
    A = [[1, -10, 2, 4],
         [3, 1, 4, 12],
         [9, 2, 3, 4],
         [-1, 2, 7, 3]]
    #now for the 1x4 matrix b:
    b = [2, 12, 21, 37]
    #now for the 3x3 matrix C:
    C = [[3, 1, -1],
         [1, 4, 1],
         [2, 1, 2]]
    #now for the 1x3 matrix d:
    d = [2, 12, 10]
    #This creates the augmented matrices
    Aaug = [row + [bi] for row, bi in zip(A, b)]
    Caug = [row + [dj] for row, dj in zip(C, d)]
    #this creates the initial guess for the matrix
    x_initial_guessA = [0.0] * len(b)
    x_initial_guessC = [0.0] * len(d)
    #makes the matrix diagonally dominant
    Aaug = MakeDiagDominant(Aaug)
    Caug = MakeDiagDominant(Caug)
    #now to solve using Gauss-Seidel
    answer = GaussSeidel(Aaug, x_initial_guessA)
    answer2 = GaussSeidel(Caug, x_initial_guessC)
    #Printing the output so that we can see the answer
    for i in range(len(answer2)):
        answer2[i] = round(answer2[i])
    for j in range(len(answer)):
        answer[j] = round(answer[j])

    print("Solution to 3x3 matrix is: ", answer2)
    print("Solution to 4x4 matrix is: ", answer)

if __name__ == "__main__":
    main()