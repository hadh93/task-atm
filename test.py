from check_card import *
import hyp_bank_api

if __name__ == '__main__':
    print("\nATM TEST \n\nTIP: ERROR CODES MAY BE PRINTED REGARDLESS OF TEST RESULTS. \n")
    test_with_error = 0

    # Test 1
    print("TEST 1: Validation of Cards")
    test_cases = [
        # Test Inputs
        ["True 1234-1234-1234-1234",
         "True",
         " 1234-1234-1234-1234",
         "1234-1234-1234-1234",
         "True 9999-9999-9999-9999",
         "EXIT"
         ],
        # Expected Test Results
        [True,
         False,
         False,
         False,
         True,
         False
         ]
    ]
    total = len(test_cases[0])
    passed = 0
    for i in range(len(test_cases[0])):
        if validate_card(test_cases[0][i]) == test_cases[1][i]:
            passed += 1
        else:
            print("error on {}th case".format(i))
            print("expected: {}, found: {}".format(test_cases[1][i], validate_card(test_cases[0][i])))
            test_with_error += 1
    print("{} / {} Passed".format(passed,total))

    # Test 2
    print("\n\nTEST 2: Password Validation")
    card_info = hyp_bank_api.CardInfo(True, "1234-1234-1234-1234")
    test_cases=[["0000","1111","2222","9090","1234"],
                [False, False, False, False, True]
                ]
    total = len(test_cases[0])
    passed = 0
    for i in range(len(test_cases[0])):
        if card_info.password_match(test_cases[0][i]) == test_cases[1][i]:
            passed += 1
        else:
            print("error on {}th case".format(i))
            print("expected: {}, found: {}".format(test_cases[1][i], card_info.password_match(test_cases[0][i])))
            test_with_error += 1
    print("{} / {} Passed".format(passed, total))

    # Test 3
    print("\n\nTEST 3: See Balance")
    test_cases=[
        [0,1],
        [150,100]
    ]
    total = len(test_cases[0])
    passed = 0
    for i in range(len(test_cases[0])):
        if card_info.see_balance(test_cases[0][i]) == test_cases[1][i]:
            passed += 1
        else:
            print("error on {}th case".format(i))
            print("expected: {}, found: {}".format(test_cases[1][i], card_info.see_balance(test_cases[0][i])))
            test_with_error += 1
    print("{} / {} Passed".format(passed, total))

    # Test 4
    print("\n\nTEST 4: Deposit")
    test_cases = [
        [
            [0,100],
            [1,1000]
        ],
        [250, 1100]
    ]
    total = len(test_cases[0])
    passed = 0
    for i in range(len(test_cases[0])):
        card_info.deposit(test_cases[0][i][0], test_cases[0][i][1])
        if card_info.see_balance(test_cases[0][i][0]) == test_cases[1][i]:
            passed += 1
        else:
            print("error on {}th case".format(i))
            print("expected: {}, found: {}".format(test_cases[1][i], card_info.see_balance(test_cases[0][i])))
            test_with_error += 1
    print("{} / {} Passed".format(passed, total))

    # Test 5
    print("\n\nTEST 5: Check if the amount entered is withdrawable")
    card_info = hyp_bank_api.CardInfo(True, "9999-9999-9999-9999")
    test_cases = [
        [
            [0, 1000],
            [1, 10000],
            [0, 100],
            [1, 200],
            [0, 10000],
            [1, 10001]
        ],
        [True, True, True, True, False, False]
    ]
    total = len(test_cases[0])
    passed = 0
    for i in range(len(test_cases[0])):
        if card_info.check_withdrawable(test_cases[0][i][0], test_cases[0][i][1]) == test_cases[1][i]:
            passed += 1
        else:
            print("error on {}th case".format(i))
            print("expected: {}, found: {}".format(test_cases[1][i], card_info.check_withdrawable(test_cases[0][i][0], test_cases[0][i][1])))
            test_with_error += 1
    print("{} / {} Passed".format(passed, total))

    # Test 6
    print("\n\nTEST 6: Withdraw")
    test_cases = [
        [
            [0, 1000],
            [1, 8000]
        ],
        [0, 2000]
    ]
    total = len(test_cases[0])
    passed = 0
    for i in range(len(test_cases[0])):
        card_info.withdraw(test_cases[0][i][0], test_cases[0][i][1])
        if card_info.see_balance(test_cases[0][i][0]) == test_cases[1][i]:
            passed += 1
        else:
            print("error on {}th case".format(i))
            print("expected: {}, found: {}".format(test_cases[1][i], card_info.see_balance(test_cases[0][i])))
            test_with_error += 1
    print("{} / {} Passed".format(passed, total))

    print("\n\nFinal Test Results:")
    if test_with_error == 0:
        print("All tests passed")
    else:
        print("{} errors found".format(test_with_error))