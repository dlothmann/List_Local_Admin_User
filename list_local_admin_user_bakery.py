#!/usr/bin/env python3


from pathlib import Path

from .bakery_api.v1 import FileGenerator, OS, Plugin, register
from typing import Any,Dict

def get_list_local_admin_user(conf: Dict[str, Any]) -> FileGenerator:
    yield Plugin(base_os=OS.WINDOWS,
                 source=Path("List_Local_Admin_User.ps1"))

register.bakery_plugin(
    name="list_local_admin_user",
    files_function=get_list_local_admin_user,
)