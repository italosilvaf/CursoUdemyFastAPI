from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)

"""
'''Italo'''
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc5NjAwMjUyLCJpYXQiOjE2Nzg5OTU0NTIsInN1YiI6IjEifQ.lTTNVpuQiQXKDL9rnZmU1KytF0Srwaj8f8y29TELW00
Tipo: bearer

'''Giovanna'''
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjc5NjAyMDIyLCJpYXQiOjE2Nzg5OTcyMjIsInN1YiI6IjIifQ.g1VGKaL9zZp_9QB2F6nW857o4CTLisKq_qUPx0mFlco
Tipo: bearer
"""
