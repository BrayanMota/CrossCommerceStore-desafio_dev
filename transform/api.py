from . import functions

from fastapi import APIRouter

transform_router = APIRouter(tags=['Transform'])


class Transform():

    @transform_router.get('/v1/transform')
    def transform():
        """Método que ordena todos os valores extraidos do processo de extração.

        Returns
        -------
        Retorna o tempo de execução do processo de ordenação.
        """
        return functions.transform()
