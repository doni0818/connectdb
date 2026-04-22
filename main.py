import koneksi


conn = koneksi.get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM dim_mahasiswa")

for data in cursor.fetchall():
    print(data)