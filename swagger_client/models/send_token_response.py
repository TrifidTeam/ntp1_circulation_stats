# coding: utf-8

"""
    Neblio REST API Suite

    APIs for Interacting with NTP1 Tokens & The Neblio Blockchain  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SendTokenResponse(object):
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
        'tx_hex': 'str',
        'ntp1_output_indexes': 'list[float]',
        'multisig_outputs': 'list[float]'
    }

    attribute_map = {
        'tx_hex': 'txHex',
        'ntp1_output_indexes': 'ntp1OutputIndexes',
        'multisig_outputs': 'multisigOutputs'
    }

    def __init__(self, tx_hex=None, ntp1_output_indexes=None, multisig_outputs=None):  # noqa: E501
        """SendTokenResponse - a model defined in Swagger"""  # noqa: E501

        self._tx_hex = None
        self._ntp1_output_indexes = None
        self._multisig_outputs = None
        self.discriminator = None

        if tx_hex is not None:
            self.tx_hex = tx_hex
        if ntp1_output_indexes is not None:
            self.ntp1_output_indexes = ntp1_output_indexes
        if multisig_outputs is not None:
            self.multisig_outputs = multisig_outputs

    @property
    def tx_hex(self):
        """Gets the tx_hex of this SendTokenResponse.  # noqa: E501

        Unsigned, raw transaction hex of the transaction to send the token  # noqa: E501

        :return: The tx_hex of this SendTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._tx_hex

    @tx_hex.setter
    def tx_hex(self, tx_hex):
        """Sets the tx_hex of this SendTokenResponse.

        Unsigned, raw transaction hex of the transaction to send the token  # noqa: E501

        :param tx_hex: The tx_hex of this SendTokenResponse.  # noqa: E501
        :type: str
        """

        self._tx_hex = tx_hex

    @property
    def ntp1_output_indexes(self):
        """Gets the ntp1_output_indexes of this SendTokenResponse.  # noqa: E501

        Array of indexes transfering NTP1 tokens  # noqa: E501

        :return: The ntp1_output_indexes of this SendTokenResponse.  # noqa: E501
        :rtype: list[float]
        """
        return self._ntp1_output_indexes

    @ntp1_output_indexes.setter
    def ntp1_output_indexes(self, ntp1_output_indexes):
        """Sets the ntp1_output_indexes of this SendTokenResponse.

        Array of indexes transfering NTP1 tokens  # noqa: E501

        :param ntp1_output_indexes: The ntp1_output_indexes of this SendTokenResponse.  # noqa: E501
        :type: list[float]
        """

        self._ntp1_output_indexes = ntp1_output_indexes

    @property
    def multisig_outputs(self):
        """Gets the multisig_outputs of this SendTokenResponse.  # noqa: E501

        Array of indexes of multisig outputs  # noqa: E501

        :return: The multisig_outputs of this SendTokenResponse.  # noqa: E501
        :rtype: list[float]
        """
        return self._multisig_outputs

    @multisig_outputs.setter
    def multisig_outputs(self, multisig_outputs):
        """Sets the multisig_outputs of this SendTokenResponse.

        Array of indexes of multisig outputs  # noqa: E501

        :param multisig_outputs: The multisig_outputs of this SendTokenResponse.  # noqa: E501
        :type: list[float]
        """

        self._multisig_outputs = multisig_outputs

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
