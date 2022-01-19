from fastapi import APIRouter

from fastapi_pagination import Page, add_pagination, paginate

load_router = APIRouter(tags=['Load'])


@load_router.get('/v1/load', response_model=Page)
def load():
    """Método que retorna os todos os números com paginação.

    Returns
    -------
    Números ordenados.

    Raises
    ------
    e
    Retorna uma exceção caso ocorra durante esse processo, caso não tenha mais valores, retornara um array vazio.
    """
    try:
        numbers = open('numbers_in_order.csv', 'r', encoding="utf-8")
        return paginate(numbers.readlines())
    except Exception as e:
        raise e
    finally:
        numbers.close()


add_pagination(load_router)
