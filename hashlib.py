import re

encryption = 'd89%l++5r19o7W *o=l645le9H'
secretMsg = re.findall(r"[ A-z ]", encryption)

slicing = secretMsg [::-1]
decryption = "".join(slicing)

print (decryption)
