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

class ScanEngine(object):
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
        'address': 'str',
        'content_version': 'str',
        'engine_pools': 'list[int]',
        'id': 'int',
        'last_refreshed_date': 'str',
        'last_updated_date': 'str',
        'links': 'list[Link]',
        'name': 'str',
        'port': 'int',
        'product_version': 'str',
        'sites': 'list[int]'
    }

    attribute_map = {
        'address': 'address',
        'content_version': 'contentVersion',
        'engine_pools': 'enginePools',
        'id': 'id',
        'last_refreshed_date': 'lastRefreshedDate',
        'last_updated_date': 'lastUpdatedDate',
        'links': 'links',
        'name': 'name',
        'port': 'port',
        'product_version': 'productVersion',
        'sites': 'sites'
    }

    def __init__(self, address=None, content_version=None, engine_pools=None, id=None, last_refreshed_date=None, last_updated_date=None, links=None, name=None, port=None, product_version=None, sites=None):  # noqa: E501
        """ScanEngine - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._content_version = None
        self._engine_pools = None
        self._id = None
        self._last_refreshed_date = None
        self._last_updated_date = None
        self._links = None
        self._name = None
        self._port = None
        self._product_version = None
        self._sites = None
        self.discriminator = None
        self.address = address
        if content_version is not None:
            self.content_version = content_version
        if engine_pools is not None:
            self.engine_pools = engine_pools
        self.id = id
        if last_refreshed_date is not None:
            self.last_refreshed_date = last_refreshed_date
        if last_updated_date is not None:
            self.last_updated_date = last_updated_date
        if links is not None:
            self.links = links
        self.name = name
        self.port = port
        if product_version is not None:
            self.product_version = product_version
        if sites is not None:
            self.sites = sites

    @property
    def address(self):
        """Gets the address of this ScanEngine.  # noqa: E501

        The address the scan engine is hosted.  # noqa: E501

        :return: The address of this ScanEngine.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ScanEngine.

        The address the scan engine is hosted.  # noqa: E501

        :param address: The address of this ScanEngine.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def content_version(self):
        """Gets the content_version of this ScanEngine.  # noqa: E501

        The content version of the scan engine.  # noqa: E501

        :return: The content_version of this ScanEngine.  # noqa: E501
        :rtype: str
        """
        return self._content_version

    @content_version.setter
    def content_version(self, content_version):
        """Sets the content_version of this ScanEngine.

        The content version of the scan engine.  # noqa: E501

        :param content_version: The content_version of this ScanEngine.  # noqa: E501
        :type: str
        """

        self._content_version = content_version

    @property
    def engine_pools(self):
        """Gets the engine_pools of this ScanEngine.  # noqa: E501

        A list of identifiers of engine pools this engine is included in.  # noqa: E501

        :return: The engine_pools of this ScanEngine.  # noqa: E501
        :rtype: list[int]
        """
        return self._engine_pools

    @engine_pools.setter
    def engine_pools(self, engine_pools):
        """Sets the engine_pools of this ScanEngine.

        A list of identifiers of engine pools this engine is included in.  # noqa: E501

        :param engine_pools: The engine_pools of this ScanEngine.  # noqa: E501
        :type: list[int]
        """

        self._engine_pools = engine_pools

    @property
    def id(self):
        """Gets the id of this ScanEngine.  # noqa: E501

        The identifier of the scan engine.  # noqa: E501

        :return: The id of this ScanEngine.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScanEngine.

        The identifier of the scan engine.  # noqa: E501

        :param id: The id of this ScanEngine.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_refreshed_date(self):
        """Gets the last_refreshed_date of this ScanEngine.  # noqa: E501

        The date the engine was last refreshed. Date format is in ISO 8601.  # noqa: E501

        :return: The last_refreshed_date of this ScanEngine.  # noqa: E501
        :rtype: str
        """
        return self._last_refreshed_date

    @last_refreshed_date.setter
    def last_refreshed_date(self, last_refreshed_date):
        """Sets the last_refreshed_date of this ScanEngine.

        The date the engine was last refreshed. Date format is in ISO 8601.  # noqa: E501

        :param last_refreshed_date: The last_refreshed_date of this ScanEngine.  # noqa: E501
        :type: str
        """

        self._last_refreshed_date = last_refreshed_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this ScanEngine.  # noqa: E501

        The date the engine was last updated. Date format is in ISO 8601.  # noqa: E501

        :return: The last_updated_date of this ScanEngine.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this ScanEngine.

        The date the engine was last updated. Date format is in ISO 8601.  # noqa: E501

        :param last_updated_date: The last_updated_date of this ScanEngine.  # noqa: E501
        :type: str
        """

        self._last_updated_date = last_updated_date

    @property
    def links(self):
        """Gets the links of this ScanEngine.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this ScanEngine.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ScanEngine.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this ScanEngine.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this ScanEngine.  # noqa: E501

        The name of the scan engine.  # noqa: E501

        :return: The name of this ScanEngine.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScanEngine.

        The name of the scan engine.  # noqa: E501

        :param name: The name of this ScanEngine.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def port(self):
        """Gets the port of this ScanEngine.  # noqa: E501

        The port used by the scan engine to communicate with the Security Console.  # noqa: E501

        :return: The port of this ScanEngine.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ScanEngine.

        The port used by the scan engine to communicate with the Security Console.  # noqa: E501

        :param port: The port of this ScanEngine.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def product_version(self):
        """Gets the product_version of this ScanEngine.  # noqa: E501

        The product version of the scan engine.  # noqa: E501

        :return: The product_version of this ScanEngine.  # noqa: E501
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this ScanEngine.

        The product version of the scan engine.  # noqa: E501

        :param product_version: The product_version of this ScanEngine.  # noqa: E501
        :type: str
        """

        self._product_version = product_version

    @property
    def sites(self):
        """Gets the sites of this ScanEngine.  # noqa: E501

        A list of identifiers of each site the scan engine is assigned to.  # noqa: E501

        :return: The sites of this ScanEngine.  # noqa: E501
        :rtype: list[int]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this ScanEngine.

        A list of identifiers of each site the scan engine is assigned to.  # noqa: E501

        :param sites: The sites of this ScanEngine.  # noqa: E501
        :type: list[int]
        """

        self._sites = sites

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
        if issubclass(ScanEngine, dict):
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
        if not isinstance(other, ScanEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
