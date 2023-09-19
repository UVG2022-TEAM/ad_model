import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load the model
model = joblib.load("iso_forest_model.pkl")

# Load the dataset (assuming it's in the same directory)
data = pd.read_csv('parroquia.csv', usecols=['date', 't1', 't2', 't3', 't4', 'h3', 'h4', 'f1', 'f2'])
data['date'] = pd.to_datetime(data['date'])

# Filter data up to July 27 at 11 am
data = data[data['date'] <= '2020-07-27 11:00:00']

def plot_data(new_data=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    for idx, col in enumerate(data.columns[1:]):
        ax.plot(data['date'], data[col], label=col)
        if new_data is not None:
            ax.scatter(data['date'].iloc[-1] + pd.Timedelta(minutes=10*idx), new_data[col], color='red', s=100)
    ax.legend()
    st.pyplot(fig)

def run():
    st.title("Anomaly Detection with Isolation Forest")
    
    # Display the original data
    st.subheader("Sensor Data Over Time")
    plot_data()

    # Input fields for the sensors in a sidebar
    st.sidebar.subheader("Enter Test Data")
    t1 = st.sidebar.number_input("Sensor t1 Value")
    t2 = st.sidebar.number_input("Sensor t2 Value")
    t3 = st.sidebar.number_input("Sensor t3 Value")
    t4 = st.sidebar.number_input("Sensor t4 Value")
    h3 = st.sidebar.number_input("Sensor h3 Value")
    h4 = st.sidebar.number_input("Sensor h4 Value")
    f1 = st.sidebar.number_input("Sensor f1 Value")
    f2 = st.sidebar.number_input("Sensor f2 Value")
    
    if st.sidebar.button("Detect Anomaly"):
        test_data = {'t1': t1, 't2': t2, 't3': t3, 't4': t4, 'h3': h3, 'h4': h4, 'f1': f1, 'f2': f2}
        pred_arr = np.array(list(test_data.values()))
        preds = pred_arr.reshape(1, -1)
        prediction = model.predict(preds)
        if prediction == -1:
            st.write("The test data is detected as an anomaly!")
            plot_data(new_data=test_data)
        else:
            st.write("The test data is normal.")
            plot_data()

if __name__ == '__main__':
    run()





