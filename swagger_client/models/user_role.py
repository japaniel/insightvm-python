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

class UserRole(object):
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
        'all_asset_groups': 'bool',
        'all_sites': 'bool',
        'id': 'str',
        'name': 'str',
        'privileges': 'list[str]',
        'superuser': 'bool'
    }

    attribute_map = {
        'all_asset_groups': 'allAssetGroups',
        'all_sites': 'allSites',
        'id': 'id',
        'name': 'name',
        'privileges': 'privileges',
        'superuser': 'superuser'
    }

    def __init__(self, all_asset_groups=None, all_sites=None, id=None, name=None, privileges=None, superuser=None):  # noqa: E501
        """UserRole - a model defined in Swagger"""  # noqa: E501
        self._all_asset_groups = None
        self._all_sites = None
        self._id = None
        self._name = None
        self._privileges = None
        self._superuser = None
        self.discriminator = None
        if all_asset_groups is not None:
            self.all_asset_groups = all_asset_groups
        if all_sites is not None:
            self.all_sites = all_sites
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if privileges is not None:
            self.privileges = privileges
        if superuser is not None:
            self.superuser = superuser

    @property
    def all_asset_groups(self):
        """Gets the all_asset_groups of this UserRole.  # noqa: E501

        Whether the user has access to all asset groups.  # noqa: E501

        :return: The all_asset_groups of this UserRole.  # noqa: E501
        :rtype: bool
        """
        return self._all_asset_groups

    @all_asset_groups.setter
    def all_asset_groups(self, all_asset_groups):
        """Sets the all_asset_groups of this UserRole.

        Whether the user has access to all asset groups.  # noqa: E501

        :param all_asset_groups: The all_asset_groups of this UserRole.  # noqa: E501
        :type: bool
        """

        self._all_asset_groups = all_asset_groups

    @property
    def all_sites(self):
        """Gets the all_sites of this UserRole.  # noqa: E501

        Whether the user has access to all sites.  # noqa: E501

        :return: The all_sites of this UserRole.  # noqa: E501
        :rtype: bool
        """
        return self._all_sites

    @all_sites.setter
    def all_sites(self, all_sites):
        """Sets the all_sites of this UserRole.

        Whether the user has access to all sites.  # noqa: E501

        :param all_sites: The all_sites of this UserRole.  # noqa: E501
        :type: bool
        """

        self._all_sites = all_sites

    @property
    def id(self):
        """Gets the id of this UserRole.  # noqa: E501

        The identifier of the role the user is assigned to.  # noqa: E501

        :return: The id of this UserRole.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserRole.

        The identifier of the role the user is assigned to.  # noqa: E501

        :param id: The id of this UserRole.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserRole.  # noqa: E501

        The name of the role the user is assigned to.  # noqa: E501

        :return: The name of this UserRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserRole.

        The name of the role the user is assigned to.  # noqa: E501

        :param name: The name of this UserRole.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def privileges(self):
        """Gets the privileges of this UserRole.  # noqa: E501

        The privileges granted to the user by their role.  # noqa: E501

        :return: The privileges of this UserRole.  # noqa: E501
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this UserRole.

        The privileges granted to the user by their role.  # noqa: E501

        :param privileges: The privileges of this UserRole.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["all-permissions", "create-reports", "configure-global-settings", "manage-sites", "manage-tags", "manage-static-asset-groups", "manage-dynamic-asset-groups", "manage-scan-templates", "manage-report-templates", "manage-scan-engines", "submit-vulnerability-exceptions", "approve-vulnerability-exceptions", "delete-vulnerability-exceptions", "create-tickets", "close-tickets", "assign-ticket-assignee", "manage-site-access", "manage-asset-group-access", "manage-report-access", "use-restricted-report-sections", "manage-policies", "view-asset-group-asset-data", "manage-asset-group-assets", "view-site-asset-data", "specify-site-metadata", "purge-site-asset-data", "specify-scan-targets", "assign-scan-engine", "assign-scan-template", "manage-site-credentials", "manage-scan-alerts", "schedule-automatic-scans", "start-unscheduled-scans"]  # noqa: E501
        if not set(privileges).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `privileges` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(privileges) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._privileges = privileges

    @property
    def superuser(self):
        """Gets the superuser of this UserRole.  # noqa: E501

        Whether the user is a superuser.  # noqa: E501

        :return: The superuser of this UserRole.  # noqa: E501
        :rtype: bool
        """
        return self._superuser

    @superuser.setter
    def superuser(self, superuser):
        """Sets the superuser of this UserRole.

        Whether the user is a superuser.  # noqa: E501

        :param superuser: The superuser of this UserRole.  # noqa: E501
        :type: bool
        """

        self._superuser = superuser

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
        if issubclass(UserRole, dict):
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
        if not isinstance(other, UserRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
