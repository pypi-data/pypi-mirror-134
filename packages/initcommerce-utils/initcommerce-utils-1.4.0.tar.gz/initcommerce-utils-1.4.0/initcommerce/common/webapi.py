from typing import Optional

import strawberry as graphql  # noqa: F401
import uvicorn as WebServer  # noqa: F401
from fastapi import APIRouter as Router  # noqa: F401
from fastapi import BackgroundTasks  # noqa: F401
from fastapi import Body  # noqa: F401
from fastapi import Query  # noqa: F401
from fastapi import FastAPI as WebApp  # noqa: F401
from fastapi import Request, Response  # noqa: F401
from fastapi.exceptions import HTTPException as _BaseHTTPException  # noqa: F401
from graphql import ValidationRule  # noqa: F401
from graphql.error import format_error as format_graphql_error
from strawberry.asgi import GraphQL as _GraphQLApp  # noqa: F401
from strawberry.extensions import AddValidationRules  # noqa: F401
from strawberry.http import GraphQLHTTPResponse
from strawberry.permission import BasePermission  # noqa: F401
from strawberry.types import ExecutionResult
from strawberry.types import Info as GraphQLInfo  # noqa: F401

from initcommerce.common import exceptions
from initcommerce.common.logger import get_logger

from .value_object import Enum, StrEnum

logger = get_logger(__package__)


class HTTPException(_BaseHTTPException):
    def __init__(self):
        pass


def graphql_enum(python_enum: Enum):
    return graphql.enum(
        StrEnum(python_enum.__name__, ((e.name, e.value) for e in python_enum))
    )


class GraphQLApp(_GraphQLApp):
    async def get_context(self, request: Request, response: Optional[Response] = None):
        ctx: dict = await super().get_context(request, response=response) or dict()

        # NOTE: the graphql library doesn't provide it on its own
        response.background = BackgroundTasks()

        ctx.update(background_tasks=response.background)

        return ctx

    async def process_result(
        self, request: Request, result: ExecutionResult
    ) -> GraphQLHTTPResponse:
        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors:
            if not all(
                map(
                    lambda err: isinstance(err, exceptions.InitCommerceBaseException),
                    result.errors,
                )
            ):
                logger.error(f"GraphQL error: {result.errors}")
            data["errors"] = [format_graphql_error(err) for err in result.errors]

        return data
