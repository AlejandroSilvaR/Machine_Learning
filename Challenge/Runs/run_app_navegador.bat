@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Starting Streamlit app...
streamlit run app_ui/streamlit_app.py

pause