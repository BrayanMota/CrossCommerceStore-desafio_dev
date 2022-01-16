from fastapi import FastAPI

app = FastAPI()


@app.get('/load/order/numbers')
def load_order_numbers():
    numbers = open('numbers.csv', 'r')
    return numbers
