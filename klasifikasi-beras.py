import pickle
import streamlit as st

model = pickle.load(open('klasifikasi-beras.sav', 'rb'))

st.title('Klasifikasi Jenis Beras Jamine / Gonen')

col1, col2 = st.columns(2)

with col1 :
    Area = st.number_input ('Berapa Nilai Luasnya?')
    MajorAxisLength = st.number_input ('Berapa Panjang Sumbu Utama?')
    MinorAxisLength = st.number_input ('Berapa Panjang Sumbu Minor?')
    Eccentricity = st.number_input ('Berapa Eksentrisitasnya?')
    ConvexArea = st.number_input ('Berapa Area Cembungnya?')

with col2 :
    EquivDiameter = st.number_input ('Berapa Diameter Ekuivalennya?')
    Extent = st.number_input ('Berapa Tingkat Perluasannya?')
    Perimeter = st.number_input ('Berapa Nilai Kelilingnya?')
    Roundness = st.number_input ('Berapa Nilai Kebulatannya?')
    AspectRation = st.number_input ('Berapa Nilai Aspek Rasionya?')

predict = ''

if st.button('Test'):
    prediction = model.predict([[Area,MajorAxisLength,MinorAxisLength,Eccentricity,
                                 ConvexArea,EquivDiameter,Extent,Perimeter,Roundness,AspectRation]])

    if predict == 1:
        predict ='Termasuk Kedalam Jenis Beras Jasmine'
    else:
        predict = 'Termasuk Kedalam Jenis Beras Gonen'

st.success(predict)
