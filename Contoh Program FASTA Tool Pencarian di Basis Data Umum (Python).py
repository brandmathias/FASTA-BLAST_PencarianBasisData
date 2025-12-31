import tkinter as tk
from tkinter import messagebox

# Dummy database
database_sequences = {
    "DNA": {
        "SeqA": "ATCGTACCGTTA",
        "SeqB": "GTACGTACGGGA"
    },
    "RNA": {
        "SeqX": "AUCGAUCGGAUU",
        "SeqY": "GUACGUACGGGA"
    },
    "Protein": {
        "Prot1": "MVKVGVNGFGRIGRLVTRAAF",
        "Prot2": "GGGIMVKGVNGRRLVTAAAF"
    }
}

# FASTA match: longest substring match length
def fasta_match(query, subject):
    max_match = 0
    q_len = len(query)

    for i in range(q_len):
        for j in range(i+1, q_len+1):
            substring = query[i:j]
            if substring in subject:
                if len(substring) > max_match:
                    max_match = len(substring)
    return max_match

def cari_similarity():
    query = entry_query.get().upper()
    seq_type = jenis_var.get()

    if not query:
        messagebox.showwarning("Perhatian", "Masukkan sekuens terlebih dahulu.")
        return

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)

    if seq_type not in database_sequences:
        result_text.insert(tk.END, "Jenis sekuens belum dipilih.")
        result_text.config(state="disabled")
        return

    for name, sequence in database_sequences[seq_type].items():
        match_length = fasta_match(query, sequence)
        similarity_score = match_length / len(query) * 100
        result_text.insert(tk.END, f"{name}: {similarity_score:.2f}% match (max substring: {match_length})\n")

    result_text.config(state="disabled")

# GUI Window
window = tk.Tk()
window.title("FASTA Simple Approximate Matching | Bioinformatika 2025")
window.geometry("650x560")
window.configure(bg="#F8F9F9")

# Title Header
tk.Label(window, text="🔬 FASTA Simple Approximate Matching", font=("Segoe UI", 20, "bold"), bg="#F8F9F9", fg="#1B4F72").pack(pady=10)
tk.Label(window, text="Bioinformatika Universitas Sam Ratulangi 2025", font=("Segoe UI", 12), bg="#F8F9F9", fg="#34495E").pack()

# Garis
tk.Label(window, text="─" * 120, bg="#F8F9F9", fg="#AAB7B8").pack(pady=5)

# Pilihan Jenis Sekuens
frame_jenis = tk.Frame(window, bg="#F8F9F9")
frame_jenis.pack(pady=5)

jenis_var = tk.StringVar()
jenis_var.set("DNA")

tk.Label(frame_jenis, text="Pilih Jenis Sekuens:", font=("Segoe UI", 12, "bold"), bg="#F8F9F9").pack()
tk.Radiobutton(frame_jenis, text="DNA", variable=jenis_var, value="DNA", font=("Segoe UI", 11), bg="#F8F9F9").pack(side="left", padx=10)
tk.Radiobutton(frame_jenis, text="RNA", variable=jenis_var, value="RNA", font=("Segoe UI", 11), bg="#F8F9F9").pack(side="left", padx=10)
tk.Radiobutton(frame_jenis, text="Protein", variable=jenis_var, value="Protein", font=("Segoe UI", 11), bg="#F8F9F9").pack(side="left", padx=10)

# Input Query
frame_input = tk.Frame(window, bg="#F8F9F9")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Masukkan Query Sekuens:", font=("Segoe UI", 12, "bold"), bg="#F8F9F9").pack()
entry_query = tk.Entry(frame_input, font=("Segoe UI", 14), width=40, bd=2, relief="groove")
entry_query.pack(pady=5)

tk.Button(frame_input, text="Cari Similarity", command=cari_similarity, bg="#2980B9", fg="white",
          font=("Segoe UI", 12, "bold"), padx=12, pady=5, relief="ridge").pack(pady=5)

# Hasil Similarity
frame_result = tk.Frame(window, bg="#F8F9F9")
frame_result.pack(pady=10)

tk.Label(frame_result, text="Hasil Similarity Matching :", font=("Segoe UI", 12, "bold"), bg="#F8F9F9", fg="#2C3E50").pack(pady=5)
result_text = tk.Text(frame_result, height=7, width=55, font=("Consolas", 12), bg="#FBFCFC", bd=2, relief="sunken", state="disabled")
result_text.pack()

# Anggota Kelompok
frame_kelompok = tk.Frame(window, bg="#F8F9F9")
frame_kelompok.pack(pady=5)

tk.Label(frame_kelompok, text="👥 Kelompok Bioinformatika 2025 :", font=("Segoe UI", 12, "bold"), bg="#F8F9F9", fg="#1B4F72").pack(pady=3)
anggota = """1. SAVIO HENDRIKO PALENDENG  - 220211060043
2. VICTOR OBETNEGO SENDUK     - 220211060187
3. BRANDO MATHIAS ZUSRIADI    - 220211060351
4. NATHANAEL MICHAEL TUWAIDAN - 220211060369
5. YEFTA YOSIA ASYEL          - 220211060372"""
tk.Label(frame_kelompok, text=anggota, font=("Segoe UI", 11), bg="#F8F9F9", justify="left").pack()

# Footer
tk.Label(window, text="© 2025 Bioinformatics Tools | Universitas Sam Ratulangi", bg="#F8F9F9",
         font=("Segoe UI", 9), fg="#85929E").pack(pady=5)

window.mainloop()
