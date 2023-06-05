import tkinter as tk
import sqlite3

def delete_task(conn, task_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    cursor.close()

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

    # Fungsi untuk menangani tombol Hapus Tugas
    def handle_delete_task():
        selected_task = listbox_tasks.get(tk.ACTIVE)
        if selected_task:
            task_id = selected_task.split(':')[0]
            delete_task(conn, task_id)
            display_tasks(conn, listbox_tasks)

    # Tombol Hapus Tugas
    button_delete_task = tk.Button(window, text="Hapus Tugas", command=handle_delete_task)
    button_delete_task.pack()

    # Listbox untuk menampilkan daftar tugas
    listbox_tasks = tk.Listbox(window)
    listbox_tasks.pack()

    # Tombol Tampilkan Tugas
    button_display_tasks = tk.Button(window, text="Tampilkan Tugas", command=lambda: display_tasks(conn, listbox_tasks))
    button_display_tasks.pack()

    window.mainloop()
