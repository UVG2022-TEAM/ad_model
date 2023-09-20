import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("iso_forest_model.pkl")
data = pd.read_csv('parroquia.csv', parse_dates=['date'])
data = data[['date', 't1', 't2', 't3', 't4', 'h3', 'h4', 'f1', 'f2']]
data = data[data['date'] <= '2020-07-27 11:00:00']

def run():
    global data  
    st.title("Sensor Anomaly Detection")
    st.line_chart(data.set_index('date'))

    st.sidebar.header("Input new sensor data")
    t1 = st.sidebar.number_input("Sensor t1", value=0.0)
    t2 = st.sidebar.number_input("Sensor t2", value=0.0)
    t3 = st.sidebar.number_input("Sensor t3", value=0.0)
    t4 = st.sidebar.number_input("Sensor t4", value=0.0)
    h3 = st.sidebar.number_input("Sensor h3", value=0.0)
    h4 = st.sidebar.number_input("Sensor h4", value=0.0)
    f1 = st.sidebar.number_input("Sensor f1", value=0.0)
    f2 = st.sidebar.number_input("Sensor f2", value=0.0)

    if st.sidebar.button("Agregar y Detectar Anomalía"):
        new_data = pd.DataFrame([[data['date'].max() + pd.Timedelta(hours=1), t1, t2, t3, t4, h3, h4, f1, f2]], columns=data.columns)
        prediction = model.predict(new_data.drop(columns=['date']))
        if prediction[0] == -1:
            st.sidebar.write("The data is an anomaly.")
            data = pd.concat([data, new_data], axis=0)
            st.line_chart(data.set_index('date'))
            st.write("Anomaly detected at:", new_data['date'].values[0])
        else:
            st.sidebar.write("The data is normal.")
            data = pd.concat([data, new_data], axis=0)
            st.line_chart(data.set_index('date'))

if __name__ == '__main__':
    run()