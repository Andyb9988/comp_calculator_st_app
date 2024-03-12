FROM python:3.11

WORKDIR /compound_calc_app

COPY compound_interest_calculator.py /compound_calc_app/compound_interest_calculator.py
COPY comp_calculator_app.py /compound_calc_app/comp_calculator_app.py
COPY requirements.txt /compound_calc_app/requirements.txt
COPY di_caprio.gif /compound_calc_app/di_caprio.gif

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "comp_calculator_app.py"]