#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    DropdownChoice,
)
from cmk.gui.plugins.wato import (
    HostRulespec,
    rulespec_registry,
)

try:
    from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import (
        RulespecGroupMonitoringAgentsAgentPlugins
    )
except Exception:
    RulespecGroupMonitoringAgentsAgentPlugins = None


def _valuespec_agent_config_list_local_admin_user():
    return DropdownChoice(
        title=_('List Local Administrator User'),
        help=_('This will deploy the agent plugin <tt>list_local_admin_user</tt> '
               'for display the user in the local Administrator Group.'),
        choices=[
            (True, _('Deploy List Local Admin User plugin')),
            (None, _('Do not deploy List Local Admin User plugin')),
        ],
    )


if RulespecGroupMonitoringAgentsAgentPlugins is not None:
    rulespec_registry.register(
        HostRulespec(
            group=RulespecGroupMonitoringAgentsAgentPlugins,
            name='list_local_admin_user',
            valuespec=_valuespec_agent_config_list_local_admin_user,
        ))