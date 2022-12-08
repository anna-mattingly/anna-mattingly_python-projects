from lib2to3.pygram import Symbols
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*().'

mix_str = lower + upper + numbers + symbols

password = ''.join(random.sample
                    (mix_str, 10))

print('Password: '+password)


