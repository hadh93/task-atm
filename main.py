from check_card import *
import hyp_bank_api

if __name__ == '__main__':
    # loop
    while True:
        card_info = input("Please Insert a Card\n")

        if not validate_card(card_info):
            break
        card_info = card_info.split()
        card_status = card_info[0]
        card_num = card_info[1]
        card_info = hyp_bank_api.CardInfo(bool(card_status), card_num)

        pin = input("Please enter password:\n")
        if not card_info.password_match(pin):
            print("ERROR: WRONG PASSWORD")
            break

        # password validation successful
        account_info = int(input("Please select account:\n \t 1: Checking \n \t 2: Saving \n"))
        if account_info != 1 and account_info != 2:
            print("ERROR: WRONG ACCOUNT INFORMATION (Should be 1 (Checking) or 2 (Saving))")
            break
        account_info -= 1 # Python index starts with 0, so is bank_db index of this account


        # account selected
        action_num = int(input("Please choose your action: \n \t 1: See Balance \n \t 2: Deposit \n \t 3: Withdraw\n"))
        if action_num == 1:
            print("Current Balance: {}".format(card_info.see_balance(account_info)))
        elif action_num == 2:
            amount = int(input("Insert the amount of money you would like to deposit in dollar($)s:\n"))
            card_info.deposit(account_info, amount)
            print("Current Balance: {}".format(card_info.see_balance(account_info)))
        elif action_num == 3:
            amount = int(input("Insert the amount of money you would like to withdraw in dollar($)s:\n"))
            if not (card_info.check_withdrawable(account_info,amount)):
                print("ERROR: NOT ENOUGH BALANCE")
                break
            card_info.withdraw(account_info, amount)
            print("Current Balance: {}".format(card_info.see_balance(account_info)))
        else:
            print("ERROR: WRONG ACTION SELECTED (Should be 1 (See Balance) or 2 (Deposit) or 3 (Withdraw))")
            break
