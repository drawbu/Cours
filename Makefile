PY_VENV = venv/bin


all: run

$(PY_VENV):
	@ python3 -m venv venv
	@ $(PY_VENV)/pip install -r requirements.txt

run: $(PY_VENV)
	@ $(PY_VENV)/pytest TD**/*.py

clean:
	@ rm -rf .pytest_cache
	@ rm -rf */.pytest_cache
	@ rm -rf */__pycache__
	@ rm -f .DS_Store


.PHONY: all run