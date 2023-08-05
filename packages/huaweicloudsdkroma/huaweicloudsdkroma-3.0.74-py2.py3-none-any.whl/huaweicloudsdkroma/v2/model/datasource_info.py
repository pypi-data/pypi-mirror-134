# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasourceInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'datasource_name': 'str',
        'datasource_type': 'str',
        'app_id': 'str',
        'custom_plugin_id': 'str',
        'content': 'Content',
        'description': 'str'
    }

    attribute_map = {
        'datasource_name': 'datasource_name',
        'datasource_type': 'datasource_type',
        'app_id': 'app_id',
        'custom_plugin_id': 'custom_plugin_id',
        'content': 'content',
        'description': 'description'
    }

    def __init__(self, datasource_name=None, datasource_type=None, app_id=None, custom_plugin_id=None, content=None, description=None):
        """DatasourceInfo - a model defined in huaweicloud sdk"""
        
        

        self._datasource_name = None
        self._datasource_type = None
        self._app_id = None
        self._custom_plugin_id = None
        self._content = None
        self._description = None
        self.discriminator = None

        if datasource_name is not None:
            self.datasource_name = datasource_name
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if app_id is not None:
            self.app_id = app_id
        if custom_plugin_id is not None:
            self.custom_plugin_id = custom_plugin_id
        if content is not None:
            self.content = content
        if description is not None:
            self.description = description

    @property
    def datasource_name(self):
        """Gets the datasource_name of this DatasourceInfo.

        数据源名称，数据源名称不能包含&、<、>、\"、'、(、) ，长度为1~255字符

        :return: The datasource_name of this DatasourceInfo.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        """Sets the datasource_name of this DatasourceInfo.

        数据源名称，数据源名称不能包含&、<、>、\"、'、(、) ，长度为1~255字符

        :param datasource_name: The datasource_name of this DatasourceInfo.
        :type: str
        """
        self._datasource_name = datasource_name

    @property
    def datasource_type(self):
        """Gets the datasource_type of this DatasourceInfo.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :return: The datasource_type of this DatasourceInfo.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this DatasourceInfo.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :param datasource_type: The datasource_type of this DatasourceInfo.
        :type: str
        """
        self._datasource_type = datasource_type

    @property
    def app_id(self):
        """Gets the app_id of this DatasourceInfo.

        数据源所属应用ID

        :return: The app_id of this DatasourceInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this DatasourceInfo.

        数据源所属应用ID

        :param app_id: The app_id of this DatasourceInfo.
        :type: str
        """
        self._app_id = app_id

    @property
    def custom_plugin_id(self):
        """Gets the custom_plugin_id of this DatasourceInfo.

        数据源所属连接器Id，自定义数据源必填

        :return: The custom_plugin_id of this DatasourceInfo.
        :rtype: str
        """
        return self._custom_plugin_id

    @custom_plugin_id.setter
    def custom_plugin_id(self, custom_plugin_id):
        """Sets the custom_plugin_id of this DatasourceInfo.

        数据源所属连接器Id，自定义数据源必填

        :param custom_plugin_id: The custom_plugin_id of this DatasourceInfo.
        :type: str
        """
        self._custom_plugin_id = custom_plugin_id

    @property
    def content(self):
        """Gets the content of this DatasourceInfo.


        :return: The content of this DatasourceInfo.
        :rtype: Content
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DatasourceInfo.


        :param content: The content of this DatasourceInfo.
        :type: Content
        """
        self._content = content

    @property
    def description(self):
        """Gets the description of this DatasourceInfo.

        数据源描述

        :return: The description of this DatasourceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatasourceInfo.

        数据源描述

        :param description: The description of this DatasourceInfo.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, DatasourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
