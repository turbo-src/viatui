# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory in the container to /app
WORKDIR /app

# Set the timezone
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

# Install any needed packages specified in requirements.txt
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata && apt-get install -y \
    gnome-screenshot \
    xvfb \
    x11vnc \
    fluxbox \
    python3 \
    python3-pip \
    curl \
    scrot \
    python3-tk \
    python3-dev

RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml .
COPY poetry.lock .

RUN ~/.local/bin/poetry install

# Set environment v   ariable
ENV DISPLAY=:1

# Make port 5900 available to the world outside this container
#EXPOSE 5900

# Run x11vnc when the container launches
#CMD Xvfb :1 -screen 0 1024x768x16 & x11vnc -display :1 -forever

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["/entrypoint.sh"]

# Default command to execute
CMD ["/bin/bash"]