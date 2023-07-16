FROM python:3.10.4-slim
COPY generalSettings /generalSettings
WORKDIR /generalSettings
COPY ./generalSettings/requirements.txt /generalSettings/requirements.txt
# RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /generalSettings/requirements.txt
COPY ./generalSettings/generalSettings /generalSettings/generalSettings
EXPOSE 8005
CMD ["uvicorn", "generalSettings.web.generalSettings_app:app", "--host=0.0.0.0" , "--reload" , "--port", "8005"]
