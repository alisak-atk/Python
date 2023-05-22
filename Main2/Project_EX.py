def display_menu():
    print("======================================================================================================")
    print("||                                        WELCOME TO OUR SHOP                                      ||")
    print("||                                  COFFEE, TEA, AND SWEET DELIGHTS                                ||")
    print("======================================================================================================")
    print("||                              MENU BOARD - COFFEE AND HOT CHOCOLATE                              ||")
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
    print("|| 16. Cupcake     |  12.000 K   || 17. Brownie   |   12.000 K    || 18. Macaron    |   12.000 K   ||")
    print("|| 19. Cookie      |  14.000 K   || 20. Donut     |   14.000 K    || 21. Muffin     |   14.000 K   ||")
    print("|| 22. Croissant   |  16.000 K   ||                               ||                               ||")
    print("======================================================================================================")


def display_type_menu():
    print("===================================================")
    print(" ||                     TYPE                     ||")
    print("====================================================")
    print(" || 1. HOT                                       ||")
    print(" || 2. COLD                                      ||")
    print(" || 3. SMOOTHIE SHAKE                            ||")
    print("====================================================")


def display_size_menu():
    print("===================================================")
    print(" ||                     SIZE                     ||")
    print("===================================================")
    print(" || 1. S (SMALL)         ||    20.000 K          ||")
    print(" || 2. M (MEDIUM)        ||    25.000 K          ||")
    print(" || 3. L (LARGE)         ||    30.000 K          ||")
    print("===================================================")


def main():
    display_menu()
    total_amount = 0  # ຕົວແປເພື່ອເກັບຈໍານວນທັງຫມົດ
    ordered_items = []  # ເກັບຮັກສາຊື່ລາຍການທີ່ສັ່ງ

    while True:
        choice = input("choose menu number (1-22) or 'q' to quit: ")
        if choice == 'q':
            print("Thank you for visiting. Goodbye!")
            break

        try:
            menu_item = int(choice)
            if menu_item < 1 or menu_item > 22:
                print("don't have this menu. Please try again.")
                continue
        except ValueError: # except ແມ່ນການກວດສອບເງື່ອນໄຂ ຖ້າບໍ່ຖືກເງື່ອນໄຂ ແລ້ວຈະໄຫ້ ໂປຣແກຣມເຮັດຫຍັງຕໍ່
            print("Invalid input. Please try again.")
            continue

        display_type_menu()
        while True:
            type_choice = input("Enter the type number (1-3) or 'q' to go back: ")
            if type_choice == 'q':
                break

            try:
                item_type = int(type_choice)
                if item_type < 1 or item_type > 3:
                    print("Invalid type. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please try again.")
                continue

            display_size_menu()
            while True:
                size_choice = input("Enter the size number (1-3) or 'q' to go back: ")
                if size_choice == 'q':
                    break

                try:
                    item_size = int(size_choice)
                    if item_size < 1 or item_size > 3:
                        print("Invalid size. Please try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue

                price = create_bill(menu_item, item_type, item_size)  # ຮັບລາຄາຈາກຟັງຊັນ create_bill
                total_amount += price  # ການບວກລາຄາທັງຫມົດ

                # ​ເພີ່ມ​​ໄປ​ໃນ​​ລາຍ​ການ​ລາຍ​ການ​ສັ່ງ​
                ordered_item_name = get_menu_item_name(menu_item)
                ordered_items.append(ordered_item_name)

                print("Current Total Amount:", total_amount, "K")

                payment_choice = input("Enter 'p' to make payment or any other key to continue: ")
                if payment_choice == 'p':
                    generate_bill(ordered_items, total_amount)  # ສົ່ງຄ່າການສັ່ງຊີ້ ແລະ ຈຳນວນເງີນທັງໝົດໄປໃນ funtion generate_bill
                    make_payment(total_amount)  # ສົ່ງຈຳນວນທັງໝົດໄປ funtion make_payment
                    print("Thank you for your purchase!")
                    total_amount = 0  # reset ຈໍານວນທັງຫມົດຫຼັງຈາກການຈ່າຍເງິນ
                    ordered_items = []  # Clear ລາຍຊື່ order ທັງໝົດ
                    break
                else:
                    break
            break


def create_bill(menu_item, item_type, item_size):
    # ຄິດໄລ່ລາຄາໂດຍອີງໃສ່ລາຍການເມນູ, ປະເພດ, ແລະຂະຫນາດ
    price = 0
    if menu_item in range(1, 9):
        price += 20000  # ລາຄາກາເຟ
    elif menu_item in range(9, 16):
        price += 15000  # ລາຄາກາຊາ
    elif menu_item in range(16, 23):
        price += 12000  # ລາຄາຂອງຫວານ

    if item_type == 3:  # ປັ່ນບວກລລາຄາຂື້ນ 5000 ກີບ
        price += 5000

    if item_size == 2:  # ຈອກກາງບວກລາຄາ 5000 ກີບ
        price += 5000
    elif item_size == 3:  # ຈອກໃຫຍ່ບວກລາຄາ 10000 ກີບ
        price += 10000

    print("===================================")
    print("           ITEM DETAILS            ")
    print("===================================")
    print("Menu Item:", get_menu_item_name(menu_item))  # ສະແດງລາຍຊື່ເມນູ
    print("Type:", item_type)
    print("Size:", item_size)
    print("Price:", price, "K")
    
    return price  # ສົ່ງຄືນລາຄາຈາກຟັງຊັນ create_bill


def get_menu_item_name(menu_item):
    # ສົ່ງຊື່ກັບຕາມໝາຍເລກຂອງ menu
    menu_items = {
        1: "Espresso", 2: "Americano", 3: "Latte", 4: "Cappuccino", 5: "Chocolate", 6: "Frappuccino",
        7: "Mocha", 8: "Coffee", 9: "Black Tea", 10: "Green Tea", 11: "Oolong Tea", 12: "Chai Tea",
        13: "Herbal Tea", 14: "Thai Tea", 15: "Bubble Tea", 16: "Cupcake", 17: "Brownie", 18: "Macaron",
        19: "Cookie", 20: "Donut", 21: "Muffin", 22: "Croissant"
    }
    return menu_items.get(menu_item, "Unknown")


def generate_bill(ordered_items, total_amount):
    print("=========================")
    print("       ORDER DETAILS     ")
    print("=========================")
    print("Ordered Items:")
    for item in ordered_items:
        print("- " + item)
    print("Total Amount:", total_amount, "K")


def make_payment(amount):
    #ການຈ່າຍເງິນ
    print("Payment of", amount, "K received. Thank you for your purchase!")


if __name__ == "_main_":
    main()