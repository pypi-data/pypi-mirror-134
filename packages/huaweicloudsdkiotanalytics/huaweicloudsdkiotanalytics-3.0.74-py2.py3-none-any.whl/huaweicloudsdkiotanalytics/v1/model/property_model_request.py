# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropertyModelRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'display_name': 'str',
        'source_type': 'str',
        'data_schema': 'DataSchema',
        'unit': 'str',
        'value': 'object',
        'is_tag': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'source_type': 'source_type',
        'data_schema': 'data_schema',
        'unit': 'unit',
        'value': 'value',
        'is_tag': 'is_tag'
    }

    def __init__(self, name=None, display_name=None, source_type=None, data_schema=None, unit=None, value=None, is_tag=None):
        """PropertyModelRequest - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._display_name = None
        self._source_type = None
        self._data_schema = None
        self._unit = None
        self._value = None
        self._is_tag = None
        self.discriminator = None

        self.name = name
        if display_name is not None:
            self.display_name = display_name
        self.source_type = source_type
        self.data_schema = data_schema
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value
        if is_tag is not None:
            self.is_tag = is_tag

    @property
    def name(self):
        """Gets the name of this PropertyModelRequest.

        属性名称，正则：\"^[a-zA-Z0-9_]{1,64}$\"

        :return: The name of this PropertyModelRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyModelRequest.

        属性名称，正则：\"^[a-zA-Z0-9_]{1,64}$\"

        :param name: The name of this PropertyModelRequest.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this PropertyModelRequest.

        属性显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :return: The display_name of this PropertyModelRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PropertyModelRequest.

        属性显示名称，正则：\"^[\\\\u4E00-\\\\u9FA5A-Za-z0-9_@#.-]{1,64}$\"

        :param display_name: The display_name of this PropertyModelRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def source_type(self):
        """Gets the source_type of this PropertyModelRequest.

        属性类别，静态配置（static）、测量数据（measurement）、分析任务（analysis）

        :return: The source_type of this PropertyModelRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this PropertyModelRequest.

        属性类别，静态配置（static）、测量数据（measurement）、分析任务（analysis）

        :param source_type: The source_type of this PropertyModelRequest.
        :type: str
        """
        self._source_type = source_type

    @property
    def data_schema(self):
        """Gets the data_schema of this PropertyModelRequest.


        :return: The data_schema of this PropertyModelRequest.
        :rtype: DataSchema
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this PropertyModelRequest.


        :param data_schema: The data_schema of this PropertyModelRequest.
        :type: DataSchema
        """
        self._data_schema = data_schema

    @property
    def unit(self):
        """Gets the unit of this PropertyModelRequest.

        单位

        :return: The unit of this PropertyModelRequest.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this PropertyModelRequest.

        单位

        :param unit: The unit of this PropertyModelRequest.
        :type: str
        """
        self._unit = unit

    @property
    def value(self):
        """Gets the value of this PropertyModelRequest.

        静态属性的值，如：1 1.1 \"value\" {\"name\":\"value\"}

        :return: The value of this PropertyModelRequest.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PropertyModelRequest.

        静态属性的值，如：1 1.1 \"value\" {\"name\":\"value\"}

        :param value: The value of this PropertyModelRequest.
        :type: object
        """
        self._value = value

    @property
    def is_tag(self):
        """Gets the is_tag of this PropertyModelRequest.

        属性是否为标签。资产ID、标签属性、时间戳三者组成属性数据唯一键，两条唯一键相同的属性数据以覆盖方式存储；一个模型中只能配置三个属性为标签，标签配置后标签不能删除，配置标签的属性也不能删除；只有integer、double、string类型的属性可以被配置为标签。示例： 资产ID asset1上依次上报如下六组数据： 资产ID 属性A（标签） 属性B    属性C 时间戳 asset1 valueA_1     valueB_1  valueC_1 T1 asset1 valueA_1     valueB_2  valueC_2 T2 asset1 valueA_2     valueB_3  valueC_3 T2 asset1 valueA_2     valueB_4  valueC_4 T2 asset1              valueB_5  valueC_5 T3 asset1              valueB_6  valueC_6 T3 根据唯一键规则最终存储为如下四组数据： 资产ID 属性A（标签） 属性B    属性C 时间戳 asset1 valueA_1     valueB_1  valueC_1 T1 asset1 valueA_1     valueB_2  valueC_2 T2 asset1 valueA_2     valueB_4  valueC_4 T2 asset1              valueB_6  valueC_6 T3

        :return: The is_tag of this PropertyModelRequest.
        :rtype: bool
        """
        return self._is_tag

    @is_tag.setter
    def is_tag(self, is_tag):
        """Sets the is_tag of this PropertyModelRequest.

        属性是否为标签。资产ID、标签属性、时间戳三者组成属性数据唯一键，两条唯一键相同的属性数据以覆盖方式存储；一个模型中只能配置三个属性为标签，标签配置后标签不能删除，配置标签的属性也不能删除；只有integer、double、string类型的属性可以被配置为标签。示例： 资产ID asset1上依次上报如下六组数据： 资产ID 属性A（标签） 属性B    属性C 时间戳 asset1 valueA_1     valueB_1  valueC_1 T1 asset1 valueA_1     valueB_2  valueC_2 T2 asset1 valueA_2     valueB_3  valueC_3 T2 asset1 valueA_2     valueB_4  valueC_4 T2 asset1              valueB_5  valueC_5 T3 asset1              valueB_6  valueC_6 T3 根据唯一键规则最终存储为如下四组数据： 资产ID 属性A（标签） 属性B    属性C 时间戳 asset1 valueA_1     valueB_1  valueC_1 T1 asset1 valueA_1     valueB_2  valueC_2 T2 asset1 valueA_2     valueB_4  valueC_4 T2 asset1              valueB_6  valueC_6 T3

        :param is_tag: The is_tag of this PropertyModelRequest.
        :type: bool
        """
        self._is_tag = is_tag

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
        if not isinstance(other, PropertyModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
