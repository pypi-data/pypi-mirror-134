"""Declares :class:`WebhookReceiver`."""
from fastapi import Request
from fastapi.responses import JSONResponse
from unimatrix.lib.datastructures import ImmutableDTO

from .service import Service
#from .webhookdispatcher import WebhookDispatcher


class WebhookReceiver(Service):
    """A :class:`~unimatrix.ext.webapi.Service` implementation
    that configures itself to handle webhooks through a single
    entry point, accepting webhooks/events as JSON objects.
    """

    def __init__(self, *args, **kwargs):
        #self.dispatcher = WebhookDispatcher(
        #    handlers=kwargs.pop('handlers', []),
        #)
        super().__init__(*args, **kwargs)

    async def handle(self, request: Request, dto: dict) -> JSONResponse:
        print(dto)
        return JSONResponse(
            content={
                'handlers': [],
                'accepted': True,
                'message': dto
            },
            status_code=202
        )
        #return JSONResponse(
        #    content=await self.dispatcher.dispatch(
        #        request=request,
        #        dto=ImmutableDTO.fromdict(await request.json())
        #    ),
        #    status_code=202
        #)

    def setup_routes(self, urlconf: str) -> None:
        """Override :meth:`Service.setup_routes()` to do nothing,
        the :class:`WebhookReceiver` exposes a single endpoint.
        """
        self.add_api_route(
            '/',
            self.handle,
            name='entrypoint',
            status_code=202,
            tags=['Webhooks'],
            methods=['POST'],
            response_description="Confirmation of the event received."
        )
