from . import functions

from fastapi import APIRouter

extract_router = APIRouter(tags=['Extract'])


class Extract():

    @extract_router.get('/v1/extract')
    def extract():
        return functions.extract()
