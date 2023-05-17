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
    print(" || 1. S (SMALL)                                 ||")
    print(" || 2. M (MEDIUM)                                ||")
    print(" || 3. L (LARGE)                                 ||")
    print("===================================================")
    
    
print("======================================================================================================")
print("||                                      WELCOME TO OUR SHOP                                        ||")
print("||                             COFFEE, TEA, AND SWEET DELIGHTS                                     ||")
print("======================================================================================================")
print("||                        MENU BOARD - COFFEE AND HOT CHOCOLATE                                    ||")
print("======================================================================================================")
print("|| 1. Espresso                   ||  4. Cappuccino                ||  5. Mocha                     ||")
print("|| 2. Americano                  ||  6. Chocolate                 ||  7. Coffee                    ||")
print("|| 3. Latte                      ||  8. Frappuccino               ||                               ||")
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
while True:
    A = int(input("Choose: "))
    if A == 1:
        main1()
        B = int(input("Choose: "))
        if B == 1:
            main2()
            C = int(input("Choose: "))
            if C == 1:
                print("Your menu is Espresso")
                D = input("You wanna order: Yes or No :")
                if D == "No":
                    break  
                    print("Its equal = 10.000")
                elif D == "Yes":
                    espresso = espresso + 1 
                    print(f"Your Order is Espresso: {espresso} cup(s)")
    else:
        print("Invalid input. Please choose again.")