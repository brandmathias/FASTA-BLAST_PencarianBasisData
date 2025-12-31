import tkinter as tk
from tkinter import messagebox

# Dummy database DNA
database_sequences = {
    "SeqA": "ATCGTACCGTTA",
    "SeqB": "GTACGTACGGGA",
    "SeqC": "TTTACCGTAGGA",
    "SeqD": "ATCGTAGGGTTA"
}

def simple_blast(query, subject):
    length = min(len(query), len(subject))
    match_count = sum(1 for i in range(length) if query[i] == subject[i])
    return match_count / length * 100

def cari_similarity():
    query = entry_query.get().upper()
    if not query:
        messagebox.showwarning("Perhatian", "Masukkan sekuens DNA.")
        return

    result_text.config(state="normal")  # buka dulu
    result_text.delete("1.0", tk.END)
    for name, sequence in database_sequences.items():
        similarity = simple_blast(query, sequence)
        result_text.insert(tk.END, f"{name}: {similarity:.2f}% match\n")
    result_text.config(state="disabled")  # kunci lagi setelah selesai

# Setup window
window = tk.Tk()
window.title("Aplikasi BLAST Simple | Bioinformatika 2025")
window.geometry("600x520")
window.configure(bg="#F8F9F9")

# Title Header
tk.Label(window, text="BLAST Simple Approximate Matching", font=("Segoe UI", 20, "bold"), bg="#F8F9F9", fg="#1B4F72").pack(pady=10)
tk.Label(window, text="Bioinformatika Universitas Sam Ratulangi 2025", font=("Segoe UI", 12), bg="#F8F9F9", fg="#34495E").pack(pady=2)

# Input Frame
frame_input = tk.Frame(window, bg="#F8F9F9")
frame_input.pack(pady=20)

tk.Label(frame_input, text="Masukkan Query Sekuens DNA:", font=("Segoe UI", 12, "bold"), bg="#F8F9F9").pack()
entry_query = tk.Entry(frame_input, font=("Segoe UI", 14), width=40, bd=2, relief="groove")
entry_query.pack(pady=8)

tk.Button(frame_input, text="Cari Kemiripan", command=cari_similarity, bg="#2980B9", fg="white",
          font=("Segoe UI", 12, "bold"), padx=12, pady=5, relief="ridge").pack()

# Hasil Frame
frame_result = tk.Frame(window, bg="#F8F9F9")
frame_result.pack(pady=20)

tk.Label(frame_result, text="Hasil Similarity (%) :", font=("Segoe UI", 12, "bold"), bg="#F8F9F9", fg="#2C3E50").pack(pady=5)
result_text = tk.Text(frame_result, height=7, width=50, font=("Consolas", 12), bg="#FBFCFC", bd=2, relief="sunken", state="disabled")
result_text.pack()

# Nama Anggota Kelompok
frame_kelompok = tk.Frame(window, bg="#F8F9F9")
frame_kelompok.pack(pady=10)

tk.Label(frame_kelompok, text="Kelompok Bioinformatika TIK3012 Kelompok 3 2025 :", font=("Segoe UI", 12, "bold"), bg="#F8F9F9", fg="#1B4F72").pack(pady=3)

anggota = """1. SAVIO HENDRIKO PALENDENG        - 220211060043
2. VICTOR OBETNEGO SENDUK            - 220211060187
3. BRANDO MATHIAS ZUSRIADI          - 220211060351
4. NATHANAEL MICHAEL TUWAIDAN - 220211060369
5. YEFTA YOSIA ASYEL                           - 220211060372"""
tk.Label(frame_kelompok, text=anggota, font=("Segoe UI", 11), bg="#F8F9F9", justify="left").pack()

# Footer
tk.Label(window, text="© 2025 Bioinformatics Tools | Universitas Sam Ratulangi", bg="#F8F9F9",
         font=("Segoe UI", 9), fg="#85929E").pack(pady=5)

window.mainloop()
