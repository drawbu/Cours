PY_VENV = venv/bin


all: run

$(PY_VENV):
	@ python3 -m venv venv
	@ $(PY_VENV)/pip install -r requirements.txt

run: $(PY_VENV)
	@ $(PY_VENV)/pytest TD**/*.py


.PHONY: all run