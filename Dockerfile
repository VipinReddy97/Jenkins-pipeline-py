FROM python

WORKDIR /app

COPY Calculator.py .
COPY pycalculator.py .

CMD ["python", "./Calculator.py"]
