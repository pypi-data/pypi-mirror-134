# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'taskinfo': 'TaskInfo'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'taskinfo': 'taskinfo'
    }

    def __init__(self, code=None, message=None, taskinfo=None):
        """ShowTaskResponse - a model defined in huaweicloud sdk"""
        
        super(ShowTaskResponse, self).__init__()

        self._code = None
        self._message = None
        self._taskinfo = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if taskinfo is not None:
            self.taskinfo = taskinfo

    @property
    def code(self):
        """Gets the code of this ShowTaskResponse.

        code

        :return: The code of this ShowTaskResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowTaskResponse.

        code

        :param code: The code of this ShowTaskResponse.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ShowTaskResponse.

        message

        :return: The message of this ShowTaskResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowTaskResponse.

        message

        :param message: The message of this ShowTaskResponse.
        :type: str
        """
        self._message = message

    @property
    def taskinfo(self):
        """Gets the taskinfo of this ShowTaskResponse.


        :return: The taskinfo of this ShowTaskResponse.
        :rtype: TaskInfo
        """
        return self._taskinfo

    @taskinfo.setter
    def taskinfo(self, taskinfo):
        """Sets the taskinfo of this ShowTaskResponse.


        :param taskinfo: The taskinfo of this ShowTaskResponse.
        :type: TaskInfo
        """
        self._taskinfo = taskinfo

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
        if not isinstance(other, ShowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
