# -*- coding: utf-8 -*- 
""" 
Created on Fri Nov 11 17:26:22 2022 
 
@author: shilaa 
""" 
 
def penjumlahan(angka = 0, jml = 0, i =1):     
    if ( jml <= 0): 
        return 0    
    else: 
        angka = int(input("Masukan bilangan ke-" + str(i) + ":" 
            ))        
        if (jml == 1):            
            return angka                 
        else: 
            i +=1 
            return angka + penjumlahan (angka, jml-1, i) 
jumlah = int(input("Masukan Jumlah: ")) 
nilai = penjumlahan(jml = jumlah) 
print("hasil dari penjumlahan adalah " + str(nilai)) 


