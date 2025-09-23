from fastapi import FastAPI

app = FastAPI()

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b

def eh_par(num):
    return num % 2 == 0