# coding: utf-8

"""
    InsightVM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SwaggerSearchCriteriaFilter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'field': 'str',
        'lower': 'str',
        'operator': 'str',
        'upper': 'str',
        'value': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'field': 'field',
        'lower': 'lower',
        'operator': 'operator',
        'upper': 'upper',
        'value': 'value',
        'values': 'values'
    }

    def __init__(self, field=None, lower=None, operator=None, upper=None, value=None, values=None):  # noqa: E501
        """SwaggerSearchCriteriaFilter - a model defined in Swagger"""  # noqa: E501
        self._field = None
        self._lower = None
        self._operator = None
        self._upper = None
        self._value = None
        self._values = None
        self.discriminator = None
        if field is not None:
            self.field = field
        if lower is not None:
            self.lower = lower
        if operator is not None:
            self.operator = operator
        if upper is not None:
            self.upper = upper
        if value is not None:
            self.value = value
        if values is not None:
            self.values = values

    @property
    def field(self):
        """Gets the field of this SwaggerSearchCriteriaFilter.  # noqa: E501

        The filter field for the search criteria.  # noqa: E501

        :return: The field of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this SwaggerSearchCriteriaFilter.

        The filter field for the search criteria.  # noqa: E501

        :param field: The field of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def lower(self):
        """Gets the lower of this SwaggerSearchCriteriaFilter.  # noqa: E501

        The lower value to match in a range criteria.  # noqa: E501

        :return: The lower of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :rtype: str
        """
        return self._lower

    @lower.setter
    def lower(self, lower):
        """Sets the lower of this SwaggerSearchCriteriaFilter.

        The lower value to match in a range criteria.  # noqa: E501

        :param lower: The lower of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :type: str
        """

        self._lower = lower

    @property
    def operator(self):
        """Gets the operator of this SwaggerSearchCriteriaFilter.  # noqa: E501

        The operator on how to match the search criteria.  # noqa: E501

        :return: The operator of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SwaggerSearchCriteriaFilter.

        The operator on how to match the search criteria.  # noqa: E501

        :param operator: The operator of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def upper(self):
        """Gets the upper of this SwaggerSearchCriteriaFilter.  # noqa: E501

        The upper value to match in a range criteria.  # noqa: E501

        :return: The upper of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :rtype: str
        """
        return self._upper

    @upper.setter
    def upper(self, upper):
        """Sets the upper of this SwaggerSearchCriteriaFilter.

        The upper value to match in a range criteria.  # noqa: E501

        :param upper: The upper of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :type: str
        """

        self._upper = upper

    @property
    def value(self):
        """Gets the value of this SwaggerSearchCriteriaFilter.  # noqa: E501

        The single value to match using the operator.  # noqa: E501

        :return: The value of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SwaggerSearchCriteriaFilter.

        The single value to match using the operator.  # noqa: E501

        :param value: The value of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def values(self):
        """Gets the values of this SwaggerSearchCriteriaFilter.  # noqa: E501

        An array of values to match using the operator.  # noqa: E501

        :return: The values of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this SwaggerSearchCriteriaFilter.

        An array of values to match using the operator.  # noqa: E501

        :param values: The values of this SwaggerSearchCriteriaFilter.  # noqa: E501
        :type: list[str]
        """

        self._values = values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
                result[attr] = value
        if issubclass(SwaggerSearchCriteriaFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SwaggerSearchCriteriaFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
