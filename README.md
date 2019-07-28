# KASRT
HTTP REST API PoC for KASRT written in Python 3. 

# To-do
* models.RukunTetangga [done]
* models.Warga [done]
* models.Pemasukan [done]
* models.Pengeluaran [done]
* models.Iuran [done]
* models.SaldoKas [done]
* resources.Login [done]
* resources.RukunTetangga [done]
* resources.Warga [done]
* resources.Pemasukan [done]
* resources.Pengeluaran [done]
* resources.Iuran [done]
* resources.SaldoKas [done]
* Auth & Permission for resources.RukunTetangga [done]
* Auth & Permission for resources.Warga [done]
* Auth & Permission for resources.Pemasukan [done]
* Auth & Permission for resources.Pengeluaran [done]
* Auth & Permission for resources.Iuran [done]
* Auth & Permission for resources.SaldoKas [done]

# Endpoint List
| No. | Endpoint     | Method | Require JWT | Only for Pengurus |
|-----|--------------|--------|-------------|-------------------|
| 1   | /login       | POST   | No          | No                |
| 2   | /warga       | GET    | Yes         | Yes               |
| 3   | /warga       | POST   | Yes         | Yes               |
| 4   | /warga       | PUT    | Yes         | Yes               |
| 5   | /warga       | DELETE | Yes         | Yes               |
| 6   | /pemasukan   | GET    | Yes         | No                |
| 7   | /pemasukan   | POST   | Yes         | No                |
| 8   | /pemasukan   | PUT    | Yes         | Yes               |
| 9   | /pemasukan   | DELETE | Yes         | Yes               |
| 10  | /pengeluaran | GET    | Yes         | No                |
| 11  | /pengeluaran | POST   | Yes         | Yes               |
| 12  | /pengeluaran | DELETE | Yes         | Yes               |
| 13  | /iuran       | GET    | Yes         | No                |
| 14  | /iuran       | POST   | Yes         | Yes               |
| 15  | /iuran       | DELETE | Yes         | Yes               |
| 16  | /saldokas    | GET    | Yes         | No                |
| 17  | /saldokas    | POST   | Yes         | Yes               |
| 18  | /saldokas    | DELETE | Yes         | Yes               |

# To use: 
1. Clone the repo. 

```git clone https://github.com/anzharip/kasrt.git```

2. Enter the directory, create virtual environment. 

```cd kasrt```

```python3 -m venv env```

3. Activate virtual environment. 

```
source env/bin/activate
```

4. Install dependencies. 

```python3 -m pip install -r requirements.txt```

5. Configure the DB connection. 

```vi config.py```

6. Run the app. 

```./env/bin/gunicorn --bind 0.0.0.0:5000 wsgi:app```

# config.py Example

```
# Database host
DBHOST = "localhost"

# Database user credential
DBUSER = "username"

# Database password credential
DBPASS = "password"

# Database name
DBNAME = "app"

# Database post
DBPORT = 3306

# Flask secret key for session signing
SECRET_KEY = "somesecret"

# Flask-JWT-Extended key for token signing
JWT_SECRET_KEY = "somejwtsecret"

# Flask-JWT-Extended token expiration in second
JWT_ACCESS_TOKEN_EXPIRES = 900
```
