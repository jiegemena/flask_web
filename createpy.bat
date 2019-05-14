virtualenv venv
venv\\Scripts\\python -m pip install --upgrade pip
md ".vscode"
(
echo {
echo      "python.pythonPath": "venv\\Scripts\\python"
echo } 
) >> ./.vscode/settings.json
echo venv\\Scripts\\pip3 install -r ./requirements.txt >> pipb.bat
venv\\Scripts\\pip3 install -r ./requirements.txt

