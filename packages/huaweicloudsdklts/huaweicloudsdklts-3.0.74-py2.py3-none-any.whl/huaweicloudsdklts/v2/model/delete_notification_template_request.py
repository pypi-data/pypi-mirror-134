# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNotificationTemplateRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'body': 'DeleteNotificationTemplateBody'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'body': 'body'
    }

    def __init__(self, domain_id=None, body=None):
        """DeleteNotificationTemplateRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        """Gets the domain_id of this DeleteNotificationTemplateRequest.

        账号id，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :return: The domain_id of this DeleteNotificationTemplateRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DeleteNotificationTemplateRequest.

        账号id，获取方式请参见：获取账号ID、项目ID、日志组ID、日志流ID（https://support.huaweicloud.com/api-lts/lts_api_0006.html）。

        :param domain_id: The domain_id of this DeleteNotificationTemplateRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def body(self):
        """Gets the body of this DeleteNotificationTemplateRequest.


        :return: The body of this DeleteNotificationTemplateRequest.
        :rtype: DeleteNotificationTemplateBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteNotificationTemplateRequest.


        :param body: The body of this DeleteNotificationTemplateRequest.
        :type: DeleteNotificationTemplateBody
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
        if not isinstance(other, DeleteNotificationTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
