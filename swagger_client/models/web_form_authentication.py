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

class WebFormAuthentication(object):
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
        'base_url': 'str',
        'enabled': 'bool',
        'id': 'int',
        'links': 'list[Link]',
        'login_regular_expression': 'str',
        'login_url': 'str',
        'name': 'str',
        'service': 'str'
    }

    attribute_map = {
        'base_url': 'baseURL',
        'enabled': 'enabled',
        'id': 'id',
        'links': 'links',
        'login_regular_expression': 'loginRegularExpression',
        'login_url': 'loginURL',
        'name': 'name',
        'service': 'service'
    }

    def __init__(self, base_url=None, enabled=None, id=None, links=None, login_regular_expression=None, login_url=None, name=None, service=None):  # noqa: E501
        """WebFormAuthentication - a model defined in Swagger"""  # noqa: E501
        self._base_url = None
        self._enabled = None
        self._id = None
        self._links = None
        self._login_regular_expression = None
        self._login_url = None
        self._name = None
        self._service = None
        self.discriminator = None
        if base_url is not None:
            self.base_url = base_url
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if login_regular_expression is not None:
            self.login_regular_expression = login_regular_expression
        if login_url is not None:
            self.login_url = login_url
        if name is not None:
            self.name = name
        if service is not None:
            self.service = service

    @property
    def base_url(self):
        """Gets the base_url of this WebFormAuthentication.  # noqa: E501

        The base URL is the main address from which all paths in the target Web site begin. Includes the protocol. Example: http://acme.com.  # noqa: E501

        :return: The base_url of this WebFormAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this WebFormAuthentication.

        The base URL is the main address from which all paths in the target Web site begin. Includes the protocol. Example: http://acme.com.  # noqa: E501

        :param base_url: The base_url of this WebFormAuthentication.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def enabled(self):
        """Gets the enabled of this WebFormAuthentication.  # noqa: E501

        Flag indicating whether the HTML form web authentication is enabled for the site's scans.  # noqa: E501

        :return: The enabled of this WebFormAuthentication.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WebFormAuthentication.

        Flag indicating whether the HTML form web authentication is enabled for the site's scans.  # noqa: E501

        :param enabled: The enabled of this WebFormAuthentication.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this WebFormAuthentication.  # noqa: E501

        The identifier of the HTML form web authentication.  # noqa: E501

        :return: The id of this WebFormAuthentication.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebFormAuthentication.

        The identifier of the HTML form web authentication.  # noqa: E501

        :param id: The id of this WebFormAuthentication.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this WebFormAuthentication.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this WebFormAuthentication.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this WebFormAuthentication.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this WebFormAuthentication.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def login_regular_expression(self):
        """Gets the login_regular_expression of this WebFormAuthentication.  # noqa: E501

        The regular expression matches the message that the Web server returns if the login attempt fails.  # noqa: E501

        :return: The login_regular_expression of this WebFormAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._login_regular_expression

    @login_regular_expression.setter
    def login_regular_expression(self, login_regular_expression):
        """Sets the login_regular_expression of this WebFormAuthentication.

        The regular expression matches the message that the Web server returns if the login attempt fails.  # noqa: E501

        :param login_regular_expression: The login_regular_expression of this WebFormAuthentication.  # noqa: E501
        :type: str
        """

        self._login_regular_expression = login_regular_expression

    @property
    def login_url(self):
        """Gets the login_url of this WebFormAuthentication.  # noqa: E501

        The login page URL contains form for logging on. Include the base URL. Example: http://acme.com/login.  # noqa: E501

        :return: The login_url of this WebFormAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        """Sets the login_url of this WebFormAuthentication.

        The login page URL contains form for logging on. Include the base URL. Example: http://acme.com/login.  # noqa: E501

        :param login_url: The login_url of this WebFormAuthentication.  # noqa: E501
        :type: str
        """

        self._login_url = login_url

    @property
    def name(self):
        """Gets the name of this WebFormAuthentication.  # noqa: E501

        The HTML form web authentication name.  # noqa: E501

        :return: The name of this WebFormAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebFormAuthentication.

        The HTML form web authentication name.  # noqa: E501

        :param name: The name of this WebFormAuthentication.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service(self):
        """Gets the service of this WebFormAuthentication.  # noqa: E501

        Value indicating whether this web authentication  configuration is for HTML form authentication or HTTP header authentication.  # noqa: E501

        :return: The service of this WebFormAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this WebFormAuthentication.

        Value indicating whether this web authentication  configuration is for HTML form authentication or HTTP header authentication.  # noqa: E501

        :param service: The service of this WebFormAuthentication.  # noqa: E501
        :type: str
        """
        allowed_values = ["html-form", "http-header"]  # noqa: E501
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

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
        if issubclass(WebFormAuthentication, dict):
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
        if not isinstance(other, WebFormAuthentication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
