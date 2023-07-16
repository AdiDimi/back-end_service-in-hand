FROM python:3.10.4-slim
COPY weekOpening /weekOpening
WORKDIR /weekOpening
COPY ./weekOpening/requirements.txt /weekOpening/requirements.txt
# RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /weekOpening/requirements.txt
COPY ./weekOpening/weekOpening /weekOpening/weekOpening
EXPOSE 8004
CMD ["uvicorn", "weekOpening.web.weekOpening_app:app", "--host=0.0.0.0" , "--reload" , "--port", "8004"]
