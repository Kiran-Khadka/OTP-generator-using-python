# Author: Kiran Khadka

import random, math # import the essential libraries

def generateOTP ():
    digitsValue = "0123456789"
    OTPCode = ""

    for i in range(4): # this generate the OTP within range of 4 digits
        OTPCode += digitsValue [math.floor(random.random() * 10)]
    return OTPCode

if __name__ == "__main__":
    print ("Your OTP to login is: ",generateOTP())
    print ("\t***Please do not share it with anyone.****")