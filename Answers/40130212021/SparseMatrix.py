class SparseMatrix:
    def init(self, matrix):
        self.sm = self.to_sparse(matrix)

    def to_sparse(self, matrix):
        sp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    sp.append((i, j, matrix[i][j]))
        return sp

    def transpose(self):
        tr = [(c, r, v) for r, c, v in self.sm]
        tr.sort()
        return tr

    def change_elem(self, row, col, new_val):
        for i in range(len(self.sm)):
            if self.sm[i][0] == row and self.sm[i][1] == col:
                self.sm[i] = (row, col, new_val)
                return

    def display(self):
        for r, c, v in self.sm:
            print(f"({r}, {c}): {v}")


nm = [
    [1, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 3, 0, 0],
    [0, 0, 0, 4]
]

sm = SparseMatrix(nm)

sm.display()


tr_matrix = SparseMatrix(sm.transpose())
tr_matrix.display()

sm.change_elem(1, 2, 5)

sm.display()