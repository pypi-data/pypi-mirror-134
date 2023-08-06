from typing import Type

from eyja.interfaces.db import BaseStorageModel
from eyja.errors import ObjectNotFoundError


async def get_for_user(
    model_cls: Type[BaseStorageModel],
    object_id: str,
    user: BaseStorageModel
) -> BaseStorageModel:
    items = await model_cls.find({
        'object_id': object_id,
        'user_id': user.object_id,
    })

    if len(items) < 1:
        raise ObjectNotFoundError(
            message=object_id,
        )

    return items[0]
