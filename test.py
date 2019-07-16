# import models

# saldokas = models.SaldoKas()

# body = {
#     "yearmonth": "2019-07"
# }

# total_pemasukan = saldokas.get_total_pemasukan(body)

# print(
#     int(total_pemasukan[0])
# )



# total_pengeluaran = saldokas.get_total_pengeluaran(body)

# print(
#     int(total_pengeluaran[0])
# )

bulandict = {
    "01": "jan", 
    "02": "feb", 
    "03": "mar", 
    "04": "apr", 
    "05": "mei", 
    "06": "jun", 
    "07": "jul", 
    "08": "agu", 
    "09": "sep", 
    "10": "okt", 
    "11": "nov", 
    "12": "des", 
}

tahunbulan = "2019-07"
tahun = tahunbulan.split("-")[0]
bulan = bulandict[tahunbulan.split("-")[1]]

print(
    tahun, bulan
)