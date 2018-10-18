Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama ='Muhammad Wafiq Akhimullah'
>>> NIM = 'L200180179'
>>> x = '1' + NIM [7:]
>>> a = int(x)
>>> b = len(Nama)
>>> type(a)
<type 'int'>
>>> #artinya a memiliki variabel integer atau bilangan bulat
>>> type(b)
<type 'int'>
>>> #artinya b memiliki variabel integer atau bilangan bulat
>>> a/b
47

>>> #a dibagi b = 47
>>> a//b
47
>>> 10*(a-999)
1800
>>> #variabel a dikurangi 999 dikali 10 = 1800
>>> b**2
625
>>> #variabel b jika dipangkat = 625
>>> a%b
4
>>> #sisa hasil bagi a dibagi b adalah 4
>>> 
>>> 
>>> Nama ='Muhammad Wafiq Akhimullah'
>>> NIM = 'L200180179'
>>> x = '1' + NIM [7:]
>>> a = int(x)
>>> b = len(Nama)
>>> c = 12.5
>>> type(c)
<type 'float'>
>>> #variabel c adalah float atau bilangan real
>>> a/c
94.32
>>> #variabel a dibagi c = 94.32
>>> a%c
4.0
>>> #sisa hasil bagi dari a dibagi c adalah 4.0
>>> 
>>> 
>>> Nama ='Muhammad Wafiq Akhimullah'
>>> NIM = 'L200180179'
>>> x = '1' + NIM [7:]
>>> a = int(x)
>>> b = len(Nama)
>>> c = 12.5
>>> c>b
False
>>> #pernyataan c lebih besar sari b adalah False
>>> type(c>b)
<type 'bool'>
>>> #c>b adalah boolean atau logika
>>> a>b and b>c
True
>>> #artinya kedua pernyataan tersebut benar
>>> a>1100 or b<10
True
>>> #artinya salah satu dari kedua pernyataan tersebut benar
>>> 
>>> 
>>> Nama = 'Muhammad Wafiq Akhimullah'
>>> NIM = 179
>>> Tinggi = 1.75
>>> Berat = 73
>>> TahunLahir = 1999
>>> Aku = (TahunLahir,Berat,Tinggi,NIM,Nama)
>>> Data = (TahunLahir,Berat,Tinggi,NIM,Nama)
>>> type(Aku)
<type 'tuple'>
>>> #artinya Aku adalah tuple atau deretan objek
>>> Aku[0]
1999
>>> #artinya data ke-0 dalam tuple Aku adalah TahunLahir
>>> a = NIM%4; Aku[a]
179
>>> #sisa hasil bagi NIM dibagi 4 = 3, jadi data ke-3 pada tuple Aku adalah NIM
>>> type(Aku[a])
<type 'int'>
>>> #data ke-3 pada tuple adalah integer atau bilangan bulat
>>> Aku [a:4]
(179,)
>>> #data dari a ke-4 adalah 179,
>>> type(Aku[4])
<type 'str'>
>>> #data ke-4 dalam Aku merupakan string
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> Nama = 'Muhammad Wafiq Akhimullah'
>>> NIM = 179
>>> Tinggi = 1.75
>>> Berat = 73
>>> TahunLahir = 1999
>>> Aku = (TahunLahir,Berat,Tinggi,NIM,Nama)
>>> Data = (TahunLahir,Berat,Tinggi,NIM,Nama)
>>> type(Aku)
>>> type(Aku)
<type 'tuple'>
>>> type(Data)
<type 'tuple'>
>>> 
>>> 
>>> 
>>> Nama = 'Muhammad Wafiq Akhimullah'
>>> NIM = 179
>>> Tinggi = 1.75
>>> Berat = 73
>>> TahunLahir = 1999
>>> Aku = (TahunLahir,Berat,Tinggi,NIM,Nama)
>>> Data = (TahunLahir,Berat,Tinggi,NIM,Nama)
>>> type(Data)
<type 'tuple'>
>>> 
>>> 
>>>  Nama = 'Muhammad Wafiq Akhimullah'
>>> NIM = 179
>>> Tinggi = 1.75
>>> Berat = 73
>>> TahunLahir = 1999
>>> Aku = (TahunLahir,Berat,Tinggi,NIM,Nama)
  File "<pyshell#73>", line 2
    Nama = 'Muhammad Wafiq Akhimullah'
    ^
IndentationError: unexpected indent
>>> Nama = 'Muhammad Wafiq Akhimullah'
>>> NIM = 179
>>> Tinggi = 1.75
>>> Berat = 73
>>> TahunLahir = 1999
>>> Aku = (TahunLahir,Berat,Tinggi,NIM,Nama)
>>> Data = [TahunLahir,Berat,Tinggi,NIM,Nama]
>>> type(Data)
<type 'list'>
>>> #Data adalah List
>>> type(Data[4])
<type 'str'>
>>> #Data ke-4 adalah string(Nama)
>>> Data[4][5]
'm'
>>> Data[4]
'Muhammad Wafiq Akhimullah'
>>> a = NIM%4
>>> Data[4][a:6]
'amm'
>>> #dalam Data ke-4 slicing ke a-6 adalah amm
>>> a
3
>>> Data[0]='ok';Data
['ok', 73, 1.75, 179, 'Muhammad Wafiq Akhimullah']
>>> #data ke-0 diganti dengan string ok
>>> Data[-a]
1.75
>>> -a
-3
>>> #artinya data ke-a kurangi 1 = 1.75
>>> range(a)
[0, 1, 2]
>>> #jarak/cakupan sampai ke-a adalah 0,1,2
