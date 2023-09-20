
# Instructions to Deploy the ad_model_app

## Prerequisites:
- Ensure Docker is installed and running on your machine.

## Deployment:

1. Navigate to the directory containing the `Dockerfile`.
2. Build the Docker image using the following command:

docker build -t ad_model_app .

3. To view all created images, use:

docker images

4. Run the application on port 8501 with:

docker run -p 8501:8501 ad_model_app


5. Open your browser and enter the following URL to access the application:

http://localhost:8501


6. To stop the container, Ctrl + C

# Instructions to Use the Anomaly Detection App

## Enter Data in the Left Sidebar

### Test a Normal Value

These values are only for testing and, due to domain knowledge, we know that they are within the normal range

- t1: 18.6
- t2: 24.0
- t3: 23.8
- t4: 25.4
- h3: 72.2
- h4: 83.9
- f1: 39.1
- f2: 37.8

### Test an Anomaly

These values are exemplary only and we know from domain knowledge that they typically represent behavior that precedes a critical failure of air conditioning units. It is encouraged to try more extreme values

- t1: 7.5
- t2: 17.20
- t3: 20.9
- t4: 15.4
- h3: 52.4
- h4: 74.5
- f1: 60.35
- f2: 61.09

## Click on "Add and Detect Anomaly".


## Interpret Results:

The app will display whether the data is an "anomaly" or "normal".
If it's an anomaly, it will be highlighted on the chart.



