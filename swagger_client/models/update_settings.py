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

class UpdateSettings(object):
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
        'content_auto_update': 'bool',
        'enabled': 'bool',
        'product_auto_update': 'bool'
    }

    attribute_map = {
        'content_auto_update': 'contentAutoUpdate',
        'enabled': 'enabled',
        'product_auto_update': 'productAutoUpdate'
    }

    def __init__(self, content_auto_update=None, enabled=None, product_auto_update=None):  # noqa: E501
        """UpdateSettings - a model defined in Swagger"""  # noqa: E501
        self._content_auto_update = None
        self._enabled = None
        self._product_auto_update = None
        self.discriminator = None
        if content_auto_update is not None:
            self.content_auto_update = content_auto_update
        if enabled is not None:
            self.enabled = enabled
        if product_auto_update is not None:
            self.product_auto_update = product_auto_update

    @property
    def content_auto_update(self):
        """Gets the content_auto_update of this UpdateSettings.  # noqa: E501

        Whether automatic content updates are enabled.  # noqa: E501

        :return: The content_auto_update of this UpdateSettings.  # noqa: E501
        :rtype: bool
        """
        return self._content_auto_update

    @content_auto_update.setter
    def content_auto_update(self, content_auto_update):
        """Sets the content_auto_update of this UpdateSettings.

        Whether automatic content updates are enabled.  # noqa: E501

        :param content_auto_update: The content_auto_update of this UpdateSettings.  # noqa: E501
        :type: bool
        """

        self._content_auto_update = content_auto_update

    @property
    def enabled(self):
        """Gets the enabled of this UpdateSettings.  # noqa: E501

        Whether updates are enabled.  # noqa: E501

        :return: The enabled of this UpdateSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateSettings.

        Whether updates are enabled.  # noqa: E501

        :param enabled: The enabled of this UpdateSettings.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def product_auto_update(self):
        """Gets the product_auto_update of this UpdateSettings.  # noqa: E501

        Whether automatic product updates are enabled.  # noqa: E501

        :return: The product_auto_update of this UpdateSettings.  # noqa: E501
        :rtype: bool
        """
        return self._product_auto_update

    @product_auto_update.setter
    def product_auto_update(self, product_auto_update):
        """Sets the product_auto_update of this UpdateSettings.

        Whether automatic product updates are enabled.  # noqa: E501

        :param product_auto_update: The product_auto_update of this UpdateSettings.  # noqa: E501
        :type: bool
        """

        self._product_auto_update = product_auto_update

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
        if issubclass(UpdateSettings, dict):
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
        if not isinstance(other, UpdateSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
