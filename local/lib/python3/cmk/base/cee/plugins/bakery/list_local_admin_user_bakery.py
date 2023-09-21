"""Bakery module"""
#!/usr/bin/env python3


from pathlib import Path

from cmk.base.cee.plugins.bakery.bakery_api.v1 import FileGenerator, OS, Plugin, register

def get_list_local_admin_user() -> FileGenerator:
    """Import Local Script"""
    yield Plugin(base_os=OS.WINDOWS,
                 source=Path("List_Local_Admin_User.ps1"))

register.bakery_plugin(

    name="list_local_admin_user",
    files_function=get_list_local_admin_user,
)
