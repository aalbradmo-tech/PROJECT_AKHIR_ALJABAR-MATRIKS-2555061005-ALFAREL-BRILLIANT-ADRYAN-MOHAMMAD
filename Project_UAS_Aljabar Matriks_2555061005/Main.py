import Alfarel005 as n

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[2, 5, 5],
     [0, 6, 1],
     [0, 0, 5]]

D = [[4, 3],
     [2, 1]]

print("\nPenjumlahan Matriks A + B:")
print(n.tambah_matriks(A, B))

print("\nPengurangan Matriks A - B:")
print(n.kurang_matriks(A, B))

print("\nPerkalian Matriks A x B:")
print(n.kali_matriks(A, B))

print("\nTranspose Matriks A:")
print(n.transpose_matriks(A))

print("\nDeterminan Matriks D:")
print(n.determinan_2x2(D))
