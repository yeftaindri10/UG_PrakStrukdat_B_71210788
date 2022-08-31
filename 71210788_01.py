while True:
    print ("===Pilih operasi perhitungan yang akann dilakukan===")
    print ("1. Operasi penjumlahan")
    print ("2. Operasi pengurangan")
    print ("3. Operasi perkalian")
    print ("4. Operasi pembagian")
    print ("Ketik Q pada pilihan untuk menghentikan operasi")

    masuk =(input("Masukkan pilihan: "))

    if masuk == "Q":
        break
    bil1 = int(input("Masukkan bilangan 1 : "))
    bil2 = int(input("Masukkan bilangan 2 : "))

    if masuk == "1":
       print (bil1 + bil2)
    elif masuk == "2":
       print (bil1 - bil2)
    elif masuk == "3":
      print  (bil1 * bil2)
    elif masuk == "4":
        print (bil1 / bil2)



