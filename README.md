# psy's Pass Utils

![Pass Utils Main Menu](https://github.com/Psyborg0ne/PassUtils/blob/master/screens/menu.jpg "Main Menu")

>*A set of tools to generate and check password strength*


## Requirements
* `Python 3.8` *(Should be compatible with any version >= 3.6 )*
* `pip install pyperclip` (**NECESSARY** to copy generated passwords to clipboard)

## HOW TO RUN
*From inside the script folder run*
`python pass_utils.py` 


### Password Generator
![Pass Utils Generator](https://github.com/Psyborg0ne/PassUtils/blob/master/screens/generator.jpg "Password Generator")

+ Generate random string (4 - 32 characters)
+ Specify what to include
  1. Lowercase
  2. Uppercase
  3. Digits
  4. Special characters (!@#$)
+ Copy to clipboard



### Password Tester
![Pass Utils Tester](https://github.com/Psyborg0ne/PassUtils/blob/master/screens/tester.jpg "Password Tester")

+ Test any string (4 - 32 characters)
+ Show or hide password after you type it
+ View password stats
  1. Character Pool (26 for lowercase, 10 for digits, or combinations etc.)
  2. Password length
  3. Password entropy in bits (This tells you how strong your password is.)
  4. Possible passwords (How many unique passwords can exist with current pool.)
