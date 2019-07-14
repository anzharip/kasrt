import models

pengeluaran = models.Pengeluaran()

##

# print(pengeluaran.get_all())

##

# body = {
#     "kdpengeluaran": "2"
# }

# print(
#     pengeluaran.get(body)
# )

##

# body = {
#     "jumlah": "300000", 
#     "keterangan": "pagar kantor rt"
# }

# print(
#     pengeluaran.post(body)
# )

##

body = {
    "kdpengeluaran": "4"
}

print(
    pengeluaran.delete(body)
)