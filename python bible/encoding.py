import base64

apiKey = "8db29daf20284c2b8f8b946f0f9adbb0"
apiSecret = "d03e36a0e5094e7a94016cf7480d832d"
Authenticiation = "{}:{}".format(apiKey, apiSecret)

# convert the authenticiation string into a utf-8 byte
byte = Authenticiation.encode("utf-8")

print("{} {}".format("Basic ", base64.b64encode(byte)))
