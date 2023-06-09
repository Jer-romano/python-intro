def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    tl_to_br_total = 0
    bl_to_tr_total = 0

    for i in range(len(matrix)):
        tl_to_br_total += matrix[i][i]

    for j in range(len(matrix)):
        bl_to_tr_total += matrix[-(j+1)][j]

    #print("Here: " + str(tl_to_br_total))
   # print("Here: " + str(bl_to_tr_total))
    return tl_to_br_total + bl_to_tr_total