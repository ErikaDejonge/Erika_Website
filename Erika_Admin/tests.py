from django.test import TestCase
import random

# Create your tests here

def otp_generator(length):
    otp=''
    for _ in range(length):
        otp += str(random.randint(0,9))
    return  otp

print(otp_generator(5))



