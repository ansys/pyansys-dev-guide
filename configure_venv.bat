@echo off
setlocal

python -m venv venv
pip install -r requirements_docs.txt
venv\Scripts\activate.bat
