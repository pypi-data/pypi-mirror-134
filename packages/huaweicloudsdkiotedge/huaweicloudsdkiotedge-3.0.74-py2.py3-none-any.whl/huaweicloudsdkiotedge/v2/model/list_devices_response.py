# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevicesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'devices': 'list[QueryDeviceSimplifyDto]',
        'count': 'int',
        'page_info': 'PageInfoDTO'
    }

    attribute_map = {
        'devices': 'devices',
        'count': 'count',
        'page_info': 'page_info'
    }

    def __init__(self, devices=None, count=None, page_info=None):
        """ListDevicesResponse - a model defined in huaweicloud sdk"""
        
        super(ListDevicesResponse, self).__init__()

        self._devices = None
        self._count = None
        self._page_info = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info

    @property
    def devices(self):
        """Gets the devices of this ListDevicesResponse.

        查询设备列表响应结构体

        :return: The devices of this ListDevicesResponse.
        :rtype: list[QueryDeviceSimplifyDto]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this ListDevicesResponse.

        查询设备列表响应结构体

        :param devices: The devices of this ListDevicesResponse.
        :type: list[QueryDeviceSimplifyDto]
        """
        self._devices = devices

    @property
    def count(self):
        """Gets the count of this ListDevicesResponse.

        满足查询条件的记录总数。

        :return: The count of this ListDevicesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDevicesResponse.

        满足查询条件的记录总数。

        :param count: The count of this ListDevicesResponse.
        :type: int
        """
        self._count = count

    @property
    def page_info(self):
        """Gets the page_info of this ListDevicesResponse.


        :return: The page_info of this ListDevicesResponse.
        :rtype: PageInfoDTO
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListDevicesResponse.


        :param page_info: The page_info of this ListDevicesResponse.
        :type: PageInfoDTO
        """
        self._page_info = page_info

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
        if not isinstance(other, ListDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
