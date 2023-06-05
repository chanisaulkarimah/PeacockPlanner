import tkinter as tk
import sqlite3

def add_task(conn, task_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (name) VALUES (?)", (task_name,))
    conn.commit()
    cursor.close()

def create_task_interface(conn):
    # Membuat jendela Tkinter
    window = tk.Tk()
    window.title("Pengelola Tugas")

    # Fungsi untuk menangani tombol Tambah Tugas
    def handle_add_task():
        task_name = entry_task_name.get()
        if task_name:
            add_task(conn, task_name)
            # Lakukan tindakan lain setelah menambahkan tugas, misalnya menampilkan daftar tugas

    # Label dan input untuk nama tugas
    label_task_name = tk.Label(window, text="Nama Tugas:")
    label_task_name.pack()
    entry_task_name = tk.Entry(window)
    entry_task_name.pack()

    # Tombol Tambah Tugas
    button_add_task = tk.Button(window, text="Tambah Tugas", command=handle_add_task)
    button_add_task.pack()

    window.mainloop()
