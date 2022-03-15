from enum import Enum

from fastapi import APIRouter


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


asynchronous_router = APIRouter()

@asynchronous_router.get("/")
async def root():
    return {"message": "heloo World"}


@asynchronous_router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@asynchronous_router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@asynchronous_router.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@asynchronous_router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have Some residuals"}


