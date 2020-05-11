from getpass import getpass
import re
from string import punctuation

def PasswordValidation(password):
    if len(password) not in range(5,11):
        return 'Password length is not between 5 to 10 Chars'
    special_Chars = [True for x in password if x in punctuation]
    if len(special_Chars) == 0:
        return 'Your password should have atleast one spl character'
    string_check = re.compile('[@&]')
    if (string_check.search(password) == None):
        return 'Atleast & Or @ Spl Character must present'
    nums = any(x.isdigit() for x in password)
    if not nums:
        return 'You should have atleast one number'
    chars = any(x.isalpha() for x in password)
    if not chars:
        return 'You should have atleast one Character'
    return f'You password:{password} is correct'

password = getpass("Enter your password here: ")
print(password)
print(PasswordValidation(password))
