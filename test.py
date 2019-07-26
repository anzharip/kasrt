import models

warga = models.Warga()

# body = {
#     "username": "010100005",
#     "password": "john doe"
# }

# print(
#     warga.get(body)
# )

##

body = {
    "kdrw": "01",
    "kdrt": "02",
    "norumah": "103",
    "nokk": "10102",
    "nmkk": "john doe",
    "statustinggal": "kontrak",
    "pengurus": "0",
    "passwd": "john doe"
}



print(
    warga.post(body)
)