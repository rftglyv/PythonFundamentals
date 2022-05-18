c = []
arr = []

def numAppend():
    x = range(a+1, b)
    for num in x:
        c.append(num)

def main():
    for i in c:
        if i%5==0 and i%7!=0:
            arr.append(i)

def arrFormat():
    for n in arr:
        print(n, end = ' ')

while True:
    try:
        a = int(input("A ədədini daxil edin : "))
        b = int(input("B ədədini daxil edin : "))
    except ValueError:
        raise ValueError("Düzgün dəyər daxil edilməyib!") from None

    if a>b:
        print('\033[31m' + "\nDaxil edilən dəyərlər tələblərə uyğun deyil!")
        broker = input('\033[33m' + "Proqram yenidən başladılsın ? H/Y : ")
        print('\033[39m')
    elif a<b:
        numAppend()
        main()
        print('\033[32m' + "\nŞərti ödəyən ədədlər :")
        arrFormat()
        broker = input('\033[33m' + "\n\nProqram yenidən başladılsın ? H/Y : ")
        print('\033[39m')
    else:
        print('\033[31m' + "\nNəsə düzgün getmədi!")
        broker = input('\033[33m' + "Proqram yenidən başladılsın ? H/Y : ")
        print('\033[39m')

    if broker.upper() == "H":   
        continue    
    print('\033[34m' + "Proqram sona çatdırıldı!")
    print('\033[39m')
    break
        
