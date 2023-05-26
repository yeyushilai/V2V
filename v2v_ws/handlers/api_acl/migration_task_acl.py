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
    ACTION_V2V_MIGRATION_TASK_CREATE_MIGRATION_TASK,
    ACTION_V2V_MIGRATION_TASK_UPDATE_MIGRATION_TASK,
    ACTION_V2V_MIGRATION_TASK_DELETE_MIGRATION_TASK,
    ACTION_V2V_MIGRATION_TASK_DESCRIBE_MIGRATION_TASK,
    ACTION_V2V_MIGRATION_TASK_DETAIL_MIGRATION_TASK,
    ACTION_V2V_MIGRATION_TASK_DESCRIBE_MIGRATION_VM
)

API_ACL_V2V_MIGRATION_TASK = {
    ACTION_V2V_MIGRATION_TASK_CREATE_MIGRATION_TASK: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    },
    ACTION_V2V_MIGRATION_TASK_UPDATE_MIGRATION_TASK: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    },
    ACTION_V2V_MIGRATION_TASK_DELETE_MIGRATION_TASK: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    },
    ACTION_V2V_MIGRATION_TASK_DESCRIBE_MIGRATION_TASK: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    },
    ACTION_V2V_MIGRATION_TASK_DETAIL_MIGRATION_TASK: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    },
    ACTION_V2V_MIGRATION_TASK_DESCRIBE_MIGRATION_VM: {
        CHANNEL_API: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                      ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
        CHANNEL_SESSION: [ROLE_GLOBAL_ADMIN, ROLE_NORMAL_USER,
                          ROLE_CONSOLE_ADMIN, ROLE_ZONE_ADMIN],
    }
}
