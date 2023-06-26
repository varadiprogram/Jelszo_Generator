import time


print("⠀⠀⠀⠀     ⣀⣠⣤⣤⣶⣶⣶⣶⣶⣶⣠⣤⣤⣀⣀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⣀⣴⣾⠿⠟⠛⠛⠉⠉⠉⠉⠉⠛⠛⠛⠿⠿⡿⠛⢿⣿⣷⣤")
print("⠀⠀⠀⣠⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠉⠁")
print("⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠀⠀")
print("⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀")
print("⠋⠀⠀⠀⠀⠀ ⢀⣤⣤⣤⣶⣶⣆⢤⣤⣀⣀⠀⠀⠀⠀⣸⡟⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢸⡿⠋⠙⢿⣿⣿⣿⣻⣿⣿⡇⠀⠀⠀⣿⠇⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⠐⢻⣿⣻⣷⡽⣿⣷⠀⠀⢸⣿⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⠐⢻⣿⣻⣷⡽⣿⣷⠀⠀⢸⣿⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠿⣃⠹⠿⠗⣿⣷⣻⣿⡽⣿⣧⠀⣼⡇⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣴⡏⣁⢀⠲⣿⣿⣷⢻⣿⡽⣿⢀⣿⠁⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⣉⣡⣿⣿⣿⣏⣿⣿⣿⣼⡿⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢰⡿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠛⠛⠛⠆⠀⠀⠀⠀⠀")
print("  ⠀⠀⠀⠀⠀⠈⠛⠘⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
valasz = input("random jelszó generátor(Üsd le az entert)")

random_jelszo_betui = \
{"A","B","C","D", "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}

random_jelszo_karakters_more = \
    {"0","1","2","3","4","5","6","7","8","9","$","ß","ł","đ","đ","€","÷","×","#","@","[","]","{","}",".",",","-","_",}

random_jelszo = random_jelszo_betui.union(random_jelszo_karakters_more)

print(".")
time.sleep(0.7)
print("..")
time.sleep(0.7)
print("...")
time.sleep(0.7)
print("a jelszavad:")

for x in random_jelszo:
    print(x, end='')

print("")
print("")
time.sleep(1)
print("egytől ötös skálán kell értékelnie, csak írja be a számot")
time.sleep(0.3)
ertekeles = int(input("értékeld a programot(1-5): "))


time.sleep(0.5)
print("köszönöm hogy a programom használta!")
time.sleep(0.9)
print(end='')



if ertekeles == 5:
    print("értékelesed: hibátlan")

elif ertekeles == 4:
    print("értékelésed: jó")

elif ertekeles == 3:
    print("értékelésed: közepes")

elif ertekeles == 2:
    print("értékelésed: elmegy")

elif ertekeles == 1:
    print("értékelésed: rossz")
else:
    print("nem jól töltötte ki ezt az egyszerű kérdést ezért maga tutira AUTISTA!!!")
    time.sleep(0.3)























