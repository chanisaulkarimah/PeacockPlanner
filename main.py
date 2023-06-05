import tkinter as tk
import sqlite3
from getpass import getpass
from task_interface import create_task_interface

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
        label_login_error = tk.Label(window_login, text="Username atau password salah.")
        label_login_error.pack()

# Membuat jendela Tkinter untuk login
window_login = tk.Tk()
window_login.title("Login - Pengelola Tugas")

label_username = tk.Label(window_login, text="Username:")
label_username.pack()
entry_username = tk.Entry(window_login)
entry_username.pack()

label_password = tk.Label(window_login, text="Password:")
label_password.pack()
entry_password = tk.Entry(window_login, show="*")
entry_password.pack()

button_login = tk.Button(window_login, text="Login", command=login)
button_login.pack()

# Menjalankan aplikasi login
window_login.mainloop()

# Menutup koneksi ke database SQLite setelah aplikasi selesai
cursor.close()
conn.close()
