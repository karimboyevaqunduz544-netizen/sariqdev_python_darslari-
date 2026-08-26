mevalar = ["olma ", "anor", "anjir", "shaftoli", "banan", "qulupnay"]
harf = "o"
mevalar_b =list(filter(lambda meva:meva.startswith(harf), mevalar)) # mevalar_b degan yangi royxatga mevalardan o harfi bilan boshlanadigan mevani saralab chiqar
print(mevalar_b) # ['olma ']

mevalar2 = list(filter(lambda meva : len(meva)<= 5, mevalar)) #yangi mevalar2 degan royxatga mevalardan uzunligi 5 ga teng va undan kichik mevalarni saralab chiqar
print(mevalar2) #['olma ', 'anor', 'anjir', 'banan']

mevalar3 = list(filter(lambda meva: (meva.startswith('a') and meva.endswith('r')),mevalar)) #mevalar3 royxatga  boshi adan boshlanadigan va r harfi bilan tugidigan mevani saralab chiqar
print(mevalar3) # ["anor" , "anjir"]
