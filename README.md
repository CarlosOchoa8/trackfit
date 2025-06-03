# Trackfit

The app for your training records and performance tracking.


### How to build API

### Pre requisites
- virtualenv with python 3.12 or above
- **poetry** instaled on your machine ([Install Poetry]((https://install.python-poetry.org))) OR ```pip install poetry``` into your virtualenv
- **Docker** / **Docker Compose** instaled on your machine ([Install Docker]((https://docs.docker.com/get-docker/)))


### Installation

<!-- 1. Open a terminal and activate your virtual env

2. Install dependencies from requirements.txt
    ```bash
    pip install --upgrade pip

    cd trackfit
    poetry install
    ``` -->
3. Set .env variable
    ```
        IMAGE_NAME=trackfit-service
    ```

### Building the Docker containers

Follow the next steps to build the python container:

1. Open a terminal.
2. Navigate to the directory of the project.
3. Run the following command:

    ```bash
    docker compose build --no-cache
    docker compose up -d 
    ```

    You can remove flag `-d` to show in terminal logs while container is running.

Now you can run the application on your localhost: http://localhost:80

#### Contributions
#### As were said, the project is in current development,therefore it is possible if you investigate on it, probably get any  kind of error or improvements areas. If that's the case, feel yourself free to contribute with your comments, features, issues or pull request. I'll take a look. Thanks!
