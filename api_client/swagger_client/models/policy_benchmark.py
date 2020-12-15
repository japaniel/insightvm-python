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

class PolicyBenchmark(object):
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
        'links': 'list[Link]',
        'name': 'str',
        'title': 'str',
        'version': 'str'
    }

    attribute_map = {
        'links': 'links',
        'name': 'name',
        'title': 'title',
        'version': 'version'
    }

    def __init__(self, links=None, name=None, title=None, version=None):  # noqa: E501
        """PolicyBenchmark - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._name = None
        self._title = None
        self._version = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if version is not None:
            self.version = version

    @property
    def links(self):
        """Gets the links of this PolicyBenchmark.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this PolicyBenchmark.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyBenchmark.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this PolicyBenchmark.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this PolicyBenchmark.  # noqa: E501

        The name of the policy's benchmark.  # noqa: E501

        :return: The name of this PolicyBenchmark.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyBenchmark.

        The name of the policy's benchmark.  # noqa: E501

        :param name: The name of this PolicyBenchmark.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this PolicyBenchmark.  # noqa: E501

        The title of the policy benchmark.  # noqa: E501

        :return: The title of this PolicyBenchmark.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PolicyBenchmark.

        The title of the policy benchmark.  # noqa: E501

        :param title: The title of this PolicyBenchmark.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """Gets the version of this PolicyBenchmark.  # noqa: E501

        The version number of the benchmark that includes the policy.  # noqa: E501

        :return: The version of this PolicyBenchmark.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PolicyBenchmark.

        The version number of the benchmark that includes the policy.  # noqa: E501

        :param version: The version of this PolicyBenchmark.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(PolicyBenchmark, dict):
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
        if not isinstance(other, PolicyBenchmark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other