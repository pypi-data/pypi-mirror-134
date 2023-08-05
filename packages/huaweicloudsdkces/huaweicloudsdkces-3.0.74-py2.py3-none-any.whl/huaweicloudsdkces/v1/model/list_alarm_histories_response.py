# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmHistoriesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alarm_histories': 'list[AlarmHistoryInfo]',
        'meta_data': 'MetaDataForAlarmHistory'
    }

    attribute_map = {
        'alarm_histories': 'alarm_histories',
        'meta_data': 'meta_data'
    }

    def __init__(self, alarm_histories=None, meta_data=None):
        """ListAlarmHistoriesResponse - a model defined in huaweicloud sdk"""
        
        super(ListAlarmHistoriesResponse, self).__init__()

        self._alarm_histories = None
        self._meta_data = None
        self.discriminator = None

        if alarm_histories is not None:
            self.alarm_histories = alarm_histories
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def alarm_histories(self):
        """Gets the alarm_histories of this ListAlarmHistoriesResponse.

        一条或者多条告警历史详细信息

        :return: The alarm_histories of this ListAlarmHistoriesResponse.
        :rtype: list[AlarmHistoryInfo]
        """
        return self._alarm_histories

    @alarm_histories.setter
    def alarm_histories(self, alarm_histories):
        """Sets the alarm_histories of this ListAlarmHistoriesResponse.

        一条或者多条告警历史详细信息

        :param alarm_histories: The alarm_histories of this ListAlarmHistoriesResponse.
        :type: list[AlarmHistoryInfo]
        """
        self._alarm_histories = alarm_histories

    @property
    def meta_data(self):
        """Gets the meta_data of this ListAlarmHistoriesResponse.


        :return: The meta_data of this ListAlarmHistoriesResponse.
        :rtype: MetaDataForAlarmHistory
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListAlarmHistoriesResponse.


        :param meta_data: The meta_data of this ListAlarmHistoriesResponse.
        :type: MetaDataForAlarmHistory
        """
        self._meta_data = meta_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAlarmHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
