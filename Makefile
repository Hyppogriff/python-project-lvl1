install:
	poetry install

prompt: install
	poetry add prompt

lint:
	poetry run flake8 brain_games
