from fastapi import APIRouter

transform_router = APIRouter(tags=['Transform'])

class Transform():

    @transform_router.get('/v1/transform')
    def transform():
        return ''