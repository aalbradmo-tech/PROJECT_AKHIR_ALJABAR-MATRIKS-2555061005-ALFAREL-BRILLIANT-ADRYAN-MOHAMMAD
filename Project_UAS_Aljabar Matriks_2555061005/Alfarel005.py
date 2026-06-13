def tambah_matriks(m1, m2):
    hasil = []
    for i in range(len(m1)):
        baris = []
        for j in range(len(m1[0])):
            baris.append(m1[i][j] + m2[i][j])
        hasil.append(baris)
    return hasil


def kurang_matriks(m1, m2):
    hasil = []
    for i in range(len(m1)):
        baris = []
        for j in range(len(m1[0])):
            baris.append(m1[i][j] - m2[i][j])
        hasil.append(baris)
    return hasil


def kali_matriks(m1, m2):
    hasil = []
    for i in range(len(m1)):
        baris = []
        for j in range(len(m2[0])):
            jumlah = 0
            for k in range(len(m2)):
                jumlah += m1[i][k] * m2[k][j]
            baris.append(jumlah)
        hasil.append(baris)
    return hasil


def transpose_matriks(m):
    hasil = []
    for j in range(len(m[0])):
        baris = []
        for i in range(len(m)):
            baris.append(m[i][j])
        hasil.append(baris)
    return hasil


def determinan_2x2(m):
    if len(m) != 2 or len(m[0]) != 2:
        return None
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]
