print('Selamat Datang di KOSATAN')
print('Silahkan Login Terlebih dahulu!')
id = str(input("ID : "))
print('Masukan Password')
pw = str(input("Password : "))
while pw != "kosatanedan":
    print("Maaf Password salah, Silahkan masukan lagi")
    pw = str(input("Password : "))
if pw == "kosatanedan" :

     while True:
         # print("")
         menu = int(input("Selamat Datang di Dashboard KOSATAN\nKetik angka untuk melanjutkan \n 1.Backroom \n 2.Casino Room \n 3.Canteen \nMasukan Pilihan anda (ketik angka) : "))

         if menu == 1 :

             print("\nSelamat Datang di Backroom KOSATAN \nKami menyediakan lonte yang sangat enak, seenak fitbar")
             listlon = ["XX-Simar", "XX-Rajah"]
             pilon  = int(input("pilih mau lonte yang mana? \n 1.Simar \n 2.Raja \nMasukan Pilihan anda (ketik angka) : "))
             while True :
                if pilon == 1 :
                  print("Kamu memilih onta yang bernama : ", listlon[0])
                  break
                elif pilon == 2 :
                  print("Kamu memilih onta yang bernama : ", listlon[1])
                  break
                else :
                 print("GOBLOK DISURUH 1/2 MALAH MILIH YANG LAIN MAMPUS LOOPING")
             break

         elif menu == 2 :
             print("Selamat Datang di Casino KOSATAN \nAnda menang kami tidak senang")

             game = int(input("Mau main game apa? \n 1.Quiz \n 2.Poker \n"))
             if game == 1 :
                 benar = []
                 salah = []
                 print("Kamu Memilih Quiz")
                 print("1.Jika Fadlol mengeluarkan kartu Flush\nAgar Menang kamu mengeluarkan kartu... ")
                 jaku = int(input("A.Pair of King\nB.Straight\nC.Full House\nD.Pair of 2\nJawaban :"))
                 print("2.Jika Adlos mengeluarkan kartu Fullhouse of Queen\nAgar Menang kamu mengeluarkan kartu... ")
                 jaku = int(input("A.Straight\nB.Flush\nC.Royal Flush\nD.Pair of 2\nJawaban :"))

                 benar.append(jaku)

                 print("Jawaban yang benar : ",benar)

             break
         elif menu == 3 :
             print("Selamat Datang di Canteen KOSATAN \nBanyak makanan yang sangat enak tapi basi")
             break
         else :
             print("Invalid Command")


else :
     print("iqbal salah")