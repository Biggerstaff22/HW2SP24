from copy import deepcopy

def GaussSeidel(Aaug, x, Niter=15):
    """
    Use the Gauss-Seidel method to estimate the solution to a set of N linear equations.

    Parameters:
    - Aaug: Augmented matrix containing [A | b].
    - x: Vector containing the values of the initial guess.
    - Niter: The number of iterations (new x vectors) to compute.

    Returns:
    - The final new x vector.
    """
    rows, cols = len(Aaug), len(Aaug[0]) - 1

    if not is_diagonal_dominant(Aaug):
        print("Matrix is not diagonal dominant. Adjusting...")
        Aaug = make_diagonally_dominant(Aaug)

    for _ in range(Niter):
        for i in range(rows):
            sum_ax = sum(Aaug[i][j] * x[j] for j in range(cols) if j != i)
            x[i] = (Aaug[i][cols] - sum_ax) / Aaug[i][i]

    return x

def MakeDiagDom(A):
    """
    This function reorders the rows of matrix A to put the largest absolute values along the diagonal.

    :param A: The matrix to sort
    :return: The sorted matrix
    """
    # Create a list of tuples containing row index and maximum absolute value in each row
    max_values = [(i, max(map(abs, row))) for i, row in enumerate(A)]

    # Sort the list of tuples based on the maximum absolute value
    max_values.sort(key=lambda x: x[1], reverse=True)

    # Create a new matrix with rows rearranged based on the sorted indices
    sorted_A = [A[i] for i, _ in max_values]

    return sorted_A

def main():
    # Test case
    Aaug = [[3, 1, -1, 2],
            [1, 4, 1, 12],
            [2, 1, 2, 10]]

    initial_guess = [0, 0, 0]

    print("Original Matrix:")
    for row in Aaug:
        print(row)

    print("\nDiagonally Dominant Matrix:")
    Aaug = MakeDiagDom(Aaug)
    for row in Aaug:
        print(row)

    solution = GaussSeidel(Aaug, initial_guess, Niter=15)

    print(f"\nEstimated Solution: {solution}")

if __name__ == "__main__":
    main()
