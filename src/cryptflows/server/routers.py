from __future__ import annotations

from typing import TYPE_CHECKING

from cryptflows.domain.accounts.controllers import AccessController, UserController, UserRoleController
from cryptflows.domain.system.controllers import SystemController
from cryptflows.domain.tags.controllers import TagController
from cryptflows.domain.teams.controllers import TeamController, TeamMemberController
from cryptflows.domain.web.controllers import WebController

if TYPE_CHECKING:
    from litestar.types import ControllerRouterHandler
