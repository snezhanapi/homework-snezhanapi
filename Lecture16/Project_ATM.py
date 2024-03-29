from ATM_Management import validate_pin, show_balance, enter_option, withdraw, deposit, myMain

from Project_ATM_Database import customer_id

customer_name = input("Please enter your name\n")
if customer_name in customer_id.keys():
    customer_id_number = customer_id[customer_name]
    is_pin_valid = validate_pin(customer_id_number)
    if is_pin_valid:
        option = enter_option()
        if option == "balance":
            show_balance(customer_id_number)
        elif option == "withdraw":
            show_balance(customer_id_number)
            withdraw(customer_id_number)
        elif option == "deposit":
            show_balance(customer_id_number)
            deposit(customer_id_number)
    else:
        print("Your card has been blocked")
else:
    print("Invalid customer name")