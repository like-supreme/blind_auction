import os
from art import logo
print(logo)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

blind_auction = {}
while True:
    
    name = input("What is the bidders name ? ")
    amount = int(input("What is the amount you bid ?"))
    blind_auction[name] = amount
    clear_screen()
    again = input("Are there any bidders y/n ?")
    if again == "y":
        continue  
    if again == "n":
        break
    else:
        print("Invalid text. pls try again.")
        break
print(blind_auction)

# gereken liste yapısı gözüktü şimdi maksimum kim vermiş onu görmek lazım. bunun için döngüye ihtiyacımız yok 
#sebebi ise zaten döngünn temel işlevi verileri almak. içerde maksimum döndürmek mantıklı olmaz
for key , value in blind_auction.items():
    ismax = max(blind_auction.values())
    if value == ismax:
        winner = key # key olarak tutarsak değişken olduğu için sürekli en son değeri üretecek. yani hatalı olacak. bir değişkeni sabit bir şeye atamak ise burada işimize yarayacak temel olacak
        break
    
print(f"The winner is {key} with {ismax}")  # buradaki for döngüsü hem liste içindeki değerlerin en yükseğini buluyor hemde değerden anahtara ulaitırma işlemini yapıyor.
    
    