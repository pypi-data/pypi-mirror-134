"""Declares :class:`WebhookDispatcher`."""
import asyncio

from fastapi import Request
from fastapi.dependencies.utils import get_dependant

from .bodyconsumer import BodyConsumer


class WebhookDispatcher(BodyConsumer):
    """Dispatches webhook invocations and events to handlers."""

    def __init__(self, handlers: list = None):
        """Initialize a new :class:`WebhookDispatcher`.

        Args:
            handlers (list): the list of handlers that are matched
                against each event.
        """
        self.handlers = handlers

    async def dispatch(self, request: Request) -> None:
        """Collect all handlers for the webhook notification or
        event included in the request body, and run the results.
        """
        dto = await self.get_body(request)
        futures = []
        for handler_class in self.get_handlers(request, dto):
            futures.append(self.run_handler(handler_class, dto))
        return await asyncio.gather(futures)

    def get_handlers(self, request: Request, dto: dict) -> list:
        """Return the matching handlers for the (webhook) event
        included in the request body.
        """
        return [
            x for x in self.handlers
            if x.can_handle(request, dto)
        ]

    async def run_handler(self, handler_class: type, dto: dict) -> None:
        """Runs the given handler class with the incoming
        event.
        """
        dependant = get_dependant(
            path='/',
            call=handler_class(dto)
        )
