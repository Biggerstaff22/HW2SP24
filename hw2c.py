import copy

def is_diagonal_dominant(matrix):
    """
    Check if a matrix is diagonal dominant.

    Parameters:
    - matrix: A 2D square matrix.

    Returns:
    - True if the matrix is diagonal dominant, False otherwise.
    """
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        diagonal_element = abs(matrix[i][i])
        sum_of_other_elements = sum(abs(matrix[i][j]) for j in range(cols) if j != i)

        if diagonal_element <= sum_of_other_elements:
            return False

    return True

def make_diagonally_dominant(matrix):
    """
    Make a matrix diagonally dominant.

    Parameters:
    - matrix: A 2D square matrix.

    Returns:
    - Diagonally dominant matrix.
    """
    A = copy.deepcopy(matrix)
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        diagonal_element = abs(matrix[i][i])
        sum_of_other_elements = sum(abs(matrix[i][j]) for j in range(cols) if j != i)

        if diagonal_element <= sum_of_other_elements:
            # Adjust diagonal element to make it larger than the sum of other elements
            matrix[i][i] = sum_of_other_elements + 1

    return matrix

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
    Aaug = make_diagonally_dominant(Aaug)
    for row in Aaug:
        print(row)

    solution1 = GaussSeidel(Aaug, initial_guess, Niter=15)

    print(f"\nEstimated Solution: {solution1}")

def main2():
    # Test case
    Aaug2 = [[1, -10, 2, 4, 2],
            [3, 1, 4, 12, 12],
            [9, 2, 3, 4, 21],
            [-1, 2, 7, 3, 37]]

    initial_guess2 = [0, 0, 0, 0]

    print("Original Matrix:")
    for row in Aaug2:
        print(row)

    print("\nDiagonally Dominant Matrix:")
    Aaug2 = make_diagonally_dominant(Aaug2)
    for row in Aaug2:
        print(row)

    solution2 = GaussSeidel(Aaug2, initial_guess2, Niter=15)

    print(f"\nEstimated Solution: {solution2}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main2()
