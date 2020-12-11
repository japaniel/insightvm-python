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

class ScanTemplateDiscoveryPerformanceScanDelay(object):
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
        'maximum': 'str',
        'minimum': 'str'
    }

    attribute_map = {
        'maximum': 'maximum',
        'minimum': 'minimum'
    }

    def __init__(self, maximum=None, minimum=None):  # noqa: E501
        """ScanTemplateDiscoveryPerformanceScanDelay - a model defined in Swagger"""  # noqa: E501
        self._maximum = None
        self._minimum = None
        self.discriminator = None
        if maximum is not None:
            self.maximum = maximum
        if minimum is not None:
            self.minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this ScanTemplateDiscoveryPerformanceScanDelay.  # noqa: E501

        The minimum duration to wait between sending packets to each target host. The value is specified as a ISO8601 duration and can range from `PT0S` (0ms) to `P30S` (30s). Defaults to `PT0S`.  # noqa: E501

        :return: The maximum of this ScanTemplateDiscoveryPerformanceScanDelay.  # noqa: E501
        :rtype: str
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this ScanTemplateDiscoveryPerformanceScanDelay.

        The minimum duration to wait between sending packets to each target host. The value is specified as a ISO8601 duration and can range from `PT0S` (0ms) to `P30S` (30s). Defaults to `PT0S`.  # noqa: E501

        :param maximum: The maximum of this ScanTemplateDiscoveryPerformanceScanDelay.  # noqa: E501
        :type: str
        """

        self._maximum = maximum

    @property
    def minimum(self):
        """Gets the minimum of this ScanTemplateDiscoveryPerformanceScanDelay.  # noqa: E501

        The maximum duration to wait between sending packets to each target host. The value is specified as a ISO8601 duration and can range from `PT0S` (0ms) to `P30S` (30s). Defaults to `PT0S`.  # noqa: E501

        :return: The minimum of this ScanTemplateDiscoveryPerformanceScanDelay.  # noqa: E501
        :rtype: str
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this ScanTemplateDiscoveryPerformanceScanDelay.

        The maximum duration to wait between sending packets to each target host. The value is specified as a ISO8601 duration and can range from `PT0S` (0ms) to `P30S` (30s). Defaults to `PT0S`.  # noqa: E501

        :param minimum: The minimum of this ScanTemplateDiscoveryPerformanceScanDelay.  # noqa: E501
        :type: str
        """

        self._minimum = minimum

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
        if issubclass(ScanTemplateDiscoveryPerformanceScanDelay, dict):
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
        if not isinstance(other, ScanTemplateDiscoveryPerformanceScanDelay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
