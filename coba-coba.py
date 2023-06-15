import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkcalendar import DateEntry

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
        self.label_stasiun_tujuan = ttk.Label(self.frame_input, text="Stasiun Tujuan:")
        self.label_stasiun_tujuan.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.stasiun_tujuan = ttk.Combobox(self.frame_input, values=self.get_station_data()[0])
        self.stasiun_tujuan.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_stasiun_akhir = ttk.Label(self.frame_input, text="Stasiun Akhir:")
        self.label_stasiun_akhir.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.stasiun_akhir = ttk.Combobox(self.frame_input, values=self.get_station_data()[1])
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
        self.label_konfirmasi = ttk.Label(self.frame_tiket, text="Konfirmasi Pesanan")
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

        self.tombol_kembali = ttk.Button(self.frame_tiket, text="Kembali", command=self.kembali_input)
        self.tombol_kembali.grid(row=5, columnspan=2, padx=10, pady=10, sticky="e")

        self.frame_tiket.pack()
    
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

        self.label_stasiun_tujuan_val.config(text=f"Stasiun Tujuan: {stasiun_tujuan_val}")
        self.label_stasiun_akhir_val.config(text=f"Stasiun Akhir: {stasiun_akhir_val}")
        self.label_tanggal_keberangkatan_val.config(text=f"Tanggal Keberangkatan: {tanggal_keberangkatan_val}")
        self.label_jumlah_penumpang_val.config(text=f"Jumlah Penumpang: {jumlah_penumpang_val}")
        self.label_kelas_val.config(text=f"Kelas: {kelas_val}")

        self.stasiun_tujuan.set("")
        self.stasiun_akhir.set("")
        self.kelas.set("")
        
        self.show_tiket_frame()
    
    def kembali_input(self):
        self.frame_tiket.pack_forget()
        self.show_input_frame()
    
    def show_input_frame(self):
        self.frame_input.pack()
    
    def show_tiket_frame(self):
        self.frame_input.pack_forget()
        self.frame_tiket.pack()

if __name__ == "__main__":
    app = TiketApp()
    app.mainloop()
