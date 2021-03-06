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

class PolicyControl(object):
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
        'cce_item_id': 'str',
        'cce_platform': 'str',
        'control_name': 'str',
        'id': 'str',
        'links': 'list[Link]',
        'published_date': 'int'
    }

    attribute_map = {
        'cce_item_id': 'cceItemId',
        'cce_platform': 'ccePlatform',
        'control_name': 'controlName',
        'id': 'id',
        'links': 'links',
        'published_date': 'publishedDate'
    }

    def __init__(self, cce_item_id=None, cce_platform=None, control_name=None, id=None, links=None, published_date=None):  # noqa: E501
        """PolicyControl - a model defined in Swagger"""  # noqa: E501
        self._cce_item_id = None
        self._cce_platform = None
        self._control_name = None
        self._id = None
        self._links = None
        self._published_date = None
        self.discriminator = None
        if cce_item_id is not None:
            self.cce_item_id = cce_item_id
        if cce_platform is not None:
            self.cce_platform = cce_platform
        if control_name is not None:
            self.control_name = control_name
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if published_date is not None:
            self.published_date = published_date

    @property
    def cce_item_id(self):
        """Gets the cce_item_id of this PolicyControl.  # noqa: E501

        The identifier of the CCE item.  # noqa: E501

        :return: The cce_item_id of this PolicyControl.  # noqa: E501
        :rtype: str
        """
        return self._cce_item_id

    @cce_item_id.setter
    def cce_item_id(self, cce_item_id):
        """Sets the cce_item_id of this PolicyControl.

        The identifier of the CCE item.  # noqa: E501

        :param cce_item_id: The cce_item_id of this PolicyControl.  # noqa: E501
        :type: str
        """

        self._cce_item_id = cce_item_id

    @property
    def cce_platform(self):
        """Gets the cce_platform of this PolicyControl.  # noqa: E501

        The platform of the CCE.  # noqa: E501

        :return: The cce_platform of this PolicyControl.  # noqa: E501
        :rtype: str
        """
        return self._cce_platform

    @cce_platform.setter
    def cce_platform(self, cce_platform):
        """Sets the cce_platform of this PolicyControl.

        The platform of the CCE.  # noqa: E501

        :param cce_platform: The cce_platform of this PolicyControl.  # noqa: E501
        :type: str
        """

        self._cce_platform = cce_platform

    @property
    def control_name(self):
        """Gets the control_name of this PolicyControl.  # noqa: E501

        The name of the control mapping.  # noqa: E501

        :return: The control_name of this PolicyControl.  # noqa: E501
        :rtype: str
        """
        return self._control_name

    @control_name.setter
    def control_name(self, control_name):
        """Sets the control_name of this PolicyControl.

        The name of the control mapping.  # noqa: E501

        :param control_name: The control_name of this PolicyControl.  # noqa: E501
        :type: str
        """

        self._control_name = control_name

    @property
    def id(self):
        """Gets the id of this PolicyControl.  # noqa: E501

        The textual representation of the control identifier.  # noqa: E501

        :return: The id of this PolicyControl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyControl.

        The textual representation of the control identifier.  # noqa: E501

        :param id: The id of this PolicyControl.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this PolicyControl.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this PolicyControl.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyControl.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this PolicyControl.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def published_date(self):
        """Gets the published_date of this PolicyControl.  # noqa: E501

        The published date of the control mapping.  # noqa: E501

        :return: The published_date of this PolicyControl.  # noqa: E501
        :rtype: int
        """
        return self._published_date

    @published_date.setter
    def published_date(self, published_date):
        """Sets the published_date of this PolicyControl.

        The published date of the control mapping.  # noqa: E501

        :param published_date: The published_date of this PolicyControl.  # noqa: E501
        :type: int
        """

        self._published_date = published_date

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
        if issubclass(PolicyControl, dict):
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
        if not isinstance(other, PolicyControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
