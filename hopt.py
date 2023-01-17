import pyotp

key = "7FIURGESUSOMITHPFCXSUMQE34YBEO2D"
index = 0
hotp = pyotp.HOTP(key)

print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(99))

for _ in range(3):
    print(hotp.verify(input("Your 2FA code:"), index))
    index +=1