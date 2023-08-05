# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportLiveDataApiDefinitionsV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'success': 'list[Success]',
        'failure': 'list[Failure]',
        'swagger': 'Swagger'
    }

    attribute_map = {
        'success': 'success',
        'failure': 'failure',
        'swagger': 'swagger'
    }

    def __init__(self, success=None, failure=None, swagger=None):
        """ImportLiveDataApiDefinitionsV2Response - a model defined in huaweicloud sdk"""
        
        super(ImportLiveDataApiDefinitionsV2Response, self).__init__()

        self._success = None
        self._failure = None
        self._swagger = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failure is not None:
            self.failure = failure
        if swagger is not None:
            self.swagger = swagger

    @property
    def success(self):
        """Gets the success of this ImportLiveDataApiDefinitionsV2Response.

        导入成功信息

        :return: The success of this ImportLiveDataApiDefinitionsV2Response.
        :rtype: list[Success]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ImportLiveDataApiDefinitionsV2Response.

        导入成功信息

        :param success: The success of this ImportLiveDataApiDefinitionsV2Response.
        :type: list[Success]
        """
        self._success = success

    @property
    def failure(self):
        """Gets the failure of this ImportLiveDataApiDefinitionsV2Response.

        导入失败信息

        :return: The failure of this ImportLiveDataApiDefinitionsV2Response.
        :rtype: list[Failure]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this ImportLiveDataApiDefinitionsV2Response.

        导入失败信息

        :param failure: The failure of this ImportLiveDataApiDefinitionsV2Response.
        :type: list[Failure]
        """
        self._failure = failure

    @property
    def swagger(self):
        """Gets the swagger of this ImportLiveDataApiDefinitionsV2Response.


        :return: The swagger of this ImportLiveDataApiDefinitionsV2Response.
        :rtype: Swagger
        """
        return self._swagger

    @swagger.setter
    def swagger(self, swagger):
        """Sets the swagger of this ImportLiveDataApiDefinitionsV2Response.


        :param swagger: The swagger of this ImportLiveDataApiDefinitionsV2Response.
        :type: Swagger
        """
        self._swagger = swagger

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
        if not isinstance(other, ImportLiveDataApiDefinitionsV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
