import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data nutrisi buah-buahan
data_nutrisi = {
    'Buah': ['Apel', 'Pisang', 'Jeruk', 'Pir', 'Strawberry', 'Semangka', 'Mangga', 'Alpukat', 'Kurma', 'Anggur', 'Nanas', 'Kiwi', 'Rambutan', 'Pepaya', 'Lemon', 'Markisa', 'Kelapa', 'Durian', 'Salak'],
    'Serat (g)': [2.4, 2.6, 2.4, 2.4, 2.0, 0.4, 1.6, 6.7, 8.0, 0.9, 1.4, 2.1, 0.9, 1.7, 2.8, 2.4, 9.0, 3.8, 2.6],
    'Protein (g)': [0.3, 1.1, 0.9, 0.4, 0.7, 0.6, 0.8, 2.0, 2.2, 0.6, 0.5, 1.1, 0.9, 0.5, 1.1, 2.2, 3.3, 1.5, 0.6],
    'Lemak (g)': [0.2, 0.3, 0.2, 0.2, 0.3, 0.2, 0.4, 14.7, 0.2, 0.2, 0.1, 0.5, 0.2, 0.3, 0.3, 0.7, 33.5, 5.3, 0.7]
}

# Membuat DataFrame dari data nutrisi
df_nutrisi = pd.DataFrame(data_nutrisi)

# Mengatur kolom 'Buah' sebagai index DataFrame
df_nutrisi.set_index('Buah', inplace=True)

# Visualisasi data nutrisi menggunakan diagram batang
st.title('Visualisasi Data Nutrisi Buah-Buahan')
st.write("Berikut adalah visualisasi data nutrisi buah-buahan dalam bentuk diagram batang.")

# Memilih jenis nutrisi yang ingin divisualisasikan
jenis_nutrisi = st.radio("Pilih Jenis Nutrisi:", ('Serat', 'Protein', 'Lemak'))

# Mengambil data nutrisi sesuai dengan pilihan pengguna
data = df_nutrisi[jenis_nutrisi]

# Membuat diagram batang
fig, ax = plt.subplots()
data.plot(kind='bar', ax=ax, color=['skyblue', 'orange', 'green'])

# Menambahkan judul dan label sumbu
plt.title(f'Kandungan {jenis_nutrisi} dalam Buah-Buahan')
plt.xlabel('Buah')
plt.ylabel(f'{jenis_nutrisi} (g)')
plt.xticks(rotation=45)

# Menampilkan diagram batang
st.pyplot(fig)
# Sekarang lanjutkan dengan kode aplikasi Streamlit Anda seperti biasa



st.title('Kalkulator Kalori Buah')
st.write("Selamat datang di aplikasi kalkulator kalori buah. Pilih buah favorit Anda dan berapa beratnya, lalu kami akan memberi tahu Anda jumlah kalori yang terkandung.")
buah = st.selectbox('Pilih Buah', list(kalori_buah.keys()), format_func=lambda x: x.capitalize())

berat = st.slider('Berat (gram)', min_value=1, max_value=1000, value=100)



if st.button('Hitung Kalori'):
    kalori_total = (kalori_buah[buah]['kalori'] / 100) * berat
    st.write(f"Jumlah kalori dalam {berat} gram {buah} adalah: {kalori_total} kalori")
    st.write("Informasi Nutrisi:")
    st.write(f"- Serat: {kalori_buah[buah]['serat']}")
    st.write(f"- Protein: {kalori_buah[buah]['protein']}")
    st.write(f"- Lemak: {kalori_buah[buah]['lemak']}")
    st.write("Kandungan Vitamin:")
    for vitamin, nilai in kalori_buah[buah]['vitamin'].items():
        st.write(f"- {vitamin}: {nilai}")
    st.image(kalori_buah[buah]['gambar'], caption='Gambar ' + buah.capitalize())

# Tambahkan rekomendasi buah berdasarkan jumlah kalori yang dipilih
st.sidebar.title('Rekomendasi Buah Berdasarkan Kalori')
kalori_target = st.sidebar.slider('Pilih Jumlah Kalori', min_value=10, max_value=1000, value=100)
st.sidebar.write('Buah-buahan dengan kalori serupa:')
for buah, info in kalori_buah.items():
    if abs((info['kalori'] / 100) * berat - kalori_target) < 20:
        st.sidebar.write(f"- {buah.capitalize()}")



# Menambahkan judul aplikasi
st.title('KELOMPOK 1')

# Mendefinisikan URL musik yang akan diputar
url_musik = 'c:\\Users\\Bagas AL-Fikri\\Downloads\\The+Smiths+-+There+Is+A+Light+That+Never+Goes+Out+(Official+Audio) (1).mp3'  # Ganti dengan URL musik yang ingin Anda putar

# Menampilkan widget audio untuk memutar musik
st.audio(url_musik, format='audio/mp3')
