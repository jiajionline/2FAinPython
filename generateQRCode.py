import pyotp
import qrcode

key = "7FIURGESUSOMITHPFCXSUMQE34YBEO2D"

uri = pyotp.TOTP(key).provisioning_uri(name="your name", issuer_name = "your app")
print(uri)
# otpauth://totp/your%20app:your%20name?secret=7FIURGESUSOMITHPFCXSUMQE34YBEO2D&issuer=your%20app
qrcode.make(uri).save("qrcode_totp.png")

#scan the qrcode in your authenticator, it generates a one-time password every 30 seconds