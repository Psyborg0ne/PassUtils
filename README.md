# psy's Pass Utils
*A set of tools to generate and check password strength*

## Dependencies
(**NECESSARY** to copy generated passwords to clipboard)
`pip install pyperclip` 

## HOW TO RUN
*From inside the script folder run*
`python pass_utils.py` 

### Features
**Password Generator**
+ Generate random string (4 - 32 characters)
+ Specify what to include
  1. Lowercase
  2. Uppercase
  3. Digits
  4. Special characters (!@#$)
+ Copy to clipboard

**Password Tester**
+ Test any string (4 - 32 characters)
+ Show or hide password after you type it
+ View password stats
  1. Character Pool (26 for lowercase, 10 for digits, or combinations etc.)
  2. Password length
  3. Password entropy in bits (This tells you how strong your password is.)
  4. Possible passwords (How many unique passwords can exist with current pool.)
