import random
import time

def reqemi_tap():
    random_reqem = random.randint(1, 40)
    haqq = 6
    
    print("1 ile 40 arasında bir reqem tapmağa çalışın. 6 haqqınız var.")
    
    while haqq > 0:
        try:
            texmin = int(input("Texmininizi daxil edin: "))
        except ValueError:
            print("Zəhmət olmasa bir reqem daxil edin.")
            continue
        
        if texmin < 1 or texmin > 40:
            print("Zəhmət olmasa 1 ile 40 arasında bir reqem daxil edin.")
            continue
        
        if texmin == random_reqem:
            print("Təbriklər, doğru tapdınız!")
            break
        elif texmin < random_reqem:
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
