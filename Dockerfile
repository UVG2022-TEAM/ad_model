# Mention the base image 
FROM continuumio/anaconda3

# Copy the current folder structure and content to docker folder
COPY . /usr/ML/app

# Expose the port within docker 
EXPOSE 8501

# Set current working directory
WORKDIR /usr/ML/app

# Install Cython
RUN pip install Cython

# Install the required libraries
RUN pip install -r requirements.txt

#container start up command
CMD ["streamlit", "run", "app.py"]
