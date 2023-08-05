# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryError:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, error_code=None, error_message=None):
        """QueryError - a model defined in huaweicloud sdk"""
        
        

        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this QueryError.

        错误编码。

        :return: The error_code of this QueryError.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryError.

        错误编码。

        :param error_code: The error_code of this QueryError.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this QueryError.

        错误信息。

        :return: The error_message of this QueryError.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this QueryError.

        错误信息。

        :param error_message: The error_message of this QueryError.
        :type: str
        """
        self._error_message = error_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
