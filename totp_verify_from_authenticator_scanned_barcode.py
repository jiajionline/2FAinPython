import pyotp

#key = pyotp.random_base32()
#print(key)
key = "7FIURGESUSOMITHPFCXSUMQE34YBEO2D"

totp = pyotp.TOTP(key)
while True:
    print(totp.verify(input("Your 2FA:")))
