A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[2, 5, 5],
     [1, 0, 6],
     [0, 0, 5]]

print("Matriks A:")
print(A)

print("\nMatriks B:")
print(B)

print("\nPenjumlahan Matriks A + B:")
print(tambah_matriks(A, B))

print("\nPengurangan Matriks A - B:")
print(kurang_matriks(A, B))

print("\nPerkalian Matriks A x B:")
print(kali_matriks(A, B))

print("\nTranspose Matriks A:")
print(transpose_matriks(A))
