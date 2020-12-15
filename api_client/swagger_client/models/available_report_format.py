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

class AvailableReportFormat(object):
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
        'format': 'str',
        'templates': 'list[str]'
    }

    attribute_map = {
        'format': 'format',
        'templates': 'templates'
    }

    def __init__(self, format=None, templates=None):  # noqa: E501
        """AvailableReportFormat - a model defined in Swagger"""  # noqa: E501
        self._format = None
        self._templates = None
        self.discriminator = None
        if format is not None:
            self.format = format
        if templates is not None:
            self.templates = templates

    @property
    def format(self):
        """Gets the format of this AvailableReportFormat.  # noqa: E501

        The output file-format of a report.  # noqa: E501

        :return: The format of this AvailableReportFormat.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AvailableReportFormat.

        The output file-format of a report.  # noqa: E501

        :param format: The format of this AvailableReportFormat.  # noqa: E501
        :type: str
        """
        allowed_values = ["arf-xml", "csv-export", "cyberscope-xml", "database-export", "pdf", "html", "nexpose-simple-xml", "oval-xml", "qualys-xml", "rtf", "scap-xml", "sql-query", "text", "xccdf-xml", "xccdf-csv", "xml", "xml-export", "xml-export-v2"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def templates(self):
        """Gets the templates of this AvailableReportFormat.  # noqa: E501

        The report template identifiers that can be used within a report format.  # noqa: E501

        :return: The templates of this AvailableReportFormat.  # noqa: E501
        :rtype: list[str]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this AvailableReportFormat.

        The report template identifiers that can be used within a report format.  # noqa: E501

        :param templates: The templates of this AvailableReportFormat.  # noqa: E501
        :type: list[str]
        """

        self._templates = templates

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
        if issubclass(AvailableReportFormat, dict):
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
        if not isinstance(other, AvailableReportFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other