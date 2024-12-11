from gempa import *

gempaPertama = Gempa(1.2, 'Bandung')
gempaKedua = Gempa(6.1, 'Palu')
gempaKetiga = Gempa(5.6, 'Cianjur')
gempaKeempat = Gempa(3.3, 'Jayapura')
gempaKelima = Gempa(4.0, 'Garut')

gempaPertama.dampak()
gempaKedua.dampak()
gempaKetiga.dampak()
gempaKeempat.dampak()
gempaKelima.dampak()
print(f'Jumlah Gempa {Gempa.jumlahGempa}')



#Object Gempa
#Gempa pertama di Banten dengan skala 1.2
#Gempa kedua di Palu dengan skala 6.1
#Gempa ketiga di Cianjur dengan skala 5.6
#Gempa keempat di Jayapura dengan skala 3.3
#Gempa kelima di Garut dengan skala 4.0