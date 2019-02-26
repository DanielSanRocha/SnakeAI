setup:
	pip install -r requirements.txt
	pip install -r requirements.dev.txt

run_gunicorn:
	honcho start -f Procfile -e .env.local

test:
	PYTHONPATH=".:$PYTHONPATH" python -m pytest tests/*