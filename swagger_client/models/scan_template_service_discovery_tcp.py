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

class ScanTemplateServiceDiscoveryTcp(object):
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
        'additional_ports': 'list[object]',
        'excluded_ports': 'list[object]',
        'links': 'list[Link]',
        'method': 'str',
        'ports': 'str'
    }

    attribute_map = {
        'additional_ports': 'additionalPorts',
        'excluded_ports': 'excludedPorts',
        'links': 'links',
        'method': 'method',
        'ports': 'ports'
    }

    def __init__(self, additional_ports=None, excluded_ports=None, links=None, method=None, ports=None):  # noqa: E501
        """ScanTemplateServiceDiscoveryTcp - a model defined in Swagger"""  # noqa: E501
        self._additional_ports = None
        self._excluded_ports = None
        self._links = None
        self._method = None
        self._ports = None
        self.discriminator = None
        if additional_ports is not None:
            self.additional_ports = additional_ports
        if excluded_ports is not None:
            self.excluded_ports = excluded_ports
        if links is not None:
            self.links = links
        if method is not None:
            self.method = method
        if ports is not None:
            self.ports = ports

    @property
    def additional_ports(self):
        """Gets the additional_ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501

        Additional TCP ports to scan. Individual ports can be specified as numbers or a string, but port ranges must be strings (e.g. `\"7892-7898\"`). Defaults to empty.  # noqa: E501

        :return: The additional_ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :rtype: list[object]
        """
        return self._additional_ports

    @additional_ports.setter
    def additional_ports(self, additional_ports):
        """Sets the additional_ports of this ScanTemplateServiceDiscoveryTcp.

        Additional TCP ports to scan. Individual ports can be specified as numbers or a string, but port ranges must be strings (e.g. `\"7892-7898\"`). Defaults to empty.  # noqa: E501

        :param additional_ports: The additional_ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :type: list[object]
        """

        self._additional_ports = additional_ports

    @property
    def excluded_ports(self):
        """Gets the excluded_ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501

        TCP ports to exclude from scanning. Individual ports can be specified as numbers or a string, but port ranges must be strings (e.g. `\"7892-7898\"`). Defaults to empty.  # noqa: E501

        :return: The excluded_ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :rtype: list[object]
        """
        return self._excluded_ports

    @excluded_ports.setter
    def excluded_ports(self, excluded_ports):
        """Sets the excluded_ports of this ScanTemplateServiceDiscoveryTcp.

        TCP ports to exclude from scanning. Individual ports can be specified as numbers or a string, but port ranges must be strings (e.g. `\"7892-7898\"`). Defaults to empty.  # noqa: E501

        :param excluded_ports: The excluded_ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :type: list[object]
        """

        self._excluded_ports = excluded_ports

    @property
    def links(self):
        """Gets the links of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ScanTemplateServiceDiscoveryTcp.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def method(self):
        """Gets the method of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501

        The method of TCP discovery. Defaults to `SYN`.  # noqa: E501

        :return: The method of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ScanTemplateServiceDiscoveryTcp.

        The method of TCP discovery. Defaults to `SYN`.  # noqa: E501

        :param method: The method of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYN", "SYN+RST", "SYN+FIN", "SYN+ECE", "Full"]  # noqa: E501
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def ports(self):
        """Gets the ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501

        The TCP ports to scan. Defaults to `well-known`.  # noqa: E501

        :return: The ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this ScanTemplateServiceDiscoveryTcp.

        The TCP ports to scan. Defaults to `well-known`.  # noqa: E501

        :param ports: The ports of this ScanTemplateServiceDiscoveryTcp.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "well-known", "custom", "none"]  # noqa: E501
        if ports not in allowed_values:
            raise ValueError(
                "Invalid value for `ports` ({0}), must be one of {1}"  # noqa: E501
                .format(ports, allowed_values)
            )

        self._ports = ports

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
        if issubclass(ScanTemplateServiceDiscoveryTcp, dict):
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
        if not isinstance(other, ScanTemplateServiceDiscoveryTcp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
