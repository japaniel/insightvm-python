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

class WebPage(object):
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
        'link_type': 'str',
        'path': 'str',
        'response': 'int'
    }

    attribute_map = {
        'link_type': 'linkType',
        'path': 'path',
        'response': 'response'
    }

    def __init__(self, link_type=None, path=None, response=None):  # noqa: E501
        """WebPage - a model defined in Swagger"""  # noqa: E501
        self._link_type = None
        self._path = None
        self._response = None
        self.discriminator = None
        if link_type is not None:
            self.link_type = link_type
        if path is not None:
            self.path = path
        if response is not None:
            self.response = response

    @property
    def link_type(self):
        """Gets the link_type of this WebPage.  # noqa: E501

        The type of link used to traverse or detect the page.  # noqa: E501

        :return: The link_type of this WebPage.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this WebPage.

        The type of link used to traverse or detect the page.  # noqa: E501

        :param link_type: The link_type of this WebPage.  # noqa: E501
        :type: str
        """
        allowed_values = ["seed", "html-ref", "robots", "js-string", "query-param", "pdf", "css", "implied-dir", "rss", "redirection", "sitemap", "backup", "vck-rewrite", "non-ref-guess", "soft-404"]  # noqa: E501
        if link_type not in allowed_values:
            raise ValueError(
                "Invalid value for `link_type` ({0}), must be one of {1}"  # noqa: E501
                .format(link_type, allowed_values)
            )

        self._link_type = link_type

    @property
    def path(self):
        """Gets the path of this WebPage.  # noqa: E501

        The path to the page (URI).  # noqa: E501

        :return: The path of this WebPage.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this WebPage.

        The path to the page (URI).  # noqa: E501

        :param path: The path of this WebPage.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def response(self):
        """Gets the response of this WebPage.  # noqa: E501

        The HTTP response code observed with retrieving the page.  # noqa: E501

        :return: The response of this WebPage.  # noqa: E501
        :rtype: int
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this WebPage.

        The HTTP response code observed with retrieving the page.  # noqa: E501

        :param response: The response of this WebPage.  # noqa: E501
        :type: int
        """

        self._response = response

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
        if issubclass(WebPage, dict):
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
        if not isinstance(other, WebPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
