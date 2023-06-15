import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector
from tkcalendar import DateEntry

# Fungsi untuk membuat koneksi ke database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="keretaapi"
        )
        print("Koneksi ke database berhasil!")
    except mysql.connector.Error as error:
        print("Error saat koneksi ke database:", error)
    return connection

app = tk.Tk()
app.resizable(50,50)

belakang = tk.StringVar()
depan = tk.StringVar()

#inputan
input=ttk.Frame(app)
input.pack(padx=10, pady=10, fill="x", expand=True)

# Label nama depan
nama_depan = ttk.Label(input, text="Username : ")
nama_depan.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Input nama depan
nama_depan_input = ttk.Entry(input, textvariable=depan)
nama_depan_input.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Label nama belakang
nama_belakang = ttk.Label(input, text="Password : ")
nama_belakang.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Input nama belakang
nama_belakang_input = ttk.Entry(input, textvariable=belakang, show="*")
nama_belakang_input.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Fungsi untuk insert data ke database
def insert_data(username, password, tanggal_lahir, no_telfon, email):
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            # Query SQL untuk insert data
            query = "INSERT INTO login (username, password, tanggal_lahir, no_hp, email) VALUES (%s, %s, %s, %s, %s)"
            # Parameter nilai yang akan diinsert
            values = (username, password, tanggal_lahir, no_telfon, email)
            # Eksekusi query SQL
            cursor.execute(query, values)
            # Commit perubahan ke database
            connection.commit()
            print("Data berhasil diinsert ke database!")
        except mysql.connector.Error as error:
            print("Error saat insert data ke database:", error)
        finally:
            # Tutup cursor dan koneksi
            cursor.close()
            connection.close()

# Frame regis
frame_regis = ttk.Frame()
# Label username
label_user = ttk.Label(frame_regis, text="Username:")
label_user.pack(padx=10, fill="x", expand=True)

# Input username
user = tk.StringVar()
user_input = ttk.Entry(frame_regis, textvariable=user)
user_input.pack(padx=10, fill="x", expand=True)

# Label tanggal lahir
label_tanggal_lahir = ttk.Label(frame_regis, text="Tanggal Lahir:")
label_tanggal_lahir.pack(padx=10, fill="x", expand=True)

# Input tanngaal lahir
ttl = tk.StringVar()
tanggal_input = ttk.Entry(frame_regis, textvariable=ttl)
tanggal_input.pack(padx=10, fill="x", expand=True)

# Label no hp
no_hp = ttk.Label(frame_regis, text="Nomer Handphone:")
no_hp.pack(padx=10, fill="x", expand=True)

no_hap = tk.StringVar()


def validate_input(input):
    # Memeriksa setiap karakter pada input
    for char in input:
        if not char.isdigit():
            return False
    return True

validate_command = (frame_regis.register(validate_input), '%P')

input_nomer = ttk.Entry(frame_regis, textvariable=no_hap, validate='key', validatecommand=validate_command)
input_nomer.pack(padx=10, fill="x", expand=True)

# Label email
label_email = ttk.Label(frame_regis, text="Email :")
label_email.pack(padx=10, fill="x", expand=True)

# Input email
email = tk.StringVar()
email_input = ttk.Entry(frame_regis, textvariable=email)
email_input.pack(padx=10, fill="x", expand=True)

# Label password
label_password = ttk.Label(frame_regis, text="Password:")
label_password.pack(padx=10, fill="x", expand=True)

# Input password
password = tk.StringVar()
input_password = ttk.Entry(frame_regis, textvariable=password, show='*')
input_password.pack(padx=10, fill="x", expand=True)

# Label konfirmasi password
label_confirm_password = ttk.Label(frame_regis, text="Konfirmasi Password:")
label_confirm_password.pack(padx=10, fill="x", expand=True)

# Input konfirmasi password
confirm_password = tk.StringVar()
input_confirm_password = ttk.Entry(frame_regis, textvariable=confirm_password, show='*')
input_confirm_password.pack(padx=10, fill="x", expand=True)

# Tombol Submit
def submit():
    if password.get() == confirm_password.get():
        # Password sesuai dengan konfirmasi password
        messagebox.showinfo("Informasi", "Registrasi berhasil!")
        
           # Insert data ke database
        insert_data(
            user.get(),
            password.get(),
            tanggal_input.get(),
            input_nomer.get(),
            email.get()
        )
           # Reset nilai inputan
        user_input.delete(0, "end")
        tanggal_input.delete(0, "end")
        input_nomer.delete(0, "end")
        email_input.delete(0, "end")
        password.set("")
        confirm_password.set("")
        # back to frame login
        frame_regis.pack_forget()  # Sembunyikan frame regis
        input.pack()  # Tampilkan kembali frame input (halaman login)
       
        
    else:
        # Password tidak sesuai dengan konfirmasi password
        # Tampilkan pesan kesalahan
        messagebox.showerror("Kesalahan", "Password tidak sama!")
        password.set("")
        confirm_password.set("")

tombol_submit = ttk.Button(frame_regis, text="Submit", command=submit)
tombol_submit.pack(pady=10)

# Tombol untuk kembali ke halaman login
def kembali_login():
    frame_regis.pack_forget()  # Sembunyikan frame regis
    input.pack()  # Tampilkan kembali frame input (halaman login)

btn_kembali = ttk.Button(frame_regis, text="Kembali ke Login", command=kembali_login)
btn_kembali.pack(pady=10)

def klik():
    # Ambil nilai dari inputan username dan password
    username = depan.get()
    password_value = belakang.get()

    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            # Query SQL untuk memeriksa username dan password
            query = "SELECT * FROM login WHERE username =%s AND password =%s"
            # Parameter nilai username dan password
            values = (str(username).strip(), str(password_value).strip())
            # Eksekusi query SQL
            cursor.execute(query, values)
            # Ambil hasil query
            result = cursor.fetchone()
            print(values)
            if result is not None:
                # Jika username dan password cocok
                messagebox.showinfo("Informasi", "Login berhasil!")
                # Alihkan tampilan ke frame tiket
                depan.set("")
                belakang.set("")
                # frame_tiket.pack()
                TiketApp()
                    
                input.pack_forget()
            else:
                # Jika username dan password tidak cocok
                user.set("")
                password.set("")
                messagebox.showerror("Kesalahan", "Username atau password salah!")
                
        except mysql.connector.Error as error:
            print("Error saat login:", error)
        finally:
            # Tutup cursor dan koneksi
            cursor.close()
            connection.close()


    # Alihkan tampilan ke frame regis
    frame_regis.pack()
    frame_regis.pack_forget()

# Sembunyikan frame regis saat awal
frame_regis.pack_forget()

def tampil_regis():
    # Sembunyikan frame input
    input.pack_forget()

    # Tampilkan frame regis
    frame_regis.pack()

 
class TiketApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Pemesanan Tiket")
        
        self.frame_input = ttk.Frame(self)
        self.frame_tiket = ttk.Frame(self)
        
        self.create_input_frame()
        self.create_tiket_frame()
        
        self.show_input_frame()
    
    def create_input_frame(self):
        stasiun_tujuan = tk.StringVar()
        self.label_stasiun_tujuan = ttk.Label(self.frame_input, text="Stasiun Tujuan:")
        self.label_stasiun_tujuan.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.stasiun_tujuan = ttk.Combobox(self.frame_input,textvariable=stasiun_tujuan, values=self.get_station_data()[0])
        self.stasiun_tujuan.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        stasiun_akhir = tk.StringVar()
        self.label_stasiun_akhir = ttk.Label(self.frame_input,text="Stasiun Akhir:")
        self.label_stasiun_akhir.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.stasiun_akhir = ttk.Combobox(self.frame_input,textvariable=stasiun_akhir ,values=self.get_station_data()[1])
        self.stasiun_akhir.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        
        self.label_tanggal_keberangkatan = ttk.Label(self.frame_input, text="Tanggal Keberangkatan:")
        self.label_tanggal_keberangkatan.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.tanggal_keberangkatan = DateEntry(self.frame_input, date_pattern="dd/mm/yyyy")
        self.tanggal_keberangkatan.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_jumlah_penumpang = ttk.Label(self.frame_input, text="Jumlah Penumpang:")
        self.label_jumlah_penumpang.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.jumlah_penumpang = ttk.Entry(self.frame_input)
        self.jumlah_penumpang.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.label_kelas = ttk.Label(self.frame_input, text="Kelas:")
        self.label_kelas.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.kelas = ttk.Combobox(self.frame_input, values=["Eksekutif", "Ekonomi", "Bisnis"])
        self.kelas.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.tombol_pesan = ttk.Button(self.frame_input, text="Pesan", command=self.pesan)
        self.tombol_pesan.grid(row=5, columnspan=2, padx=10, pady=10, sticky="w")

        self.frame_input.pack()

    def create_tiket_frame(self):
        self.label_konfirmasi = ttk.Label(self.frame_tiket, text="")
        self.label_konfirmasi.grid(row=0, columnspan=2, padx=10, pady=10)

        self.label_stasiun_tujuan_val = ttk.Label(self.frame_tiket, text="")
        self.label_stasiun_tujuan_val.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.label_stasiun_akhir_val = ttk.Label(self.frame_tiket, text="")
        self.label_stasiun_akhir_val.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.label_tanggal_keberangkatan_val = ttk.Label(self.frame_tiket, text="")
        self.label_tanggal_keberangkatan_val.grid(row=2, columnspan=2, padx=10, pady=5)

        self.label_jumlah_penumpang_val = ttk.Label(self.frame_tiket, text="")
        self.label_jumlah_penumpang_val.grid(row=3, columnspan=2, padx=10, pady=5)

        self.label_kelas_val = ttk.Label(self.frame_tiket, text="")
        self.label_kelas_val.grid(row=4, columnspan=2, padx=10, pady=5)

        self.label_harga_val = ttk.Label(self.frame_tiket, text="")
        self.label_harga_val.grid(row=5, columnspan=2, padx=10, pady=5)

        self.tombol_kembali = ttk.Button(self.frame_tiket, text="Kembali", command=self.kembali_input)
        self.tombol_kembali.grid(row=6, columnspan=2, padx=10, pady=10, sticky="w")

        self.frame_tiket.pack_forget()
    
    def get_station_data(self):
        stasiun_tujuan = ["JAKARTA", "SOLO", "SURABAYA", "BALI", "SEMARANG"]
        stasiun_akhir = ["BANDUNG", "SEMARANG", "YOGYAKARTA", "BIMA"]
        return stasiun_tujuan, stasiun_akhir
    
    def pesan(self):
        stasiun_tujuan_val = self.stasiun_tujuan.get()
        stasiun_akhir_val = self.stasiun_akhir.get()
        tanggal_keberangkatan_val = self.tanggal_keberangkatan.get()
        jumlah_penumpang_val = self.jumlah_penumpang.get()
        kelas_val = self.kelas.get()

        # Dictionary harga per pilihan
        harga = {
            "JAKARTA-BANDUNG": 100000,
            "JAKARTA-SEMARANG": 150000,
            "JAKARTA-YOGYAKARTA": 200000,
            "SOLO-BANDUNG": 250000,
            "SOLO-SEMARANG": 300000,
            "SOLO-YOGYAKARTA": 350000,
            "SURABAYA-BANDUNG": 400000,
            "SURABAYA-SEMARANG": 450000,
            "SURABAYA-YOGYAKARTA": 500000,
            "BALI-BANDUNG": 550000,
            "BALI-SEMARANG": 600000,
            "BALI-YOGYAKARTA": 650000,
            "JAKARTA-BIMA": 800000,  # Tambahkan kunci ini dengan harga yang sesuai
            "Eksekutif": 50000,
            "Ekonomi": 75000,
            "Bisnis": 100000
        }

        if f"{stasiun_tujuan_val}-{stasiun_akhir_val}" not in harga:
            print("Harga tidak tersedia untuk rute tersebut.")
            return

        harga_total = (harga[f"{stasiun_tujuan_val}-{stasiun_akhir_val}"] + harga[kelas_val]) * int(jumlah_penumpang_val)

        self.label_stasiun_tujuan_val.config(text=f"Stasiun Tujuan: {stasiun_tujuan_val}")
        self.label_stasiun_akhir_val.config(text=f"Stasiun Akhir: {stasiun_akhir_val}")
        self.label_tanggal_keberangkatan_val.config(text=f"Tanggal Keberangkatan: {tanggal_keberangkatan_val}")
        self.label_jumlah_penumpang_val.config(text=f"Jumlah Penumpang: {jumlah_penumpang_val}")
        self.label_kelas_val.config(text=f"Kelas: {kelas_val}")
        self.label_harga_val.config(text=f"Total: {harga_total}")

        self.insert_data_tiket(
            stasiun_tujuan_val,
            stasiun_akhir_val,
            tanggal_keberangkatan_val,
            jumlah_penumpang_val,
            kelas_val,
            harga_total
        )

        self.stasiun_tujuan.set("")
        self.stasiun_akhir.set("")
        self.kelas.set("")

        self.show_tiket_frame()

# Fungsi untuk insert data ke database
    # Fungsi untuk insert data ke database
    def insert_data_tiket(self, tujuan, akhir, tanggal, jumlah_penumpang, kelas, total):
        connection = create_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                # Query SQL untuk insert data
                query = "INSERT INTO pemesanan (tujuan, akhir, tanggal_keberangkatan, jumlah_penumpang, kelas, total) VALUES (%s, %s, %s, %s, %s, %s)"
                # Parameter nilai yang akan diinsert
                values = (tujuan, akhir, tanggal, jumlah_penumpang, kelas, total)
                # Eksekusi query SQL
                cursor.execute(query, values)
                # Commit perubahan ke database
                connection.commit()
                print("Data berhasil diinsert ke database!")
            except mysql.connector.Error as error:
                print("Error saat insert data ke database:", error)
            finally:
                # Tutup cursor dan koneksi
                cursor.close()
                connection.close()

    def kembali_input(self):
        self.frame_tiket.pack_forget()
        self.show_input_frame()
    
    def show_input_frame(self):
        self.frame_input.pack()
    
    def show_tiket_frame(self):
        self.frame_input.pack_forget()
        self.frame_tiket.pack()



# Tombol LOGIN
tombol_login = ttk.Button(input, text="LOGIN", command=klik)
tombol_login.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Tombol REGIS
tombol_regis = ttk.Button(input, text="REGIS", command=tampil_regis)
tombol_regis.grid(row=2, column=1, padx=10, pady=10, sticky="e")


app.mainloop()
