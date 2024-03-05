import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
hourly_df = pd.read_csv("hourly.csv")

# Mengonversi kolom 'dteday' ke dalam format datetime
hourly_df['dteday'] = pd.to_datetime(hourly_df['dteday'])

# Menentukan rentang tanggal yang valid dalam data
min_date = hourly_df['dteday'].min().date()
max_date = hourly_df['dteday'].max().date()

# Sidebar untuk memilih rentang tanggal
st.sidebar.title('Pilih Rentang Tanggal')
start_date = st.sidebar.date_input("Tanggal awal", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("Tanggal akhir", min_value=min_date, max_value=max_date, value=max_date)

# Mengonversi tanggal ke dalam format datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data berdasarkan rentang tanggal yang dipilih
filtered_data = hourly_df[(hourly_df['dteday'] >= start_date) & (hourly_df['dteday'] <= end_date)]

# Menghitung jumlah penyewaan sepeda per tanggal
daily_rentals = filtered_data.groupby('dteday')['count'].sum().reset_index()

# Visualisasi data jumlah penyewaan sepeda per tanggal
st.title('Visualisasi Jumlah Penyewaan Sepeda per Tanggal')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(daily_rentals['dteday'], daily_rentals['count'])
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
plt.xticks(rotation=45)
st.pyplot(fig)

# Menampilkan tabel data
st.title('Data Jumlah Penyewaan Sepeda per Tanggal')
st.dataframe(daily_rentals)
