# print("Hello World!")
# print("Hello bro!!")
# x = int(input(">>"))
# y = int(input(">>"))
# z = x + y
# print(z)
# print("=====XD=====")
# print("------3232--------")

# print("======================================")
# print("==          WELCOME TO OUR          ==")
# print("==            COFFEE SHOP           ==")
# print("======================================")
# print("==        MENU BOARD - COFFEE       ==")
# print("======================================")
# print("== 1. Espresso                      ==")
# print("== 2. Americano                     ==")
# print("== 3. Latte                         ==")
# print("== 4. Cappuccino                    ==")
# print("== 5. Mocha                         ==")
# print("== 6. Chocolate                     ==")
# print("== 7. Frappuccino                   ==")
# print("======================================")
# print("==        MENU BOARD - TEA          ==")
# print("======================================")
# print("== 8. Black Tea                     ==")
# print("== 9. Green Tea                     ==")
# print("== 10. Oolong Tea                   ==")
# print("== 11. Chai Tea                     ==")
# print("== 12. Herbal Tea                   ==")
# print("== 13. Bubble Tea                   ==")
# print("== 14. Thai Tea                     ==")
# print("======================================")
def main1():
    print("====================================================")
    print(" || 1. HOT                                       ||")
    print(" || 2. COLD                                      ||")
    print(" || 3. SMOOTHIE SHAKE                            ||")
    print("====================================================")


def main2():
    print("===================================================")
    print(" || 1. S (SMALL)           ||    20.000 K        ||")
    print(" || 2. M (MEDIUM)          ||    25.000 K        ||")
    print(" || 3. L (LARGE)           ||    30.000 K        ||")
    print("===================================================")

def main():
    print("======================================================================================================")
    print("||                                      WELCOME TO OUR SHOP                                        ||")
    print("||                             COFFEE, TEA, AND SWEET DELIGHTS                                     ||")
    print("======================================================================================================")
    print("||                        MENU BOARD - COFFEE AND HOT CHOCOLATE                                    ||")
    print("======================================================================================================")
    print("|| 1. Espresso                   ||  4. Cappuccino                ||  7. Mocha                     ||")
    print("|| 2. Americano                  ||  5. Chocolate                 ||  8. Coffee                    ||")
    print("|| 3. Latte                      ||  6. Frappuccino               ||                               ||")
    print("======================================================================================================")
    print("||                                  MENU BOARD - TEA AND ICED TEA                                  ||")
    print("======================================================================================================")
    print("||  9. Black Tea                 || 11. Oolong Tea                || 13. Herbal Tea                ||")
    print("|| 10. Green Tea                 || 12. Chai Tea                  || 14. Thai Tea                  ||")
    print("|| 15. Bubble Tea                ||                               ||                               ||")  
    print("======================================================================================================")
    print("||                                      MENU BOARD - SWEETS                                        ||")
    print("======================================================================================================")
    print("|| 16. Cupcake                   || 17. Brownie                   || 18. Macaron                   ||")
    print("|| 19. Cookie                    || 20. Donut                     || 21. Muffin                    ||")
    print("|| 22. Croissant                 ||                               ||                               ||")
    print("======================================================================================================")
count = 0
espresso = 0
americano = 0
latte = 0
cappuccino = 0
chocolate = 0
frappuccino = 0
mocha = 0
coffee = 0
black_tea = 0
green_tea = 0
oolong_tea = 0 
chai_tea = 0
herbal_tea = 0
thai_tea = 0
buble_tea = 0

while True:
    main()
    A = int(input("Choose: "))
    if A == 1:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is espresso: {espresso} cup(s)")
    elif A == 2:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is americano (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    americano = americano + 1 
                    print(f"Your Order is americano: {americano} cup(s)")
            elif C == 2:
                print("Your menu is americano (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    americano = americano + 1 
                    print(f"Your Order is americano: {americano} cup(s)")
            elif C == 3:
                print("Your menu is americano (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    americano = americano + 1 
                    print(f"Your Order is americano: {americano} cup(s)")
    elif A == 3:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is latte (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    latte = latte + 1 
                    print(f"Your Order is latte: {latte} cup(s)")
            elif C == 2:
                print("Your menu is latte (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    latte = latte + 1 
                    print(f"Your Order is latte: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Elatte (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    elatte = latte + 1 
                    print(f"Your Order is latte: {latte} cup(s)")
    elif A == 4:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is cappuccino (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    cappuccino = cappuccino + 1 
                    print(f"Your Order is cappuccino: {cappuccino} cup(s)")
            elif C == 2:
                print("Your menu is cappuccino (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    cappuccino = cappuccino + 1 
                    print(f"Your Order is cappuccino: {cappuccino} cup(s)")
            elif C == 3:
                print("Your menu is cappuccino (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    cappuccino = cappuccino + 1 
                    print(f"Your Order is cappuccino: {cappuccino} cup(s)")
    elif A == 5:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is chocolate (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    chocolate = chocolate + 1 
                    print(f"Your Order is chocolate: {chocolate} cup(s)")
            elif C == 2:
                print("Your menu is chocolate (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    chocolate = chocolate + 1 
                    print(f"Your Order is chocolate: {chocolate} cup(s)")
            elif C == 3:
                print("Your menu is chocolate (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    chocolate = chocolate + 1 
                    print(f"Your Order is chocolate: {chocolate} cup(s)")
    elif A == 6:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is frappuccino (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    frappuccino = frappuccino + 1 
                    print(f"Your Order is frappuccino: {frappuccino} cup(s)")
            elif C == 2:
                print("Your menu is frappuccino (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    frappuccino = frappuccino + 1 
                    print(f"Your Order is frappuccino: {frappuccino} cup(s)")
            elif C == 3:
                print("Your menu is frappuccino (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    frappuccino = frappuccino + 1 
                    print(f"Your Order is Espresso: {frappuccino} cup(s)")
    elif A == 7:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 8:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 9:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 10:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 11:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 12:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 13:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 14:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    elif A == 15:
        main1()
        B = int(input("Choose: "))
        if B == 1 or 2 or 3:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso (S)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 2:
                print("Your menu is Espresso (M)")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
            elif C == 3:
                print("Your menu is Espresso (L)")
                D = input("You wanna order: Yes or No : ")
                if D == "No":
                    break
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    
    else:
        print("Invalid input. Please choose again.")
#khsafj
