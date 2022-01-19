from fastapi import APIRouter

load_router = APIRouter(tags=['Load'])


@load_router.get('/v1/load')
def load():
    try:
        numbers = open('numbers_in_order.csv', 'r')
        return numbers.readlines()
    except Exception as e:
        raise e
