rd .publish  /s/Q
md .publish
copy app.py .publish\app.py
copy requirements.txt .publish\requirements.txt
copy config-pro.py .publish\config.py
copy gunicorn.conf.py .publish\gunicorn.conf.py
copy Dockerfile .publish\Dockerfile

md .publish\webCore
xcopy webCore .publish\webCore  /s/e
rd .publish\webCore\__pycache__ /s/Q

md .publish\key
xcopy key .publish\key /s/e

md .publish\entity
xcopy entity .publish\entity /s/e
rd .publish\entity\__pycache__ /s/Q

md .publish\area
xcopy area .publish\area /s/e
rd .publish\area\__pycache__ /s/Q

md .publish\appdata
xcopy db .publish\appdata /s/e