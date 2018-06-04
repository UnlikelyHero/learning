import base64

apikey = "apikeyvalue"
apisecret = "apikeysecret"

string = "{}:{}".format(apikey, apisecret)

encoded = base64.b64encode(string.encode("utf-8"))

print(encoded)
