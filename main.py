import tkinter as tk
import sqlite3
from getpass import getpass
from display import create_task_interface

# Membuat koneksi ke database SQLite
conn = sqlite3.connect("task_manager.db")
cursor = conn.cursor()

# Fungsi untuk memeriksa login pengguna
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Memeriksa login pengguna dengan membandingkan dengan data pengguna dalam database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        # Menutup jendela login dan melanjutkan dengan aplikasi setelah login berhasil
        window_login.destroy()
        create_task_interface(conn)
    else:
        # Menampilkan pesan kesalahan jika login gagal
        label_login_error = tk.Label(window_login, text="Username atau password salah.", font=("Cabin", 12), foreground="black")
        label_login_error.pack()

# Membuat jendela Tkinter untuk login
window_login = tk.Tk()
window_login.title("Login - Pengelola Tugas")

# Menambahkan gambar pada jendela login
photo = tk.PhotoImage(file="logo.jpg")
label = tk.Label(image=photo)
label.image = photo # must keep a reference, otherwise it will be garbage collected
label.pack()

# Menyesuaikan tampilan latar belakang dan font pada jendela login
window_login.configure(bg="#F9C784")
tk.Label(window_login, text="Masuk ke Pengelola Tugas", bg="#F9C784", fg="#ffffff", font=("Helvetica", 20)).pack(pady=10)

label_username = tk.Label(window_login, text="Username:", bg="#F9C784", fg="#ffffff", font=("Helvetica", 14))
label_username.pack()
entry_username = tk.Entry(window_login, font=("Helvetica", 14))
entry_username.pack()

label_password = tk.Label(window_login, text="Password:", bg="#F9C784", fg="#ffffff", font=("Helvetica", 14))
label_password.pack()
entry_password = tk.Entry(window_login, show="*", font=("Helvetica", 14))
entry_password.pack()

button_login = tk.Button(window_login, text="Login", command=login, bg="#065efb", fg="#ffffff", font=("Helvetica", 14))
button_login.pack(pady=10)

# Menjalankan aplikasi login
window_login.mainloop()

# Menutup koneksi ke database SQLite setelah aplikasi selesai
cursor.close()
conn.close()
