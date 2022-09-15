#menghitung luas permukaan balok
print("PROGRAM MENGHITUNG LUAS PERMUKAAN BALOK") 
p =int(input("masukkan panjangnya = "))
l =int(input("masukkan lebarnya = "))
t =int(input("masukkan tingginya = "))
luas =2*((p*l)+(p*t)+(l*t))
print("hasil luasnya adalah = ", luas)

# print di gunakan untuk menampilkan sebuah kata atau kalimat
# p (panjang) ,l (lebar), t (tinggi)
# p, l , t saya gunakan untuk nama variabel supaya mempermudah pemanggilan suatu variabel
# int (integer) adalah sebuah tipe data yang dimana berupa bilangan bulat
# input di gunakan untuk memasukkan data dari user
# rumus menghitung luas balok adalah 2*((p*l)+(p*t)+(l*t))