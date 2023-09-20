
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





