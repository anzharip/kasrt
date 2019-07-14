import models

warga = models.Warga("11", "john doe")

###

# print(warga.get())

# print(warga.verify_hash())

###

# body = {
#     "nmrt": "1", 
#     "norumah": "101", 
#     "nokk": "", 
#     "nmkk": "genghis khan", 
#     "statustinggal": "",
#     "pengurus": "0",
#     "password": "genghis khan"
# }

# print(warga.post(body))

###

# body = {
#     "norumah": "101", 
# }
# print(warga.delete(body))

# body = {
#     "nmrt": "1", 
#     "norumah": "101", 
#     "nokk": "", 
#     "nmkk": "genghis khan", 
#     "statustinggal": "",
#     "pengurus": "0"
# }

# print(warga.put(body))

###

body = {
    "norumah": "101", 
    "password": "genghis khan"
}

print(warga.put_password(body))