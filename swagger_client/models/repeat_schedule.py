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

class RepeatSchedule(object):
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
        'day_of_week': 'str',
        'every': 'str',
        'interval': 'int',
        'last_day_of_month': 'bool',
        'week_of_month': 'int'
    }

    attribute_map = {
        'day_of_week': 'dayOfWeek',
        'every': 'every',
        'interval': 'interval',
        'last_day_of_month': 'lastDayOfMonth',
        'week_of_month': 'weekOfMonth'
    }

    def __init__(self, day_of_week=None, every=None, interval=None, last_day_of_month=None, week_of_month=None):  # noqa: E501
        """RepeatSchedule - a model defined in Swagger"""  # noqa: E501
        self._day_of_week = None
        self._every = None
        self._interval = None
        self._last_day_of_month = None
        self._week_of_month = None
        self.discriminator = None
        if day_of_week is not None:
            self.day_of_week = day_of_week
        self.every = every
        self.interval = interval
        if last_day_of_month is not None:
            self.last_day_of_month = last_day_of_month
        if week_of_month is not None:
            self.week_of_month = week_of_month

    @property
    def day_of_week(self):
        """Gets the day_of_week of this RepeatSchedule.  # noqa: E501

        The day of the week the scheduled task should repeat. This property only applies to schedules with a `every` value of `\"day-of-month\"`.  # noqa: E501

        :return: The day_of_week of this RepeatSchedule.  # noqa: E501
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this RepeatSchedule.

        The day of the week the scheduled task should repeat. This property only applies to schedules with a `every` value of `\"day-of-month\"`.  # noqa: E501

        :param day_of_week: The day_of_week of this RepeatSchedule.  # noqa: E501
        :type: str
        """

        self._day_of_week = day_of_week

    @property
    def every(self):
        """Gets the every of this RepeatSchedule.  # noqa: E501

        The frequency schedule repeats. Each value represents a different unit of time and is used in conjunction with the property `interval`. For example, a schedule can repeat hourly, daily, monthly, etc. The following table describes each supported value:  | Value | Description |  | ---------- | ---------------- |  | hour | Specifies the schedule repeats in hourly increments. |  | day | Specifies the schedule repeats in daily increments. |  | week | Specifies the schedule repeats in weekly increments. |  | date-of-month | Specifies the schedule repeats nth day of the `interval` month. Requires the property `dateOfMonth` to be specified. For example, if `dateOfMonth` is `17` and the `interval` is `2`, then the schedule will repeat every 2 months on the 17th day of the month. |  | day-of-month | Specifies the schedule repeats on a monthly interval but instead of a specific date being specified, the day of the week and week of the month are specified. Requires the properties `dayOfWeek` and `weekOfMonth` to be specified. For example, if `dayOfWeek` is `\"friday\"`, `weekOfMonth` is `3`, and the `interval` is `4`, then the schedule will repeat every 4 months on the 3rd Friday of the month. |    # noqa: E501

        :return: The every of this RepeatSchedule.  # noqa: E501
        :rtype: str
        """
        return self._every

    @every.setter
    def every(self, every):
        """Sets the every of this RepeatSchedule.

        The frequency schedule repeats. Each value represents a different unit of time and is used in conjunction with the property `interval`. For example, a schedule can repeat hourly, daily, monthly, etc. The following table describes each supported value:  | Value | Description |  | ---------- | ---------------- |  | hour | Specifies the schedule repeats in hourly increments. |  | day | Specifies the schedule repeats in daily increments. |  | week | Specifies the schedule repeats in weekly increments. |  | date-of-month | Specifies the schedule repeats nth day of the `interval` month. Requires the property `dateOfMonth` to be specified. For example, if `dateOfMonth` is `17` and the `interval` is `2`, then the schedule will repeat every 2 months on the 17th day of the month. |  | day-of-month | Specifies the schedule repeats on a monthly interval but instead of a specific date being specified, the day of the week and week of the month are specified. Requires the properties `dayOfWeek` and `weekOfMonth` to be specified. For example, if `dayOfWeek` is `\"friday\"`, `weekOfMonth` is `3`, and the `interval` is `4`, then the schedule will repeat every 4 months on the 3rd Friday of the month. |    # noqa: E501

        :param every: The every of this RepeatSchedule.  # noqa: E501
        :type: str
        """
        if every is None:
            raise ValueError("Invalid value for `every`, must not be `None`")  # noqa: E501

        self._every = every

    @property
    def interval(self):
        """Gets the interval of this RepeatSchedule.  # noqa: E501

        The interval time the schedule should repeat. The is depends on the value set in `every`. For example, if the value in property `every` is set to `\"day\"` and `interval` is set to `2`, then the schedule will repeat every 2 days.  # noqa: E501

        :return: The interval of this RepeatSchedule.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this RepeatSchedule.

        The interval time the schedule should repeat. The is depends on the value set in `every`. For example, if the value in property `every` is set to `\"day\"` and `interval` is set to `2`, then the schedule will repeat every 2 days.  # noqa: E501

        :param interval: The interval of this RepeatSchedule.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def last_day_of_month(self):
        """Gets the last_day_of_month of this RepeatSchedule.  # noqa: E501


        :return: The last_day_of_month of this RepeatSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._last_day_of_month

    @last_day_of_month.setter
    def last_day_of_month(self, last_day_of_month):
        """Sets the last_day_of_month of this RepeatSchedule.


        :param last_day_of_month: The last_day_of_month of this RepeatSchedule.  # noqa: E501
        :type: bool
        """

        self._last_day_of_month = last_day_of_month

    @property
    def week_of_month(self):
        """Gets the week_of_month of this RepeatSchedule.  # noqa: E501

        The week of the month the scheduled task should repeat. For This property only applies to schedules with a `every` value of `\"day-of-month\"`. Each week of the month is counted in 7-day increments. For example, week 1 consists of days 1-7 of the month while week 2 consists of days 8-14 of the month and so forth.  # noqa: E501

        :return: The week_of_month of this RepeatSchedule.  # noqa: E501
        :rtype: int
        """
        return self._week_of_month

    @week_of_month.setter
    def week_of_month(self, week_of_month):
        """Sets the week_of_month of this RepeatSchedule.

        The week of the month the scheduled task should repeat. For This property only applies to schedules with a `every` value of `\"day-of-month\"`. Each week of the month is counted in 7-day increments. For example, week 1 consists of days 1-7 of the month while week 2 consists of days 8-14 of the month and so forth.  # noqa: E501

        :param week_of_month: The week_of_month of this RepeatSchedule.  # noqa: E501
        :type: int
        """

        self._week_of_month = week_of_month

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
        if issubclass(RepeatSchedule, dict):
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
        if not isinstance(other, RepeatSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
