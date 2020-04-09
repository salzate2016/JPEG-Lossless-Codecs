from copy import deepcopy
from tabulate import tabulate

image = [[88, 88, 88, 89, 90, 91, 92, 93, 94, 95, 93, 95, 96, 98, 97, 94],
         [93, 91, 91, 90, 92, 93, 94, 94, 95, 95, 92, 93, 95, 95, 95, 96],
         [95, 95, 95, 95, 96, 97, 94, 96, 97, 96, 98, 97, 98, 99, 95, 97],
         [97, 96, 98, 97, 98, 94, 95, 97, 99, 100, 99, 101, 100, 100, 98, 98],
         [99, 100, 97, 99, 100, 100, 98, 98, 100, 101, 100, 99, 101, 102, 99, 100],
         [100, 101, 100, 99, 101, 102, 99, 100, 103, 102, 103, 101, 101, 100, 102, 101],
         [100, 102, 103, 101, 101, 100, 102, 103, 103, 105, 104, 104, 103, 104, 104, 103],
         [103, 105, 103, 105, 105, 104, 104, 104, 102, 101, 100, 100, 100, 101, 102, 103],
         [104, 104, 105, 105, 105, 104, 104, 106, 102, 103, 101, 101, 102, 101, 102, 102],
         [102, 105, 105, 105, 106, 104, 106, 104, 103, 101, 100, 100, 101, 102, 102, 103],
         [102, 105, 105, 105, 106, 104, 106, 104, 103, 101, 100, 100, 101, 102, 102, 103],
         [102, 105, 105, 105, 106, 104, 105, 104, 103, 101, 102, 100, 102, 102, 102, 103],
         [104, 105, 106, 105, 106, 104, 106, 103, 103, 102, 100, 100, 101, 102, 102, 103],
         [103, 105, 107, 107, 106, 104, 106, 104, 103, 101, 100, 100, 101, 102, 102, 103],
         [103, 105, 106, 108, 106, 104, 106, 105, 103, 101, 101, 100, 101, 103, 102, 105],
         [102, 105, 105, 105, 106, 104, 106, 107, 104, 103, 102, 100, 101, 104, 102, 104]]

huffmanTable = {0: '1',
                1: '00',
                -1: '011',
                2: '0100',
                -2: '01011',
                3: '010100',
                -3: '0101011',
                4: '01010100',
                -4: '010101011',
                5: '0101010100',
                -5: '01010101011',
                6: '010101010100',
                -6: '0101010101011'}

"""
---------
| C | B |
---------
| A | X |
---------
"""


def formulas_Encode(i, j):
    """
    calculates DX using the seven prediction formulas
    :param i: row
    :param j: column
    :return: values of DX of each prediction formula
    """
    if i == 0 and j == 0:
        a = image[i][j]
        b = image[i][j]
        c = image[i][j]
        d = image[i][j]
        e = image[i][j]
        f = image[i][j]
        g = image[i][j]
    elif j == 0:
        a = image[i][j] - image[i - 1][j]
        b = image[i][j] - image[i - 1][j]
        c = image[i][j] - image[i - 1][j]
        d = image[i][j] - image[i - 1][j]
        e = image[i][j] - image[i - 1][j]
        f = image[i][j] - image[i - 1][j]
        g = image[i][j] - image[i - 1][j]
    elif i == 0:
        a = image[i][j] - image[i][j - 1]
        b = image[i][j] - image[i][j - 1]
        c = image[i][j] - image[i][j - 1]
        d = image[i][j] - image[i][j - 1]
        e = image[i][j] - image[i][j - 1]
        f = image[i][j] - image[i][j - 1]
        g = image[i][j] - image[i][j - 1]
    else:
        a = image[i][j] - image[i][j - 1]
        b = image[i][j] - image[i - 1][j]
        c = image[i][j] - image[i - 1][j - 1]
        d = image[i][j] - (image[i][j - 1] + image[i - 1][j] - image[i - 1][j - 1])
        e = image[i][j] - (image[i][j - 1] + (image[i - 1][j] - image[i - 1][j - 1]) // 2)
        f = image[i][j] - (image[i - 1][j] + (image[i][j - 1] - image[i - 1][j - 1]) // 2)
        g = image[i][j] - ((image[i][j - 1] + image[i - 1][j]) // 2)
    return a, b, c, d, e, f, g


def formulas_Decode(decom1, decom2, decom3, decom4, decom5, decom6, decom7, i, j):
    """
    Calculates X using the seven prediction formulas
    :param decom1: DX using formula 1
    :param decom2: DX using formula 2
    :param decom3: DX using formula 3
    :param decom4: DX using formula 4
    :param decom5: DX using formula 5
    :param decom6: DX using formula 6
    :param decom7: DX using formula 7
    :param i: Row
    :param j: Column
    :return: values of x after decompression(Original values)
    """
    if i == 0 and j == 0:
        a = image[0][0]
        b = image[0][0]
        c = image[0][0]
        d = image[0][0]
        e = image[0][0]
        f = image[0][0]
        g = image[0][0]
    elif j == 0:
        a = decom1[i][j] + decom1[i - 1][j]
        b = decom2[i][j] + decom2[i - 1][j]
        c = decom3[i][j] + decom3[i - 1][j]
        d = decom4[i][j] + decom4[i - 1][j]
        e = decom5[i][j] + decom5[i - 1][j]
        f = decom6[i][j] + decom6[i - 1][j]
        g = decom7[i][j] + decom7[i - 1][j]
    elif i == 0:
        a = decom1[i][j] + decom1[i][j - 1]
        b = decom2[i][j] + decom2[i][j - 1]
        c = decom3[i][j] + decom3[i][j - 1]
        d = decom4[i][j] + decom4[i][j - 1]
        e = decom5[i][j] + decom5[i][j - 1]
        f = decom6[i][j] + decom6[i][j - 1]
        g = decom7[i][j] + decom7[i][j - 1]
    else:
        a = decom1[i][j] + decom1[i][j - 1]
        b = decom2[i][j] + decom2[i - 1][j]
        c = decom3[i][j] + decom3[i - 1][j - 1]
        d = decom4[i][j] + (decom4[i][j - 1] + decom4[i - 1][j] - decom4[i - 1][j - 1])
        e = decom5[i][j] + (decom5[i][j - 1] + (decom5[i - 1][j] - decom5[i - 1][j - 1]) // 2)
        f = decom6[i][j] + (decom6[i - 1][j] + (decom6[i][j - 1] - decom6[i - 1][j - 1]) // 2)
        g = decom7[i][j] + ((decom7[i][j - 1] + decom7[i - 1][j]) // 2)
    return a, b, c, d, e, f, g


def huffmanConvertion(a, i, j):
    """
    Converts a coefficient to its corresponding binary code
    :param a: coefficient
    :param i: row
    :param j: column
    :return: binary code
    """
    if i == 0 and j == 0:
        b = bin(a)[2:]
    else:
        b = huffmanTable[a]
    return b


def huffmanDecoder(a, i, j):
    """
    converts a binary code to its correspondig DX
    :param a: binary code
    :param i: Row
    :param j: Column
    :return: DX
    """
    # list out keys and values separately
    key_list = list(huffmanTable.keys())
    val_list = list(huffmanTable.values())
    if i == 0 and j == 0:
        b = int(a, 2)
    else:
        b = key_list[val_list.index(a)]
    return b


def encoder():
    """
    calculates the coefficients and compressed image in the form of binary sequence
    :return: 7 matrices of coefficients and 7 compressed images(matrices) in the form of binary sequence
    """
    row = 16
    col = 16
    en1, en2, en3, en4, en5, en6, en7 = [], [], [], [], [], [], []
    enBin1, enBin2, enBin3, enBin4, enBin5, enBin6, enBin7 = [], [], [], [], [], [], []
    for i in range(col):
        ar1, ar2, ar3, ar4, ar5, ar6, ar7 = [], [], [], [], [], [], []
        arBin1, arBin2, arBin3, arBin4, arBin5, arBin6, arBin7 = [], [], [], [], [], [], []
        for j in range(row):
            a, b, c, d, e, f, g = formulas_Encode(i, j)
            ar1.append(a), ar2.append(b), ar3.append(c), ar4.append(d), ar5.append(e), ar6.append(f), ar7.append(g)
            aBin = huffmanConvertion(a, i, j)
            bBin = huffmanConvertion(b, i, j)
            cBin = huffmanConvertion(c, i, j)
            dBin = huffmanConvertion(d, i, j)
            eBin = huffmanConvertion(e, i, j)
            fBin = huffmanConvertion(f, i, j)
            gBin = huffmanConvertion(g, i, j)
            arBin1.append(aBin), arBin2.append(bBin), arBin3.append(cBin), arBin4.append(dBin)
            arBin5.append(eBin), arBin6.append(fBin), arBin7.append(gBin)
        en1.append(ar1), en2.append(ar2), en3.append(ar3), en4.append(ar4)
        en5.append(ar5), en6.append(ar6), en7.append(ar7)
        enBin1.append(arBin1), enBin2.append(arBin2), enBin3.append(arBin3), enBin4.append(arBin4)
        enBin5.append(arBin5), enBin6.append(arBin6), enBin7.append(arBin7)
    return en1, en2, en3, en4, en5, en6, en7, enBin1, enBin2, enBin3, enBin4, enBin5, enBin6, enBin7


def decoder(bin1, bin2, bin3, bin4, bin5, bin6, bin7):
    """
    Decode the binary matrices
    :param bin1: binary matrix using predictor formula 1
    :param bin2: binary matrix using predictor formula 2
    :param bin3: binary matrix using predictor formula 3
    :param bin4: binary matrix using predictor formula 4
    :param bin5: binary matrix using predictor formula 5
    :param bin6: binary matrix using predictor formula 6
    :param bin7: binary matrix using predictor formula 7
    :return: 7 matrices of coefficients and 7 matrices of decompressed images
    """
    coe1, coe2, coe3, coe4, coe5, coe6, coe7 = [], [], [], [], [], [], []
    for i in range(16):
        arCoe1, arCoe2, arCoe3, arCoe4, arCoe5, arCoe6, arCoe7 = [], [], [], [], [], [], []
        for j in range(16):
            val1 = huffmanDecoder(bin1[i][j], i, j)
            arCoe1.append(val1)
            val2 = huffmanDecoder(bin2[i][j], i, j)
            arCoe2.append(val2)
            val3 = huffmanDecoder(bin3[i][j], i, j)
            arCoe3.append(val3)
            val4 = huffmanDecoder(bin4[i][j], i, j)
            arCoe4.append(val4)
            val5 = huffmanDecoder(bin5[i][j], i, j)
            arCoe5.append(val5)
            val6 = huffmanDecoder(bin6[i][j], i, j)
            arCoe6.append(val6)
            val7 = huffmanDecoder(bin7[i][j], i, j)
            arCoe7.append(val7)
        coe1.append(arCoe1)
        coe2.append(arCoe2)
        coe3.append(arCoe3)
        coe4.append(arCoe4)
        coe5.append(arCoe5)
        coe6.append(arCoe6)
        coe7.append(arCoe7)
    decom1 = deepcopy(coe1)
    decom2 = deepcopy(coe2)
    decom3 = deepcopy(coe3)
    decom4 = deepcopy(coe4)
    decom5 = deepcopy(coe5)
    decom6 = deepcopy(coe6)
    decom7 = deepcopy(coe7)
    for i in range(16):
        for j in range(16):
            a, b, c, d, e, f, g = formulas_Decode(decom1, decom2, decom3, decom4, decom5, decom6, decom7, i, j)
            decom1[i][j] = a
            decom2[i][j] = b
            decom3[i][j] = c
            decom4[i][j] = d
            decom5[i][j] = e
            decom6[i][j] = f
            decom7[i][j] = g
    return coe1, coe2, coe3, coe4, coe5, coe6, coe7, decom1, decom2, decom3, decom4, decom5, decom6, decom7


def printMatrix(matrix):
    """
    Prints a matrix
    :param matrix: A matrix(2D array)
    :return: None
    """
    for rows in matrix:
        for value in rows:
            print(value, end=' ')
        print()


def printResults(en, enBin, coe, decom, formulaNumber):
    """
    Prints coefficients after the predictor, the compressed image,the Coefficients after decompression, and
    decompressed image
    :param en: Matrix of coefficients after the predictor
    :param enBin: Matrix of compressed image
    :param coe: Matrix of Coefficients after decompression
    :param decom: Matrix of decompressed image
    :param formulaNumber: prediction formula number
    :return: None
    """
    print("********************************************************")
    print("Coefficients(formula " + str(formulaNumber) + ")")
    print("********************************************************")
    printMatrix(en)
    print("********************************************************")
    print("compressed image(formula " + str(formulaNumber) + ")")
    print("********************************************************")
    printMatrix(enBin)
    print("********************************************************")
    print("Coefficients after Huffman decoder(formula " + str(formulaNumber) + ")")
    print("********************************************************")
    printMatrix(coe)
    print("********************************************************")
    print("Decompressed image(formula " + str(formulaNumber) + ")")
    print("********************************************************")
    printMatrix(decom)
    print("********************************************************")


def countImageBits():
    """
    counts number of bits in the original image
    :return: number of bits
    """
    count = 0
    for rows in image:
        for values in rows:
            binary = bin(values)[2:]
            count = count + len(binary)
    return count


def countEncodeBits(matrix):
    """
    counts number of bits in a matrix
    :param matrix: 2D array
    :return: number of bits
    """
    count = 0
    for rows in matrix:
        for values in rows:
            count = count + len(str(values))
    return count


def calculateCR(bin):
    """
    calculates the compression ratio
    :param bin:Matrix of compressed image
    :return: compression ratio
    """
    bits = countImageBits()
    countBit1 = countEncodeBits(bin)
    cr = bits / countBit1
    return cr


def RMSError(decompressed):
    """
    Calculates the RMS error
    :param decompressed: Matrix of decompressed image
    :return: RMS error
    """
    sum = 0
    for i in range(16):
        for j in range(16):
            sum = sum + (image[i][j] - decompressed[i][j]) ** 2
    return sum


# Driver program
if __name__ == "__main__":

    """Calculating the 7 matrices of coefficients after the predictors and 
    the 7 matrices of compressed images in the form of binary sequence"""
    en1, en2, en3, en4, en5, en6, en7, enBin1, enBin2, enBin3, enBin4, enBin5, enBin6, enBin7 = encoder()

    """Calculating the 7 matrices of Coefficients after Huffman decoder and 
    the 7 matrices of images after decompression """
    coe1, coe2, coe3, coe4, coe5, coe6, coe7, decom1, decom2, decom3, decom4, decom5, \
    decom6, decom7 = decoder(enBin1, enBin2, enBin3, enBin4, enBin5, enBin6, enBin7)

    # Printing original image
    print("********************************************************")
    print("Original Image")
    print("********************************************************")
    printMatrix(image)

    """printing coefficients after the predictor, the compressed image,
    the Coefficients  after Huffman decoder, and decompressed image"""
    printResults(en1, enBin1, coe1, decom1, 1)
    printResults(en2, enBin2, coe2, decom2, 2)
    printResults(en3, enBin3, coe3, decom3, 3)
    printResults(en4, enBin4, coe4, decom4, 4)
    printResults(en5, enBin5, coe5, decom5, 5)
    printResults(en6, enBin6, coe6, decom6, 6)
    printResults(en7, enBin7, coe7, decom7, 7)

    # Calculating Compression ratios
    CR1 = calculateCR(enBin1)
    CR2 = calculateCR(enBin2)
    CR3 = calculateCR(enBin3)
    CR4 = calculateCR(enBin4)
    CR5 = calculateCR(enBin5)
    CR6 = calculateCR(enBin6)
    CR7 = calculateCR(enBin7)

    # Calculating bits/pixel
    bitsPerPixel1 = 8 / CR1
    bitsPerPixel2 = 8 / CR2
    bitsPerPixel3 = 8 / CR3
    bitsPerPixel4 = 8 / CR4
    bitsPerPixel5 = 8 / CR5
    bitsPerPixel6 = 8 / CR6
    bitsPerPixel7 = 8 / CR7

    # Calculating RMS error
    RMS1 = RMSError(decom1)
    RMS2 = RMSError(decom2)
    RMS3 = RMSError(decom3)
    RMS4 = RMSError(decom4)
    RMS5 = RMSError(decom5)
    RMS6 = RMSError(decom6)
    RMS7 = RMSError(decom7)

    # Printing the results of the calculation
    table = [["Formula 1", CR1, bitsPerPixel1, RMS1], ["Formula 2", CR2, bitsPerPixel2, RMS2],
             ["Formula 3", CR3, bitsPerPixel3, RMS3], ["Formula 4", CR4, bitsPerPixel4, RMS4],
             ["Formula 5", CR5, bitsPerPixel5, RMS5], ["Formula 6", CR6, bitsPerPixel6, RMS6],
             ["Formula 7", CR7, bitsPerPixel7, RMS7]]
    headers = ["CR", "Bits/Pixel", "RMS Error"]
    print(tabulate(table, headers, tablefmt="pretty"))
