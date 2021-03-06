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

class Address(object):
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
        'ip': 'str',
        'mac': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'mac': 'mac'
    }

    def __init__(self, ip=None, mac=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._ip = None
        self._mac = None
        self.discriminator = None
        if ip is not None:
            self.ip = ip
        if mac is not None:
            self.mac = mac

    @property
    def ip(self):
        """Gets the ip of this Address.  # noqa: E501

        The IPv4 or IPv6 address.  # noqa: E501

        :return: The ip of this Address.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Address.

        The IPv4 or IPv6 address.  # noqa: E501

        :param ip: The ip of this Address.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def mac(self):
        """Gets the mac of this Address.  # noqa: E501

        The Media Access Control (MAC) address. The format is six groups of two hexadecimal digits separated by colons.  # noqa: E501

        :return: The mac of this Address.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this Address.

        The Media Access Control (MAC) address. The format is six groups of two hexadecimal digits separated by colons.  # noqa: E501

        :param mac: The mac of this Address.  # noqa: E501
        :type: str
        """

        self._mac = mac

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
