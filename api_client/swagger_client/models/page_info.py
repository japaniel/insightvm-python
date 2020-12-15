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

class PageInfo(object):
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
        'number': 'int',
        'size': 'int',
        'total_pages': 'int',
        'total_resources': 'int'
    }

    attribute_map = {
        'number': 'number',
        'size': 'size',
        'total_pages': 'totalPages',
        'total_resources': 'totalResources'
    }

    def __init__(self, number=None, size=None, total_pages=None, total_resources=None):  # noqa: E501
        """PageInfo - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._size = None
        self._total_pages = None
        self._total_resources = None
        self.discriminator = None
        if number is not None:
            self.number = number
        if size is not None:
            self.size = size
        if total_pages is not None:
            self.total_pages = total_pages
        if total_resources is not None:
            self.total_resources = total_resources

    @property
    def number(self):
        """Gets the number of this PageInfo.  # noqa: E501

        The index (zero-based) of the current page returned.  # noqa: E501

        :return: The number of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PageInfo.

        The index (zero-based) of the current page returned.  # noqa: E501

        :param number: The number of this PageInfo.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def size(self):
        """Gets the size of this PageInfo.  # noqa: E501

        The maximum size of the page returned.  # noqa: E501

        :return: The size of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PageInfo.

        The maximum size of the page returned.  # noqa: E501

        :param size: The size of this PageInfo.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def total_pages(self):
        """Gets the total_pages of this PageInfo.  # noqa: E501

        The total number of pages available.  # noqa: E501

        :return: The total_pages of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PageInfo.

        The total number of pages available.  # noqa: E501

        :param total_pages: The total_pages of this PageInfo.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def total_resources(self):
        """Gets the total_resources of this PageInfo.  # noqa: E501

        The total number of resources available across all pages.  # noqa: E501

        :return: The total_resources of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_resources

    @total_resources.setter
    def total_resources(self, total_resources):
        """Sets the total_resources of this PageInfo.

        The total number of resources available across all pages.  # noqa: E501

        :param total_resources: The total_resources of this PageInfo.  # noqa: E501
        :type: int
        """

        self._total_resources = total_resources

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
        if issubclass(PageInfo, dict):
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
        if not isinstance(other, PageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other