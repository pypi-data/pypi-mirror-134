# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceInfoSimple:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'device_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'device_name': 'device_name'
    }

    def __init__(self, id=None, device_name=None):
        """DeviceInfoSimple - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._device_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if device_name is not None:
            self.device_name = device_name

    @property
    def id(self):
        """Gets the id of this DeviceInfoSimple.

        设备ID

        :return: The id of this DeviceInfoSimple.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceInfoSimple.

        设备ID

        :param id: The id of this DeviceInfoSimple.
        :type: int
        """
        self._id = id

    @property
    def device_name(self):
        """Gets the device_name of this DeviceInfoSimple.

        设备名称

        :return: The device_name of this DeviceInfoSimple.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this DeviceInfoSimple.

        设备名称

        :param device_name: The device_name of this DeviceInfoSimple.
        :type: str
        """
        self._device_name = device_name

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
        if not isinstance(other, DeviceInfoSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
