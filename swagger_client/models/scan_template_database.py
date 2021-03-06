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

class ScanTemplateDatabase(object):
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
        'db2': 'str',
        'links': 'list[Link]',
        'oracle': 'list[str]',
        'postgres': 'str'
    }

    attribute_map = {
        'db2': 'db2',
        'links': 'links',
        'oracle': 'oracle',
        'postgres': 'postgres'
    }

    def __init__(self, db2=None, links=None, oracle=None, postgres=None):  # noqa: E501
        """ScanTemplateDatabase - a model defined in Swagger"""  # noqa: E501
        self._db2 = None
        self._links = None
        self._oracle = None
        self._postgres = None
        self.discriminator = None
        if db2 is not None:
            self.db2 = db2
        if links is not None:
            self.links = links
        if oracle is not None:
            self.oracle = oracle
        if postgres is not None:
            self.postgres = postgres

    @property
    def db2(self):
        """Gets the db2 of this ScanTemplateDatabase.  # noqa: E501

        Database name for DB2 database instance.  # noqa: E501

        :return: The db2 of this ScanTemplateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._db2

    @db2.setter
    def db2(self, db2):
        """Sets the db2 of this ScanTemplateDatabase.

        Database name for DB2 database instance.  # noqa: E501

        :param db2: The db2 of this ScanTemplateDatabase.  # noqa: E501
        :type: str
        """

        self._db2 = db2

    @property
    def links(self):
        """Gets the links of this ScanTemplateDatabase.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this ScanTemplateDatabase.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ScanTemplateDatabase.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this ScanTemplateDatabase.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def oracle(self):
        """Gets the oracle of this ScanTemplateDatabase.  # noqa: E501

        Database name (SID) for an Oracle database instance.  # noqa: E501

        :return: The oracle of this ScanTemplateDatabase.  # noqa: E501
        :rtype: list[str]
        """
        return self._oracle

    @oracle.setter
    def oracle(self, oracle):
        """Sets the oracle of this ScanTemplateDatabase.

        Database name (SID) for an Oracle database instance.  # noqa: E501

        :param oracle: The oracle of this ScanTemplateDatabase.  # noqa: E501
        :type: list[str]
        """

        self._oracle = oracle

    @property
    def postgres(self):
        """Gets the postgres of this ScanTemplateDatabase.  # noqa: E501

        Database name for PostgesSQL database instance.  # noqa: E501

        :return: The postgres of this ScanTemplateDatabase.  # noqa: E501
        :rtype: str
        """
        return self._postgres

    @postgres.setter
    def postgres(self, postgres):
        """Sets the postgres of this ScanTemplateDatabase.

        Database name for PostgesSQL database instance.  # noqa: E501

        :param postgres: The postgres of this ScanTemplateDatabase.  # noqa: E501
        :type: str
        """

        self._postgres = postgres

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
        if issubclass(ScanTemplateDatabase, dict):
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
        if not isinstance(other, ScanTemplateDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
