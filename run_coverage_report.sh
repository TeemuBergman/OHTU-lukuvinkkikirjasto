cd src
poetry run coverage run --branch -m pytest
poetry run coverage xml