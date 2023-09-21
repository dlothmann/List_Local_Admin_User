"""Check Evaluations"""

####
## List Local Admin Users
####
##
## Agent based part of List Local Admin User Script
##
## Version: 2.1.0
##
## Date: 2023-07-26
##
## Author: D. Lothmann

#Script for CheckMK Agent to List Local Admin Users
from itertools import chain
from .agent_based_api.v1 import Service, State, Result, register


def flatten_chain(matrix):
    """Flatten the given array from powershell"""
    return list(chain.from_iterable(matrix))

def discover_list_local_admin_user(section):
    """Service Discovery"""
    yield Service(item="Local Admin User")

def check_list_local_admin_user(item, section):
    """Evaluate the result from the check script"""

    crit = "Seems this is a Domain Controller. No Local Admin Group Available."
    warn = "No Group with SID S-1-5-32-544 found. Are you sure this is a windows system?"

    for line in section:
        if "3" in line[0]:
            yield Result(state=State.CRIT, summary=crit)
            return
        if "2" in line[0]:
            yield Result(state=State.Warn, summary=warn)
            return


    arr = flatten_chain(section)
    out = ''
    for string in arr:
        out += string
        out += " "

    yield Result(state=State.OK, summary=out)


register.check_plugin(

    name="list_local_admin_user",
    service_name="%s",
    discovery_function=discover_list_local_admin_user,
    check_function=check_list_local_admin_user,
)
