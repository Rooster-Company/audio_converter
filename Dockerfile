FROM python:3.10.15-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
#install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg

EXPOSE 8000

CMD ["python3", "main.py"]