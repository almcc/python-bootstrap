# Python Bootstrap

Requires [asdf](https://asdf-vm.com/)

```bash
cookiecutter gh:almcc/python-bootstrap
cd <new_project>
asdf install # Install Python Version
python -m venv venv # Create a Virtual Env
source ./venv/bin/activate # Activate Virtual Env
pip install -r dev-requirements.txt -r requirements.txt # Install packages
inv update-requirements sync-venv # Update packages to latest and sync updates to the virtual environment
```

## Docs

- https://www.pyinvoke.org/
- https://github.com/jazzband/pip-tools
- https://black.readthedocs.io/en/stable/
