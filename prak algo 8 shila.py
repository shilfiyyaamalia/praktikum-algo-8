# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 23:14:30 2022

@author: shilaa
"""

# penjumlahan dengan fungsi rekursif
def penjumlahan(a,b):
    if a == 0:
        return b
    else:
        return 1 + penjumlahan(a-1,b)

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
print(penjumlahan(angka1,angka2))

# desimal ke biner
def desimal_ke_biner(c):
    if c == 0:
        return 0
    else:
        return c % 2 + 10 * desimal_ke_biner(int(c/2))

print(desimal_ke_biner(int(input('masukkan angka desimal: '))))