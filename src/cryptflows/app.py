from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from litestar import Litestar



def create_app() -> Litestar:
    """Create ASGI application."""

    from litestar import Litestar
    from litestar.di import Provide

    #from app.config import app as config
    #from app.config import constants
    from cryptflows.config.base import get_settings
    #from app.domain.accounts import signals as account_signals
    #from app.domain.accounts.dependencies import provide_user
    #from app.domain.accounts.guards import auth
    #from app.domain.teams import signals as team_signals
    #from app.lib.dependencies import create_collection_dependencies
    #from app.server import openapi, plugins, routers

    #dependencies = {constants.USER_DEPENDENCY_KEY: Provide(provide_user)}
    #dependencies.update(create_collection_dependencies())
    CurrentSettings = get_settings()

    return Litestar(
        #route_handlers=[],
        #plugins=[],
    )