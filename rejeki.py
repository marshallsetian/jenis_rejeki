from colorama import Fore ,Style
import time
import sys
import random
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)


mengetik(Style.BRIGHT+Fore.GREEN+"\n8 Jenis Rejeki dari ALLAH :")
mengetik(Fore.LIGHTWHITE_EX+"...............................................")

mengetik(Fore.LIGHTYELLOW_EX +"1.Rejeki yang telah diJamin... ( Hud : 6 )\n")
mengetik(Fore.LIGHTYELLOW_EX +"2.Rejeki karena Bekerja ... ( An - Najm : 38 )\n")
mengetik("3.Rejeki karena Bersyukur ... ( Ibrahim : 7 )\n")
mengetik("4.Rejeki tak Terduga ... ( At - Thalaq : 2-3 )\n")
mengetik("5.Rejeki karena Istigfar ... ( Nuh : 10-11 )\n")
mengetik("6.Rejeki karena Menikah ... ( An - Nur : 32 )\n")
mengetik("7.Rejeki karena Anak ... ( Al - Israa : 31 )\n")
mengetik("8.Rejeki karena Sedekah ... ( Al - Baqarah : 245 )\n\n")

mengetik(Fore.GREEN +"semoga semua Saudara & Teman2 di limpahkan Rejekinya\n")

print(Fore.LIGHTWHITE_EX+"ini adalah akhir dari :")
mengetik(Fore.LIGHTBLUE_EX+"PROGRAM PYTHON 3.9 BY.MARSHALL_SETIAN")



