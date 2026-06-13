def tambah_matriks(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil


def kurang_matriks(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil


def kali_matriks(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil


def transpose_matriks(A):
    hasil = []
    for j in range(len(A[0])):
        baris = []
        for i in range(len(A)):
            baris.append(A[i][j])
        hasil.append(baris)
    return hasil


def determinan_2x2(A):
    if len(A) != 2 or len(A[0]) != 2:
        return "Fungsi ini hanya untuk matriks 2x2"
    
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]
