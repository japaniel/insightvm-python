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

class Site(object):
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
        'assets': 'int',
        'connection_type': 'str',
        'description': 'str',
        'id': 'int',
        'importance': 'str',
        'last_scan_time': 'str',
        'links': 'list[Link]',
        'name': 'str',
        'risk_score': 'float',
        'scan_engine': 'int',
        'scan_template': 'str',
        'type': 'str',
        'vulnerabilities': 'Vulnerabilities'
    }

    attribute_map = {
        'assets': 'assets',
        'connection_type': 'connectionType',
        'description': 'description',
        'id': 'id',
        'importance': 'importance',
        'last_scan_time': 'lastScanTime',
        'links': 'links',
        'name': 'name',
        'risk_score': 'riskScore',
        'scan_engine': 'scanEngine',
        'scan_template': 'scanTemplate',
        'type': 'type',
        'vulnerabilities': 'vulnerabilities'
    }

    def __init__(self, assets=None, connection_type=None, description=None, id=None, importance=None, last_scan_time=None, links=None, name=None, risk_score=None, scan_engine=None, scan_template=None, type=None, vulnerabilities=None):  # noqa: E501
        """Site - a model defined in Swagger"""  # noqa: E501
        self._assets = None
        self._connection_type = None
        self._description = None
        self._id = None
        self._importance = None
        self._last_scan_time = None
        self._links = None
        self._name = None
        self._risk_score = None
        self._scan_engine = None
        self._scan_template = None
        self._type = None
        self._vulnerabilities = None
        self.discriminator = None
        if assets is not None:
            self.assets = assets
        if connection_type is not None:
            self.connection_type = connection_type
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if importance is not None:
            self.importance = importance
        if last_scan_time is not None:
            self.last_scan_time = last_scan_time
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if risk_score is not None:
            self.risk_score = risk_score
        if scan_engine is not None:
            self.scan_engine = scan_engine
        if scan_template is not None:
            self.scan_template = scan_template
        if type is not None:
            self.type = type
        if vulnerabilities is not None:
            self.vulnerabilities = vulnerabilities

    @property
    def assets(self):
        """Gets the assets of this Site.  # noqa: E501

        The number of assets that belong to the site.  # noqa: E501

        :return: The assets of this Site.  # noqa: E501
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Site.

        The number of assets that belong to the site.  # noqa: E501

        :param assets: The assets of this Site.  # noqa: E501
        :type: int
        """

        self._assets = assets

    @property
    def connection_type(self):
        """Gets the connection_type of this Site.  # noqa: E501

        The type of discovery connection configured for the site. This property only applies to dynamic sites.  # noqa: E501

        :return: The connection_type of this Site.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this Site.

        The type of discovery connection configured for the site. This property only applies to dynamic sites.  # noqa: E501

        :param connection_type: The connection_type of this Site.  # noqa: E501
        :type: str
        """
        allowed_values = ["activesync-ldap", "activesync-office365", "activesync-powershell", "aws", "dhcp", "sonar", "vsphere"]  # noqa: E501
        if connection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

    @property
    def description(self):
        """Gets the description of this Site.  # noqa: E501

        The site description.  # noqa: E501

        :return: The description of this Site.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Site.

        The site description.  # noqa: E501

        :param description: The description of this Site.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Site.  # noqa: E501

        The identifier of the site.  # noqa: E501

        :return: The id of this Site.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Site.

        The identifier of the site.  # noqa: E501

        :param id: The id of this Site.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def importance(self):
        """Gets the importance of this Site.  # noqa: E501

        The site importance.  # noqa: E501

        :return: The importance of this Site.  # noqa: E501
        :rtype: str
        """
        return self._importance

    @importance.setter
    def importance(self, importance):
        """Sets the importance of this Site.

        The site importance.  # noqa: E501

        :param importance: The importance of this Site.  # noqa: E501
        :type: str
        """

        self._importance = importance

    @property
    def last_scan_time(self):
        """Gets the last_scan_time of this Site.  # noqa: E501

        The date and time of the site's last scan.  # noqa: E501

        :return: The last_scan_time of this Site.  # noqa: E501
        :rtype: str
        """
        return self._last_scan_time

    @last_scan_time.setter
    def last_scan_time(self, last_scan_time):
        """Sets the last_scan_time of this Site.

        The date and time of the site's last scan.  # noqa: E501

        :param last_scan_time: The last_scan_time of this Site.  # noqa: E501
        :type: str
        """

        self._last_scan_time = last_scan_time

    @property
    def links(self):
        """Gets the links of this Site.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this Site.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Site.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this Site.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this Site.  # noqa: E501

        The site name.  # noqa: E501

        :return: The name of this Site.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Site.

        The site name.  # noqa: E501

        :param name: The name of this Site.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def risk_score(self):
        """Gets the risk_score of this Site.  # noqa: E501

        The risk score (with criticality adjustments) of the site.  # noqa: E501

        :return: The risk_score of this Site.  # noqa: E501
        :rtype: float
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """Sets the risk_score of this Site.

        The risk score (with criticality adjustments) of the site.  # noqa: E501

        :param risk_score: The risk_score of this Site.  # noqa: E501
        :type: float
        """

        self._risk_score = risk_score

    @property
    def scan_engine(self):
        """Gets the scan_engine of this Site.  # noqa: E501

        The identifier of the scan engine configured in the site.  # noqa: E501

        :return: The scan_engine of this Site.  # noqa: E501
        :rtype: int
        """
        return self._scan_engine

    @scan_engine.setter
    def scan_engine(self, scan_engine):
        """Sets the scan_engine of this Site.

        The identifier of the scan engine configured in the site.  # noqa: E501

        :param scan_engine: The scan_engine of this Site.  # noqa: E501
        :type: int
        """

        self._scan_engine = scan_engine

    @property
    def scan_template(self):
        """Gets the scan_template of this Site.  # noqa: E501

        The identifier of the scan template configured in the site.  # noqa: E501

        :return: The scan_template of this Site.  # noqa: E501
        :rtype: str
        """
        return self._scan_template

    @scan_template.setter
    def scan_template(self, scan_template):
        """Sets the scan_template of this Site.

        The identifier of the scan template configured in the site.  # noqa: E501

        :param scan_template: The scan_template of this Site.  # noqa: E501
        :type: str
        """

        self._scan_template = scan_template

    @property
    def type(self):
        """Gets the type of this Site.  # noqa: E501

        The type of the site.  # noqa: E501

        :return: The type of this Site.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Site.

        The type of the site.  # noqa: E501

        :param type: The type of this Site.  # noqa: E501
        :type: str
        """
        allowed_values = ["agent", "dynamic", "static"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vulnerabilities(self):
        """Gets the vulnerabilities of this Site.  # noqa: E501


        :return: The vulnerabilities of this Site.  # noqa: E501
        :rtype: Vulnerabilities
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        """Sets the vulnerabilities of this Site.


        :param vulnerabilities: The vulnerabilities of this Site.  # noqa: E501
        :type: Vulnerabilities
        """

        self._vulnerabilities = vulnerabilities

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
        if issubclass(Site, dict):
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
        if not isinstance(other, Site):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
