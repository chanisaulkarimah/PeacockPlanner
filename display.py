import tkinter as tk
import sqlite3

def display_tasks(conn, listbox_tasks):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()

    listbox_tasks.delete(0, tk.END)  # Menghapus item-item sebelumnya dari listbox

    for task in tasks:
        task_id = task[0]
        task_name = task[1]
        listbox_tasks.insert(tk.END, f"{task_id}: {task_name}")

def create_task_interface(conn):
    # Membuat jendela Tkinter
    window = tk.Tk()
    window.title("Pengelola Tugas")

    # Fungsi untuk menangani tombol Tampilkan Tugas
    def handle_display_tasks():
        display_tasks(conn, listbox_tasks)

    # Tombol Tampilkan Tugas
    button_display_tasks = tk.Button(window, text="Tampilkan Tugas", command=handle_display_tasks)
    button_display_tasks.pack()

    # Listbox untuk menampilkan daftar tugas
    listbox_tasks = tk.Listbox(window)
    listbox_tasks.pack()

    window.mainloop()
