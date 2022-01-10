@echo off
setlocal

python -m venv venv
pip install -r requirements_docs.txt
pip install -r requirements_style.txt
venv\Scripts\activate.bat
