# Getting the official python image
FROM python:3

# Specifying the directory where all commands should execute.
# This is like cd /usr/src/app
WORKDIR /usr/src/app

# Copying requirements.txt from your local machine to the Docker image
COPY requirements.txt ./

# Installing packages in the Docker image. This is the longest step.
# Docker caches the result of each command
# When you make a change to your code, it checks each step to see if there is a change
# It only reruns the part that has change
# If you copy all files first, then install the packages, Docker will redownload the packages each time you make a change to your code
RUN pip install --no-cache-dir -r requirements.txt

# Copying all files from your current directory on your machine to the working directory in the image
COPY . .

# The following is equivalent to uvicorn app.main:app --host 0.0.0.0 --port 8000
# Command to start app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port","8000"]