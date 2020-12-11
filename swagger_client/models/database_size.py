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

class DatabaseSize(object):
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
        'bytes': 'int',
        'formatted': 'str'
    }

    attribute_map = {
        'bytes': 'bytes',
        'formatted': 'formatted'
    }

    def __init__(self, bytes=None, formatted=None):  # noqa: E501
        """DatabaseSize - a model defined in Swagger"""  # noqa: E501
        self._bytes = None
        self._formatted = None
        self.discriminator = None
        if bytes is not None:
            self.bytes = bytes
        if formatted is not None:
            self.formatted = formatted

    @property
    def bytes(self):
        """Gets the bytes of this DatabaseSize.  # noqa: E501

        The raw value in bytes.  # noqa: E501

        :return: The bytes of this DatabaseSize.  # noqa: E501
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this DatabaseSize.

        The raw value in bytes.  # noqa: E501

        :param bytes: The bytes of this DatabaseSize.  # noqa: E501
        :type: int
        """

        self._bytes = bytes

    @property
    def formatted(self):
        """Gets the formatted of this DatabaseSize.  # noqa: E501

        The value formatted in human-readable notation (e.g. GB, MB, KB, bytes).  # noqa: E501

        :return: The formatted of this DatabaseSize.  # noqa: E501
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        """Sets the formatted of this DatabaseSize.

        The value formatted in human-readable notation (e.g. GB, MB, KB, bytes).  # noqa: E501

        :param formatted: The formatted of this DatabaseSize.  # noqa: E501
        :type: str
        """

        self._formatted = formatted

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
        if issubclass(DatabaseSize, dict):
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
        if not isinstance(other, DatabaseSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
