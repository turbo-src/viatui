# viatui

## Overview

`viatui` is an experimental project exploring the integration of Large Language Models (LLMs) with UI testing. The project aims to leverage LLMs to analyze screenshots of UIs, perform actions like clicking, and report on the results. This approach is at the forefront of combining AI and UI testing. The concept isn't fully fleshed out yet.

## Experimental Nature

- The code in `viatui` is primarily pseudocode, serving to illustrate the conceptual framework.
- This project is a starting point for discussions and further development in AI-driven UI testing.

## Modules

- `move_cursor.py`: Demonstrates cursor movement based on grid positions.
- `screenshot_grid.py`: Captures and processes screenshots for analysis by LLMs.
- `more to come...`

## Documentation

- **Virtual Screen and Screenshot Guide**: Details on setting up virtual screens for capturing UI states.

## Vision

- Utilize LLMs to interpret UI elements from screenshots.
- Automate UI interactions based on LLM analysis.
- Develop methods for intelligent, automated UI testing.

## Usage

new X server instance on DISPLAY=:1

```
Xorg :1 -nolisten tcp&
```

```
xhost +
```

Remember to restrict permissions again with xhost - after you're done, as this command disables access control and can pose a security risk.

```
docker build -t viatui .
```

```
docker run -it \
    -m 512m \
    -e DISPLAY=:1 \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    --volume /var/run/dbus:/var/run/dbus \
    --volume $(pwd):/app \
    --privileged \
    viatui
```

```
docker exec -it <container_id> /bin/bash
```

```
google-chrome --no-sandbox --disable-dbus --disable-gpu --disable-software-rasterizer --disable-dev-shm-usage
```

If you don't run the disable flags (at least certain ones), you'll gets some errors related to graphics that prevent dynamic websites from loading (error code SIGTRAP)



## License

This project is licensed under the MIT License.

## Poetry Workflow

1. **Open a Terminal:** You'll need a command line interface to interact with Poetry.

2. **Navigate to Your Project Directory:** Use the `cd` command to navigate to your project directory. In your case, it would be `cd viatui`.

3. **Check the Virtual Environment:** Poetry creates a virtual environment for each project. You can check the status of the environment with `poetry env info`.

4. **Install Dependencies:** If you're starting your work for the first time or if you've added new dependencies to your `pyproject.toml` file, you should install them using `poetry install`.

5. **Run Your Scripts:** You can run your Python scripts within the virtual environment using `poetry run python script.py`. Replace `script.py` with the path to your script.

6. **Add or Update Dependencies:** If you need to add or update a dependency, you can use `poetry add package_name` or `poetry update package_name`. Replace `package_name` with the name of the package.

7. **Build Your Project:** Once you're ready, you can build your project using `poetry build`. This will create a distribution package that you can share or publish.

8. **Test Your Project:** If you have tests in your project, you can run them using `poetry run pytest` (or replace `pytest` with your test runner).

Remember, every time you start a new terminal session, you'll need to navigate to your project directory and activate the virtual environment. Poetry handles the activation for you when you use `poetry run`.

