FROM python:3.10.4
COPY requests /requests
WORKDIR /requests
COPY ./requests/requirements.txt /requests/requirements.txt
# RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /requests/requirements.txt
COPY ./requests/requestTypes /requests/requestTypes
EXPOSE 8003
CMD ["uvicorn", "requestTypes.web.requestTypes_app:app", "--host=0.0.0.0" , "--reload" , "--port", "8003"]
