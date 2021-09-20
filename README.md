# task-atm

## Installation Notes

### 1. Clone the repository
```
git clone https://github.com/hadh93/task-atm.git
```

### 2-1. Run main.py to have ATM code running.
```
python main.py
```

### 2-2. Run test.py to run unit tests per function.
```
python test.py
```


## main.py

In general, a user of this ATM device should follow the instruction provided by the prompt. 
All inputs/outputs are handled by the console.

Below is a brief explanation of what a user should enter for each input prompt you will see while running this program.

### 1. Please insert a card
After this prompt, the user needs to type two information of your card, separated by a space, as described below:  
- Type "True" to indicate that the card being inserted is flawless and functional.
- Followed by a space, type your full card number following the format: "dddd-dddd-dddd-dddd"
> After the validation process, this "insertion" will create a class named "CardInfo," which supports account-related methods that will take care of transactions.
> Users are forced to use dddd-dddd-dddd-dddd pattern, as the program is using RegEx (python re library) to validate it.

e.g.
```
True 1234-1234-1234-1234
```



#### 2. Please enter password:
- Type in password
- Justification for the current implementation:
```
Description specifies that the bank API "wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not."
Therefore, user password input is encrypted into SHA256 format and compared with the 'correct' password stored in SHA256 format.
The task hypothesized that the bank API would communicate and validate the password. 
But since I do not have access to the API, I hypothesized that I have a user/PW DB table in an encrypted form. 
I declared that variable as a two-dimensional list and named it 'bank_db.'
```
Registered account/pw information in the hypothetical bank db:
|account|password|balance-checking|balance-saving|
|------|---|---|---|
|1234-1234-1234-1234|1234|150|100|
|9999-9999-9999-9999|0000|1000|10000|

#### 3. Please select account:
- Type 1 to choose "Checking" account
- Type 2 to choose "Saving" account

#### 4. Please choose your action:
- Type 1 to choose "See Balance" option
- Type 2 to choose "Deposit" option
- Type 3 to choose "Withdraw" option

#### Optional: Insert the amount of money you would like to deposit/withdraw in dollar($)s:
- Only appears when you choose option "Deposit" or "Withdraw"
- If the balance is not enough to withdraw entered amount, it will throw an error.


## test.py

A total of 23 test cases was generated for six different functionalities written below:
1. Validation of the card being handled
2. Password validation
3. "See Balance" functionality
4. "Deposit" functionality
5. Checking if the amount entered is withdraw-able
6. "Withdraw" functionality
