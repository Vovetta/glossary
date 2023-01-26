from asyncio import run
from json import loads, dumps

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from fastapi.routing import APIRoute


GLOSSARY = {}

class IndentedJSONResponse(JSONResponse):
    def render(self, content: dict) -> bytes:
        return dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(",", ":"),
        ).encode("utf-8")


async def glossary(name = Query(None)):
    if name:
        return JSONResponse(GLOSSARY.get(name.lower(), "Данный термин не найден"))
    return IndentedJSONResponse(GLOSSARY)


async def mindmap():
    return FileResponse("mindmap.png")


def get_application():
    with open("glossary.json", "r+", encoding='utf-8') as file:
        GLOSSARY.update(loads(file.read()))

    app = FastAPI(routes=[
        APIRoute('/glossary', glossary, methods=['GET']),
        APIRoute('/mindmap', mindmap, methods=['GET'])
    ])
    return app


if __name__ == '__main__':
    config = Config()
    config.accesslog = '-'
    config.bind = f'0.0.0.0:8000'
    config.errorlog = '-'
    run(serve(get_application(), config))  # type: ignore
