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

class License(object):
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
        'edition': 'str',
        'evaluation': 'bool',
        'expires': 'str',
        'features': 'Features',
        'limits': 'LicenseLimits',
        'links': 'list[Link]',
        'perpetual': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'edition': 'edition',
        'evaluation': 'evaluation',
        'expires': 'expires',
        'features': 'features',
        'limits': 'limits',
        'links': 'links',
        'perpetual': 'perpetual',
        'status': 'status'
    }

    def __init__(self, edition=None, evaluation=None, expires=None, features=None, limits=None, links=None, perpetual=None, status=None):  # noqa: E501
        """License - a model defined in Swagger"""  # noqa: E501
        self._edition = None
        self._evaluation = None
        self._expires = None
        self._features = None
        self._limits = None
        self._links = None
        self._perpetual = None
        self._status = None
        self.discriminator = None
        if edition is not None:
            self.edition = edition
        if evaluation is not None:
            self.evaluation = evaluation
        if expires is not None:
            self.expires = expires
        if features is not None:
            self.features = features
        if limits is not None:
            self.limits = limits
        if links is not None:
            self.links = links
        if perpetual is not None:
            self.perpetual = perpetual
        if status is not None:
            self.status = status

    @property
    def edition(self):
        """Gets the edition of this License.  # noqa: E501

        The edition of the product.  # noqa: E501

        :return: The edition of this License.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this License.

        The edition of the product.  # noqa: E501

        :param edition: The edition of this License.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def evaluation(self):
        """Gets the evaluation of this License.  # noqa: E501

        Whether the license is a time-restricted evaluation.  # noqa: E501

        :return: The evaluation of this License.  # noqa: E501
        :rtype: bool
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        """Sets the evaluation of this License.

        Whether the license is a time-restricted evaluation.  # noqa: E501

        :param evaluation: The evaluation of this License.  # noqa: E501
        :type: bool
        """

        self._evaluation = evaluation

    @property
    def expires(self):
        """Gets the expires of this License.  # noqa: E501

        The date and time the license expires.  # noqa: E501

        :return: The expires of this License.  # noqa: E501
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this License.

        The date and time the license expires.  # noqa: E501

        :param expires: The expires of this License.  # noqa: E501
        :type: str
        """

        self._expires = expires

    @property
    def features(self):
        """Gets the features of this License.  # noqa: E501


        :return: The features of this License.  # noqa: E501
        :rtype: Features
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this License.


        :param features: The features of this License.  # noqa: E501
        :type: Features
        """

        self._features = features

    @property
    def limits(self):
        """Gets the limits of this License.  # noqa: E501


        :return: The limits of this License.  # noqa: E501
        :rtype: LicenseLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this License.


        :param limits: The limits of this License.  # noqa: E501
        :type: LicenseLimits
        """

        self._limits = limits

    @property
    def links(self):
        """Gets the links of this License.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this License.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this License.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this License.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def perpetual(self):
        """Gets the perpetual of this License.  # noqa: E501

        Whether the license is perpetual.  # noqa: E501

        :return: The perpetual of this License.  # noqa: E501
        :rtype: bool
        """
        return self._perpetual

    @perpetual.setter
    def perpetual(self, perpetual):
        """Sets the perpetual of this License.

        Whether the license is perpetual.  # noqa: E501

        :param perpetual: The perpetual of this License.  # noqa: E501
        :type: bool
        """

        self._perpetual = perpetual

    @property
    def status(self):
        """Gets the status of this License.  # noqa: E501

        The status of the license.  # noqa: E501

        :return: The status of this License.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this License.

        The status of the license.  # noqa: E501

        :param status: The status of this License.  # noqa: E501
        :type: str
        """
        allowed_values = ["Activated", "Unlicensed", "Expired", "Evaluation Mode", "Revoked", "Unknown"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(License, dict):
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
        if not isinstance(other, License):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
