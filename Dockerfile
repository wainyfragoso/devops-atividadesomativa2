FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install "fastapi[standard]" uvicorn
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
CMD [ "uvicorn" , "app:app" , "fastapi", "--host" , "dev", "main.py", "--port", "80" ]

