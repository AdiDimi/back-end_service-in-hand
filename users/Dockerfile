FROM python:3.10.4 
COPY users /users
WORKDIR /users
COPY ./users/requirements.txt /users/requirements.txt
# RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /users/requirements.txt
COPY ./users/usersInfo /users/usersInfo
EXPOSE 8001
CMD ["uvicorn", "usersInfo.web.users_app:app", "--host=0.0.0.0" , "--reload" , "--port", "8001"]
