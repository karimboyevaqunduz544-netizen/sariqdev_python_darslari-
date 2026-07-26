#tuple da metodlarni qo'llash
 
viloyatlar = ('Xorazm' , ' Samarqand', 'Buxoro', 'Andijon', 'Toshkent'  )
shaharlar= tuple()
print(viloyatlar)
print('kortejdagi x element soni' , viloyatlar.count('Buxoro'))
print("kortejdagi x element indeksi" , viloyatlar.index("Andijon"))
print("kortejni tekshirish" , any(viloyatlar))
print("kortejni tekshirish" , any(shaharlar))
print("max element: " , max(viloyatlar))
print("min element: " , min(viloyatlar))
print("kortej uzunligi: " , len(viloyatlar))

"""
Kutilgan natija quyidagicha:
	
	('Xorazm', ' Samarqand', 'Buxoro', 'Andijon', 'Toshkent')
kortejdagi x element soni 1
kortejdagi x element indeksi 3
kortejni tekshirish True
kortejni tekshirish False
max element:  Xorazm
min element:   Samarqand
kortej uzunligi:  5


"""
