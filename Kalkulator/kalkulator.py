# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Perkalian Matriks", layout="centered")

st.title("🧮 Kalkulator Perkalian Matriks")
st.markdown("""
Selamat datang! Aplikasi ini membantu kamu menghitung hasil **perkalian dua matriks**.
Pastikan jumlah **kolom Matriks A** sama dengan jumlah **baris Matriks B** agar bisa dikalikan.
""")

# Input ukuran matriks dari sidebar
st.sidebar.header("🔢 Ukuran Matriks")
baris_a = st.sidebar.number_input("Jumlah Baris Matriks A", min_value=1, max_value=5, value=2)
kolom_a = st.sidebar.number_input("Jumlah Kolom Matriks A", min_value=1, max_value=5, value=2)
baris_b = kolom_a  # Syarat agar matriks bisa dikalikan
kolom_b = st.sidebar.number_input("Jumlah Kolom Matriks B", min_value=1, max_value=5, value=2)

# Fungsi input matriks
def input_matriks(nama, baris, kolom):
    st.markdown(f"**Isi Matriks {nama} ({baris}×{kolom}):**")
    matriks = []
    for i in range(baris):
        cols = st.columns(kolom)
        baris_matriks = []
        for j in range(kolom):
            elemen = cols[j].number_input(f"{nama}[{i+1},{j+1}]", value=0.0, step=1.0, key=f"{nama}_{i}_{j}")
            baris_matriks.append(elemen)
        matriks.append(baris_matriks)
    return np.array(matriks)

# Input Matriks A dan B
st.subheader("🧷 Input Matriks A dan B")
matriks_a = input_matriks("A", baris_a, kolom_a)
matriks_b = input_matriks("B", baris_b, kolom_b)

# Tombol Hitung dan hasil perkalian
if st.button("🧮 Hitung Hasil Perkalian"):
    try:
        hasil = np.matmul(matriks_a, matriks_b)
        st.success("✅ Perkalian berhasil!")
        
        # Tampilkan hasil dalam bentuk tabel
        st.subheader("📊 Matriks A × B =")
        df_hasil = pd.DataFrame(hasil)
        st.dataframe(df_hasil.style.format("{:.2f}"), use_container_width=True)

        # Tampilkan visualisasi heatmap
        st.subheader("🎨 Visualisasi Matriks Hasil")
        fig, ax = plt.subplots()
        sns.heatmap(df_hasil, annot=True, fmt=".2f", cmap="YlGnBu", cbar=True, ax=ax)
        ax.set_title("Heatmap Hasil Matriks A × B")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")

# Catatan bawah
st.markdown("""
---
📚 **Catatan:**
- Perkalian matriks hanya bisa dilakukan jika jumlah **kolom Matriks A = baris Matriks B**.
""")
