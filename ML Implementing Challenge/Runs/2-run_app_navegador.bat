@echo off
echo Creating virtual environment...
IF NOT EXIST "..\venv" (
    py -m venv ..\venv
) ELSE (
    echo Virtual environment already exists.
)

echo Activating virtual environment...
call ..\venv\Scripts\activate

echo Installing dependencies...
pip install -r ../requirements.txt

echo Training model and preparing app...
python ..\src\train.py

echo Starting Streamlit app...
streamlit run ../app_ui/streamlit_app.py

pause