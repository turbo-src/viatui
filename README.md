# viatui

## Overview

`viatui` is an experimental project exploring the integration of Large Language Models (LLMs) with UI testing. The project aims to leverage LLMs (e.g. inference and/or embeddings using cosine similarity) to analyze screenshots of UIs, perform actions like clicking, and report on the results. This approach is at the forefront of combining AI and UI testing. The concept isn't fully fleshed out yet.

## Experimental Nature

- The code in `viatui` is experimental and demonstrated against the web extension for turbo-src.
- This project is a starting point for discussions and further development in AI-driven UI testing.
- The automated user actions and screenshots all happen in `scripts/container_screenshots.py`.
- Nix and docker are used crudely in order to create reproducible chromium environemnts.
- The ethos is 'get it to work, then optimize', so don't be alarmed by the insanely large docker images it prodocues, etc.

## Vision

- Utilize LLMs or embeddings to interpret UI elements from screenshots.
- Automate UI interactions based on LLM analysis.
- Develop methods that are at least an order of magnitude easier and more effective for UI testing.

## Issues to overcome

1. For whatever reason (e.g. dbus issues), you can't run viatui along with turbo-src in local mode. Turbosrc must be online.

2. For whatever reason, turbo-src buttons don't dynamically update (must refresh), possibly due to dbus issues.

3. Race conditions: a healthy delay between the launching of chromium and the starting of the script.

## Testing usage

You must allow viatui to due its tasks up to repo creation. After that, the backend e2e tests can be ran.

### Connecting instance

1. Comment out the create user and create repo test in `turbo-src/tsrc-test`

2. Run `./tsrc-dev init --testers`

### Locally

1. `turbosrc.config` must be in `router-client` mode.

2. Run `./tsrc-dev init`

3. In `viatui/scripts/container_screesnhot.py`, comment out everything beyond the creation of the repo.

4. Run `docker-compose build viatui`

5. Run `docker-compose run viatui`

#### Connecting instance

1. Run `./tsrc-dev start`

2. Run `./tsrc-dev test <username> <repo> run_tests

#### Locally

1. In `viatui/scripts/container_screesnhot.py`, comment everything except code to refresh page and screeshot.

2. Open the screenshot in `chromium-nix-screenshots/`

You want to capture screenshots as the tests move along.


## License

This project is licensed under the MIT License.
