import pyotp

#key = pyotp.random_base32()
#print(key)
key = "7FIURGESUSOMITHPFCXSUMQE34YBEO2D"

totp = pyotp.TOTP(key)
print(totp.now())

your_input_code = input("Your 2FA code:")
result = totp.verify(your_input_code)
print(result)
