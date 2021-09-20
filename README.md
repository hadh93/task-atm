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
All inputs/ouputs are handled by the console.

### 1. Please insert a card
After this prompt, the user needs to type two information of your card, separated by a space, as described below:  
- Type "True" to indicate that the card being inserted is flawless and functional.
- Followed by a space, type your full card number following the format: "dddd-dddd-dddd-dddd"
> After validation process, this "insertion" will create a class named "CardInfo", which supports account-related methods that will take care of transactions.

e.g.
```
True 1234-1234-1234-1234
```



#### 2. Please enter password:
- Type in password
```
Description specifies that the bank API "wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not."
Therefore, user password input is encrypted into SHA256 format and will be compared with the 'correct' password, which is also stored as SHA256 format.
The task hypothesized that the bank API would communicate and validate the password. 
But since I do not have the acess to the API, I hypothesized that I have a table of user/pw db in an encrypted form. 
I declared that variable as a two-dimensional list and named 'bank_db'.
```
Registered account/pw information in the hypothetical bank db:
|account|password|balance-checking|balance-saving|
|------|---|---|---|
|1234-1234-1234-1234|1234|150|100|
|9999-9999-9999-9999|0000|1000|10000|
