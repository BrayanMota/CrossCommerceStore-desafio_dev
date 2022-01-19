from . import functions

from fastapi import APIRouter

import asyncio

extract_router = APIRouter(tags=['Extract'])


class Extract():

    @extract_router.get('/v1/extract')
    def extract():
        """Método de extração dos dados da API disponibilizada

        Returns
        -------
        Retorna o tempo de execução do processo de extração
        """
        return asyncio.run(functions.main())
