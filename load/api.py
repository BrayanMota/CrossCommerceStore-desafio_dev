from fastapi import APIRouter

load_router = APIRouter(tags=['Load'])


@load_router.get('/load/order/numbers')
def load_order_numbers():
    numbers = open('numbers_in_order.csv', 'r')
    return numbers.readlines()
