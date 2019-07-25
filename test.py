import models

warga = models.Warga()

body = {
    "username": "010100005",
    "password": "john doe"
}

print(
    warga.get(body)
)