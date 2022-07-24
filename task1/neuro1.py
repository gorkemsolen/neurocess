import pickle
from itertools import groupby
import matplotlib.pyplot as plt

#pickle dosyasını oku

with open('data1.pkl','rb') as pickle_file:
    new_data =pickle.load(pickle_file)

#verileri say
    
for keys in new_data:
    for i in range(337):
        if (keys=='task'):
            count_dups = [sum(1 for _ in group) for _, group in groupby(new_data[keys])]

print(count_dups)

#verileri ve verilerin tekrar sayılarını atama (1'ler tek sayılara denk düşüyor)

names = {
    "1": "split squat" , 
    "2": "SL squat" , 
    "3": "SL BW Decel" , 
    "4": "SL prone curls",
    "5": "SL glute bridge",
    "6": "SL elevated glue bridge",
    "7": "45deg adductor squeeze",
    "8": "0deg adductor squeeze",
    "9": "copenhagen",
    "10": "SL straight knee calf raise"
}   
counts = {
    names['1']:count_dups[1],
    names['2']:count_dups[3],
    names['3']:count_dups[5],
    names['4']:count_dups[7],
    names['5']:count_dups[9],
    names['6']:count_dups[11],
    names['7']:count_dups[13],
    names['8']:count_dups[15],
    names['9']:count_dups[17],
    names['10']:count_dups[19]
}
print(counts)

#bar grafiğine dökme ve grafik rötüşları

name = list(counts.keys())
count = list(counts.values())
  
fig = plt.figure(figsize = (10, 8))
 
plt.bar(name, count, color ='maroon', width = 0.2)
plt.xticks(
    rotation=20, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='small'  
) 
plt.xlabel("Counted names")
plt.ylabel("Counted values")
plt.title("Graph")
plt.show()
