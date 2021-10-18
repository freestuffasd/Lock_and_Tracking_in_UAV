import random
import time
import math

a = (33.65771288706495, 92.21570806743144, 78.32326161621613)


def mesafe(x, y, z, s, d, f):
    c = ((x - s) ** 2) + ((y - d) ** 2) + ((z - f) ** 2)
    return math.sqrt(c)


def en_yakin_siha(a, b, c, d, e, f, g, h, k, l):
    liste = [a, b, c, d, e, f, g, h, k, l]
    return min(liste)


while True:
    time.sleep(1)
    sayac = 0
    liste = [None] * 10
    liste1 = [None] * 10
    sayi = 10
    n = 0
    while sayac < 10:
        e = random.uniform(30, 40)
        b = random.uniform(90, 99)
        i = random.uniform(50, 100)

        liste[sayac] = [e, b, i]
        # print(liste[sayac])
        sayac = sayac + 1

    for g in range(sayi):
        liste1[g] = [mesafe(liste[g][n], liste[g][n + 1], liste[g][n + 2], a[0], a[1], a[2])]
        # print(liste1[g])

    print(
        en_yakin_siha(liste1[0], liste1[1], liste1[2], liste1[3], liste1[4], liste1[5], liste1[6], liste1[7], liste1[8],
                      liste1[9]))
    time.sleep(10)
