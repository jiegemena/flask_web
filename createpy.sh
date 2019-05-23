#!/bin/bash

virtualenv -p /usr/bin/python3 venv
venv/bin/python3 -m pip install --upgrade pip
mkdir .vscode
echo '''
{
    "python.pythonPath": "venv/bin/python3"
}
''' >> ./.vscode/settings.json
echo '''
#!/bin/bash
venv/bin/pip3 install -r ./requirements.txt
''' >> pipb.sh
chmod 777 ./pipb.sh