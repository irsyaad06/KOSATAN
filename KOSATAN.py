import getpass
user = "keane"
psw = "kosatanedan"

print('Selamat Datang di KOSATAN')
print('Silahkan Login Terlebih dahulu!')
id = str(input("ID : "))
while id != user :
    print("Tidak ada ID yang terdaftar \nSilahkan Coba lagi")
    id = str(input("ID : "))

if id == user :
    print('Masukan Password')
    pw = getpass.getpass("Password : ")
while pw != psw:
    print("Maaf Password salah, Silahkan masukan lagi")
    pw = getpass.getpass("Password : ")
if  pw == psw :

     while True:
         # print("")
         menu = int(input("Selamat Datang di Dashboard KOSATAN\nKetik angka untuk melanjutkan \n 1.Backroom \n 2.Casino Room \n 3.Canteen \nMasukan Pilihan anda (ketik angka) : "))

         if menu == 1 :

             print("\nSelamat Datang di Backroom KOSATAN \nKami menyediakan lonte yang sangat enak, seenak fitbar")
             list_ont = ["asd","asd"]
             for i in list_ont:
                print(i)

                # pilon  = int(input("\nMasukan Pilihan anda (ketik angka) : "))
                # while True :
                #     if pilon == 1 :
                #      print("Kamu memilih onta yang bernama : ", list_onta[0])
                #      break
                #     elif pilon == 2 :
                #      print("Kamu memilih onta yang bernama : ", list_onta[1])
                #      break
                #     else :
                #      print("GOBLOK DISURUH 1/2 MALAH MILIH YANG LAIN MAMPUS LOOPING")
                # break

         elif menu == 2 :
             print("Selamat Datang di Casino KOSATAN \nAnda menang kami tidak senang")

             game = int(input("Mau main game apa? \n 1.Quiz \n 2.Poker \n"))
             if game == 1 :
                 benar = []
                 salah = []
                 print("Kamu Memilih Quiz")
                 print("1.Jika Fadlol mengeluarkan kartu Flush\nAgar Menang kamu mengeluarkan kartu... ")
                 jaku = str(input("A.Pair of King\nB.Straight\nC.Full House\nD.Pair of 2\nJawaban :"))
                 print("2.Jika Adlos mengeluarkan kartu Fullhouse of Queen\nAgar Menang kamu mengeluarkan kartu... ")
                 jaku = str(input("A.Straight\nB.Flush\nC.Royal Flush\nD.Pair of 2\nJawaban :"))

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