def numAppend():
    global arr
    x = range(a+1, b)
    for num in x:
        arr.append(num)

def main():
    global mid
    mid = sum(arr) / len(arr)

def comparer():
    global compared
    for i in arr:
        if i > mid:
            compared.append(i)
            
def arrFormat():
    for n in compared:
        print(n, end = ' ')

while True:
    arr = []
    mid = 0
    compared = []
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
        comparer()
        print(f"\033[32m \nƏdədlərin ədədi ortası : {mid}")
        print('\033[32m' + "Şərti ödəyən ədədlər :")
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