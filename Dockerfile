FROM python:3.10.4-slim
COPY appointments /appointments
WORKDIR /appointments
COPY ./appointments/requirements.txt /appointments/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /appointments/requirements.txt
COPY ./appointments/Appointments /appointments/Appointments
EXPOSE 8002
CMD ["uvicorn", "Appointments.web.appointments_app:app", "--host=0.0.0.0" , "--reload" , "--port", "8002"]