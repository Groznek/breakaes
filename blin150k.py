from Crypto.Cipher import AES
import base64

key = b"v6DoYyXT7Nys1lMdHTXOtLcqOBDYsMJW"
iv = b"ihkzZOUAidDm2reQ"
flag = "577876455a386f754c4e5755344564726a2b756e6c52515a4f6e397548464c364c656c35335168367841365269513d3d"
decrypt = AES.new(key, AES.MODE_CFB, iv)
txt = decrypt.decrypt(base64.b64decode(bytearray.fromhex(flag).decode())).decode("utf-8")
print(txt)