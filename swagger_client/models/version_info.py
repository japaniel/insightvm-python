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

class VersionInfo(object):
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
        'build': 'str',
        'changeset': 'str',
        'platform': 'str',
        'semantic': 'str',
        'update': 'UpdateInfo'
    }

    attribute_map = {
        'build': 'build',
        'changeset': 'changeset',
        'platform': 'platform',
        'semantic': 'semantic',
        'update': 'update'
    }

    def __init__(self, build=None, changeset=None, platform=None, semantic=None, update=None):  # noqa: E501
        """VersionInfo - a model defined in Swagger"""  # noqa: E501
        self._build = None
        self._changeset = None
        self._platform = None
        self._semantic = None
        self._update = None
        self.discriminator = None
        if build is not None:
            self.build = build
        if changeset is not None:
            self.changeset = changeset
        if platform is not None:
            self.platform = platform
        if semantic is not None:
            self.semantic = semantic
        if update is not None:
            self.update = update

    @property
    def build(self):
        """Gets the build of this VersionInfo.  # noqa: E501

        The build number.  # noqa: E501

        :return: The build of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this VersionInfo.

        The build number.  # noqa: E501

        :param build: The build of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def changeset(self):
        """Gets the changeset of this VersionInfo.  # noqa: E501

        The changeset of the source build.  # noqa: E501

        :return: The changeset of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._changeset

    @changeset.setter
    def changeset(self, changeset):
        """Sets the changeset of this VersionInfo.

        The changeset of the source build.  # noqa: E501

        :param changeset: The changeset of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._changeset = changeset

    @property
    def platform(self):
        """Gets the platform of this VersionInfo.  # noqa: E501

        The platform of the build.  # noqa: E501

        :return: The platform of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this VersionInfo.

        The platform of the build.  # noqa: E501

        :param platform: The platform of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def semantic(self):
        """Gets the semantic of this VersionInfo.  # noqa: E501

        The semantic version number of the installation.  # noqa: E501

        :return: The semantic of this VersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._semantic

    @semantic.setter
    def semantic(self, semantic):
        """Sets the semantic of this VersionInfo.

        The semantic version number of the installation.  # noqa: E501

        :param semantic: The semantic of this VersionInfo.  # noqa: E501
        :type: str
        """

        self._semantic = semantic

    @property
    def update(self):
        """Gets the update of this VersionInfo.  # noqa: E501


        :return: The update of this VersionInfo.  # noqa: E501
        :rtype: UpdateInfo
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this VersionInfo.


        :param update: The update of this VersionInfo.  # noqa: E501
        :type: UpdateInfo
        """

        self._update = update

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
        if issubclass(VersionInfo, dict):
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
        if not isinstance(other, VersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
