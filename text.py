import random
import time

def reqemi_tap():
    random_reqem = random.randint(1, 40)
    haqq = 6
    
    print("1 ile 40 arasında bir reqem tapmağa çalışın. Toplam 6 haqqınız var.")
    
    while haqq > 0:
        try:
            tahmin = int(input("Tahmininizi daxil edin: "))
        except ValueError:
            print("Zəhmət olmasa bir reqem daxil edin.")
            continue
        
        if tahmin < 1 or tahmin > 40:
            print("Zəhmət olmasa 1 ile 40 arasında bir reqem daxil edin.")
            continue
        
        if tahmin == random_reqem:
            print("Təbriklər, doğru tapdınız!")
            break
        elif tahmin < random_reqem:
            haqq -= 1
            print(f"Yanlış, random reqem daha böyükdür. {haqq} haqqınız qaldı.")
        else:
            haqq -= 1
            print(f"Yanlış, random reqem daha kiçikdir. {haqq} haqqınız qaldı.")
        
        time.sleep(2)
    
    if haqq == 0:
        print(f"Yanlış, cavab: {random_reqem} idi, oyun bitdi.")

if __name__ == "__main__":
    reqemi_tap()