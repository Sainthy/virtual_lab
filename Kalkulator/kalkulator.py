import matplotlib.pyplot as plt
import seaborn as sns

if st.button("🧮 Hitung Hasil Perkalian"):
    try:
        hasil = np.matmul(matriks_a, matriks_b)
        st.success("✅ Perkalian berhasil!")
        st.subheader("📊 Matriks A × B =")
        df_hasil = pd.DataFrame(hasil)
        st.dataframe(df_hasil.style.format("{:.2f}"), use_container_width=True)

        # 🔥 Visualisasi heatmap
        st.subheader("🎨 Visualisasi Matriks Hasil")
        fig, ax = plt.subplots()
        sns.heatmap(df_hasil, annot=True, fmt=".2f", cmap="YlGnBu", cbar=True, ax=ax)
        ax.set_title("Heatmap Hasil Matriks A × B")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan: {e}")
