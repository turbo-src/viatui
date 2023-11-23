# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory in the container to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    fluxbox \
    chromium-browser

# Make port 5900 available to the world outside this container
EXPOSE 5900

# Run x11vnc when the container launches
CMD Xvfb :0 -screen 0 1024x768x16 & x11vnc -display :0 -forever
