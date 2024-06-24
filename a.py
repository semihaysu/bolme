
uzun_tahta=int(input("uzunluk giriniz"))
while uzun_tahta<=0: uzun_tahta=int(input("uzunluk giriniz")) 
parca_sayısı=int(input("parça sayısı giriniz"))
while parca_sayısı<=0: parca_sayısı=int(input("parca sayısı giriniz")) 
parca_uzunluğu=uzun_tahta/parca_sayısı
kesim_nokta=parca_uzunluğu*parca_sayısı
print(parca_uzunluğu)




# i = 1
# while i < 6:
#   print(i) 
#   if i == 3:
#     break
#   i += 1