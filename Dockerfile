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

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "fastapi.railway.internal", "--port", "8000"]