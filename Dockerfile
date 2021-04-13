FROM python

WORKDIR /app

COPY Input.py .
COPY pycalculator.py .

CMD ["python", "./Input.py"]
