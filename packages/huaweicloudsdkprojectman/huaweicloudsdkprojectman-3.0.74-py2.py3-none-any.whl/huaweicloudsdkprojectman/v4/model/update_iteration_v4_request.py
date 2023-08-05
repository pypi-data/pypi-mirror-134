# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIterationV4Request:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'iteration_id': 'int',
        'body': 'UpdateIterationRequestV4'
    }

    attribute_map = {
        'project_id': 'project_id',
        'iteration_id': 'iteration_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, iteration_id=None, body=None):
        """UpdateIterationV4Request - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._iteration_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.iteration_id = iteration_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this UpdateIterationV4Request.

        devcloud的项目id

        :return: The project_id of this UpdateIterationV4Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdateIterationV4Request.

        devcloud的项目id

        :param project_id: The project_id of this UpdateIterationV4Request.
        :type: str
        """
        self._project_id = project_id

    @property
    def iteration_id(self):
        """Gets the iteration_id of this UpdateIterationV4Request.

        迭代id

        :return: The iteration_id of this UpdateIterationV4Request.
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this UpdateIterationV4Request.

        迭代id

        :param iteration_id: The iteration_id of this UpdateIterationV4Request.
        :type: int
        """
        self._iteration_id = iteration_id

    @property
    def body(self):
        """Gets the body of this UpdateIterationV4Request.


        :return: The body of this UpdateIterationV4Request.
        :rtype: UpdateIterationRequestV4
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateIterationV4Request.


        :param body: The body of this UpdateIterationV4Request.
        :type: UpdateIterationRequestV4
        """
        self._body = body

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
        if not isinstance(other, UpdateIterationV4Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
