# Imelda Putri-2209116016

import os
import random
os.system ('cls')

def quickshort (data):
    # jika panjang array <= 1 maka kembalikan array
    if len (data) <= 1:
        return data
    else:
        pivot = data [0]
        # lebih kecil dari pivot
        left = [x for x in data[1:] if x <= pivot]
        # lebih besar dari pivot
        right = [x for x in data[1:] if x >= pivot]
        # kembalikan semua nilai beserta pivot
        return quickshort(left) + [pivot] + quickshort(right)
    
# Penggunaan
angka = list (range(1,50))
data = random.sample (angka,k=10)

quickshort(data)
print (f"Sebelum Di Sorting: {data}")
result = quickshort(data)
print (f"Sesudah Di Sorting Menggunakan Quickshort: {result}")