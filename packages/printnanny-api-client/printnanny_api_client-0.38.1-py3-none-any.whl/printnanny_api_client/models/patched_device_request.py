# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class PatchedDeviceRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'release_channel': 'ReleaseChannelEnum',
        'monitoring_active': 'bool',
        'hostname': 'str'
    }

    attribute_map = {
        'release_channel': 'release_channel',
        'monitoring_active': 'monitoring_active',
        'hostname': 'hostname'
    }

    def __init__(self, release_channel=None, monitoring_active=False, hostname=None, local_vars_configuration=None):  # noqa: E501
        """PatchedDeviceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._release_channel = None
        self._monitoring_active = None
        self._hostname = None
        self.discriminator = None

        self.release_channel = release_channel
        if monitoring_active is not None:
            self.monitoring_active = monitoring_active
        if hostname is not None:
            self.hostname = hostname

    @property
    def release_channel(self):
        """Gets the release_channel of this PatchedDeviceRequest.  # noqa: E501


        :return: The release_channel of this PatchedDeviceRequest.  # noqa: E501
        :rtype: ReleaseChannelEnum
        """
        return self._release_channel

    @release_channel.setter
    def release_channel(self, release_channel):
        """Sets the release_channel of this PatchedDeviceRequest.


        :param release_channel: The release_channel of this PatchedDeviceRequest.  # noqa: E501
        :type release_channel: ReleaseChannelEnum
        """

        self._release_channel = release_channel

    @property
    def monitoring_active(self):
        """Gets the monitoring_active of this PatchedDeviceRequest.  # noqa: E501


        :return: The monitoring_active of this PatchedDeviceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._monitoring_active

    @monitoring_active.setter
    def monitoring_active(self, monitoring_active):
        """Sets the monitoring_active of this PatchedDeviceRequest.


        :param monitoring_active: The monitoring_active of this PatchedDeviceRequest.  # noqa: E501
        :type monitoring_active: bool
        """

        self._monitoring_active = monitoring_active

    @property
    def hostname(self):
        """Gets the hostname of this PatchedDeviceRequest.  # noqa: E501

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :return: The hostname of this PatchedDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PatchedDeviceRequest.

        Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)  # noqa: E501

        :param hostname: The hostname of this PatchedDeviceRequest.  # noqa: E501
        :type hostname: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) > 255):
            raise ValueError("Invalid value for `hostname`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hostname is not None and len(hostname) < 1):
            raise ValueError("Invalid value for `hostname`, length must be greater than or equal to `1`")  # noqa: E501

        self._hostname = hostname

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchedDeviceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedDeviceRequest):
            return True

        return self.to_dict() != other.to_dict()
