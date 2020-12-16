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

class UserAccount(object):
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
        'full_name': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'full_name': 'fullName',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, full_name=None, id=None, name=None):  # noqa: E501
        """UserAccount - a model defined in Swagger"""  # noqa: E501
        self._full_name = None
        self._id = None
        self._name = None
        self.discriminator = None
        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        self.name = name

    @property
    def full_name(self):
        """Gets the full_name of this UserAccount.  # noqa: E501

        The full name of the user account.  # noqa: E501

        :return: The full_name of this UserAccount.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserAccount.

        The full name of the user account.  # noqa: E501

        :param full_name: The full_name of this UserAccount.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this UserAccount.  # noqa: E501

        The identifier of the user account.  # noqa: E501

        :return: The id of this UserAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAccount.

        The identifier of the user account.  # noqa: E501

        :param id: The id of this UserAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserAccount.  # noqa: E501

        The name of the user account.  # noqa: E501

        :return: The name of this UserAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserAccount.

        The name of the user account.  # noqa: E501

        :param name: The name of this UserAccount.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(UserAccount, dict):
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
        if not isinstance(other, UserAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
