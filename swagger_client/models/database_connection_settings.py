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

class DatabaseConnectionSettings(object):
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
        'maximum_administration_pool_size': 'int',
        'maximum_pool_size': 'int',
        'maximum_prepared_statement_pool_size': 'int'
    }

    attribute_map = {
        'maximum_administration_pool_size': 'maximumAdministrationPoolSize',
        'maximum_pool_size': 'maximumPoolSize',
        'maximum_prepared_statement_pool_size': 'maximumPreparedStatementPoolSize'
    }

    def __init__(self, maximum_administration_pool_size=None, maximum_pool_size=None, maximum_prepared_statement_pool_size=None):  # noqa: E501
        """DatabaseConnectionSettings - a model defined in Swagger"""  # noqa: E501
        self._maximum_administration_pool_size = None
        self._maximum_pool_size = None
        self._maximum_prepared_statement_pool_size = None
        self.discriminator = None
        if maximum_administration_pool_size is not None:
            self.maximum_administration_pool_size = maximum_administration_pool_size
        if maximum_pool_size is not None:
            self.maximum_pool_size = maximum_pool_size
        if maximum_prepared_statement_pool_size is not None:
            self.maximum_prepared_statement_pool_size = maximum_prepared_statement_pool_size

    @property
    def maximum_administration_pool_size(self):
        """Gets the maximum_administration_pool_size of this DatabaseConnectionSettings.  # noqa: E501

        The maximum number of administrative connections in the connection pool. -1 means unlimited.  # noqa: E501

        :return: The maximum_administration_pool_size of this DatabaseConnectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._maximum_administration_pool_size

    @maximum_administration_pool_size.setter
    def maximum_administration_pool_size(self, maximum_administration_pool_size):
        """Sets the maximum_administration_pool_size of this DatabaseConnectionSettings.

        The maximum number of administrative connections in the connection pool. -1 means unlimited.  # noqa: E501

        :param maximum_administration_pool_size: The maximum_administration_pool_size of this DatabaseConnectionSettings.  # noqa: E501
        :type: int
        """

        self._maximum_administration_pool_size = maximum_administration_pool_size

    @property
    def maximum_pool_size(self):
        """Gets the maximum_pool_size of this DatabaseConnectionSettings.  # noqa: E501

        ${settings.database.connection.max}  # noqa: E501

        :return: The maximum_pool_size of this DatabaseConnectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._maximum_pool_size

    @maximum_pool_size.setter
    def maximum_pool_size(self, maximum_pool_size):
        """Sets the maximum_pool_size of this DatabaseConnectionSettings.

        ${settings.database.connection.max}  # noqa: E501

        :param maximum_pool_size: The maximum_pool_size of this DatabaseConnectionSettings.  # noqa: E501
        :type: int
        """

        self._maximum_pool_size = maximum_pool_size

    @property
    def maximum_prepared_statement_pool_size(self):
        """Gets the maximum_prepared_statement_pool_size of this DatabaseConnectionSettings.  # noqa: E501

        The maximum number of prepared statements in the prepared statement pool. -1 means unlimited.  # noqa: E501

        :return: The maximum_prepared_statement_pool_size of this DatabaseConnectionSettings.  # noqa: E501
        :rtype: int
        """
        return self._maximum_prepared_statement_pool_size

    @maximum_prepared_statement_pool_size.setter
    def maximum_prepared_statement_pool_size(self, maximum_prepared_statement_pool_size):
        """Sets the maximum_prepared_statement_pool_size of this DatabaseConnectionSettings.

        The maximum number of prepared statements in the prepared statement pool. -1 means unlimited.  # noqa: E501

        :param maximum_prepared_statement_pool_size: The maximum_prepared_statement_pool_size of this DatabaseConnectionSettings.  # noqa: E501
        :type: int
        """

        self._maximum_prepared_statement_pool_size = maximum_prepared_statement_pool_size

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
        if issubclass(DatabaseConnectionSettings, dict):
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
        if not isinstance(other, DatabaseConnectionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
