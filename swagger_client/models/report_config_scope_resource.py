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

class ReportConfigScopeResource(object):
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
        'asset_groups': 'list[int]',
        'assets': 'list[int]',
        'scan': 'int',
        'sites': 'list[int]',
        'tags': 'list[int]'
    }

    attribute_map = {
        'asset_groups': 'assetGroups',
        'assets': 'assets',
        'scan': 'scan',
        'sites': 'sites',
        'tags': 'tags'
    }

    def __init__(self, asset_groups=None, assets=None, scan=None, sites=None, tags=None):  # noqa: E501
        """ReportConfigScopeResource - a model defined in Swagger"""  # noqa: E501
        self._asset_groups = None
        self._assets = None
        self._scan = None
        self._sites = None
        self._tags = None
        self.discriminator = None
        if asset_groups is not None:
            self.asset_groups = asset_groups
        if assets is not None:
            self.assets = assets
        if scan is not None:
            self.scan = scan
        if sites is not None:
            self.sites = sites
        if tags is not None:
            self.tags = tags

    @property
    def asset_groups(self):
        """Gets the asset_groups of this ReportConfigScopeResource.  # noqa: E501

        ${report.config.asset.groups.description}  # noqa: E501

        :return: The asset_groups of this ReportConfigScopeResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._asset_groups

    @asset_groups.setter
    def asset_groups(self, asset_groups):
        """Sets the asset_groups of this ReportConfigScopeResource.

        ${report.config.asset.groups.description}  # noqa: E501

        :param asset_groups: The asset_groups of this ReportConfigScopeResource.  # noqa: E501
        :type: list[int]
        """

        self._asset_groups = asset_groups

    @property
    def assets(self):
        """Gets the assets of this ReportConfigScopeResource.  # noqa: E501

        ${report.config.assets.description}  # noqa: E501

        :return: The assets of this ReportConfigScopeResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this ReportConfigScopeResource.

        ${report.config.assets.description}  # noqa: E501

        :param assets: The assets of this ReportConfigScopeResource.  # noqa: E501
        :type: list[int]
        """

        self._assets = assets

    @property
    def scan(self):
        """Gets the scan of this ReportConfigScopeResource.  # noqa: E501

        ${report.config.scans.description}  # noqa: E501

        :return: The scan of this ReportConfigScopeResource.  # noqa: E501
        :rtype: int
        """
        return self._scan

    @scan.setter
    def scan(self, scan):
        """Sets the scan of this ReportConfigScopeResource.

        ${report.config.scans.description}  # noqa: E501

        :param scan: The scan of this ReportConfigScopeResource.  # noqa: E501
        :type: int
        """

        self._scan = scan

    @property
    def sites(self):
        """Gets the sites of this ReportConfigScopeResource.  # noqa: E501

        ${report.config.sites.description}  # noqa: E501

        :return: The sites of this ReportConfigScopeResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this ReportConfigScopeResource.

        ${report.config.sites.description}  # noqa: E501

        :param sites: The sites of this ReportConfigScopeResource.  # noqa: E501
        :type: list[int]
        """

        self._sites = sites

    @property
    def tags(self):
        """Gets the tags of this ReportConfigScopeResource.  # noqa: E501

        ${report.config.tags.description}  # noqa: E501

        :return: The tags of this ReportConfigScopeResource.  # noqa: E501
        :rtype: list[int]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReportConfigScopeResource.

        ${report.config.tags.description}  # noqa: E501

        :param tags: The tags of this ReportConfigScopeResource.  # noqa: E501
        :type: list[int]
        """

        self._tags = tags

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
        if issubclass(ReportConfigScopeResource, dict):
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
        if not isinstance(other, ReportConfigScopeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
