# Stepik Page Object

Selenium and pytest tests for the course's Oscar demo store. The four peer-review scenarios use the `need_review` marker.

Run in PowerShell from the project directory with Python and Chrome installed.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v --tb=line --language=en
.\.venv\Scripts\python.exe -m pytest -v --tb=line --language=en -m need_review
```

Selenium Manager resolves ChromeDriver. The default run uses headless Chrome. Pass `--headed` to display the browser. The registration scenarios create disposable accounts in the course demo store.
