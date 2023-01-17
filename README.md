# 2FAinPython, An example for Two-Factor Authentication (2FA) in Python
### totp.py, time-based One-time Password (TOTP) is a time-based OTP. The seed for TOTP is static, just like in HOTP, but the moving factor in a TOTP is time-based rather than counter-based.
### hotp.py, each time the HOTP is requested and validated, the moving factor is incremented based on a counter. 
##### Inspired by https://blog.bytebytego.com/i/96603172/how-does-google-authenticator-or-other-types-of-factor-authenticators-work
##### https://www.onelogin.com/learn/otp-totp-hotp
#####  pip install pyotp pillow qrcode