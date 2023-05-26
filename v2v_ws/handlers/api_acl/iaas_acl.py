# -*- coding: utf-8 -*-

from api.constants import (
    CHANNEL_API,
    CHANNEL_SESSION,
    ROLE_GLOBAL_ADMIN,
    ROLE_ZONE_ADMIN,
    ROLE_CONSOLE_ADMIN,
    ROLE_NORMAL_USER,
)
from constants import (
    ACTION_V2V_IAAS_DESCRIBE_IAAS_HYPER_NODES,
    ACTION_V2V_IAAS_DESCRIBE_IAAS_HYPER_NODES_PG_RULE
)

API_ACL_V2V_IAAS = {
    ACTION_V2V_IAAS_DESCRIBE_IAAS_HYPER_NODES: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    },
    ACTION_V2V_IAAS_DESCRIBE_IAAS_HYPER_NODES_PG_RULE: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    }
}
