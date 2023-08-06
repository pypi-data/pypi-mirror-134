#!/usr/bin/env python3
# Copyright (c) 2004-present Facebook All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from datetime import datetime
from psym.client import SymphonyClient
from psym.common.data_class import alarmFilter, alarmStatus
from psym.common.data_enum import Entity
from psym.exceptions import EntityNotFoundError

#from ..graphql.input.edit_alarm_filter_input import EditAlarmFilterInput
from ..graphql.input.add_alarm_filter_input import AddAlarmFilterInput
from ..graphql.mutation.add_alarm_filter import addAlarmFilter
#from ..graphql.mutation.edit_alarm_filter import editAlarmFilter
#from ..graphql.mutation.remove_alarm_filter import removeAlarmFilter
#from ..graphql.query.alarm_filteres import alarmFilteres
from psym.common.constant import PAGINATION_STEP
from typing import Any, Dict, Iterator, List, Optional




def add_alarm_filter(
    client: SymphonyClient, 
    name: str,
    networkResource: str,
    enable: bool,
    beginTime: datetime,
    endTime: datetime,
    reason: str,
    user: str,
    creationTime: datetime,
    alarmStatus: str
) -> alarmFilter:
    """This function adds Alarm Filter.

    :param name: Alarm Filter name
    :type name: str

    :return: alarmFilter object
    :rtype: :class:`~psym.common.data_class.alarmFilter`

    **Example 1**

    .. code-block:: python

        new_alarm_filters = client.add_alarm_filter(name="new_alarm_filter")

    **Example 2**

    .. code-block:: python

        new_alarm_filter = client.add_alarm_filter(
            name="alarm_filter",

        )
    """
    alarm_filter_input = AddAlarmFilterInput(
        name=name,
        networkResource=networkResource,
        enable=enable,
        beginTime=beginTime,
        endTime=endTime,
        reason=reason,
        user=user,
        creationTime=creationTime,
        alarmStatus=alarmStatus
        )
    result = addAlarmFilter.execute(client, input=alarm_filter_input)
    return alarmFilter(
        name=result.name, 
        id=result.id,
        networkResource=result.networkResource,
        enable=result.enable,
        beginTime=result.beginTime,
        endTime=result.endTime,
        reason=result.reason,
        user=result.user,
        creationTime=result.creationTime,
        alarmStatus=result.alarmStatus
        )


