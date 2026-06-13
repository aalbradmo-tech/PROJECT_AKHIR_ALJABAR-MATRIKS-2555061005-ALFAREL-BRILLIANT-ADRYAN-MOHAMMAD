
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[2, 5, 5],
     [0, 6, 1],
     [0, 0, 5]]

D = [[4, 3],
     [2, 1]]

print("\nPenjumlahan Matriks A + B:")
print(tambah_matriks(A, B))

print("\nPengurangan Matriks A - B:")
print(kurang_matriks(A, B))

print("\nPerkalian Matriks A x B:")
print(kali_matriks(A, B))

print("\nTranspose Matriks A:")
print(transpose_matriks(A))

print("\nDeterminan Matriks D:")
print(determinan_2x2(D))
