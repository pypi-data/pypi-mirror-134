# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHostListRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host_id_list': 'list[str]',
        'filter': 'GetHostListFilter'
    }

    attribute_map = {
        'host_id_list': 'host_id_list',
        'filter': 'filter'
    }

    def __init__(self, host_id_list=None, filter=None):
        """GetHostListRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._host_id_list = None
        self._filter = None
        self.discriminator = None

        if host_id_list is not None:
            self.host_id_list = host_id_list
        if filter is not None:
            self.filter = filter

    @property
    def host_id_list(self):
        """Gets the host_id_list of this GetHostListRequestBody.

        主机ID列表。可以根据主机ID列表进行批量过滤

        :return: The host_id_list of this GetHostListRequestBody.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this GetHostListRequestBody.

        主机ID列表。可以根据主机ID列表进行批量过滤

        :param host_id_list: The host_id_list of this GetHostListRequestBody.
        :type: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def filter(self):
        """Gets the filter of this GetHostListRequestBody.


        :return: The filter of this GetHostListRequestBody.
        :rtype: GetHostListFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this GetHostListRequestBody.


        :param filter: The filter of this GetHostListRequestBody.
        :type: GetHostListFilter
        """
        self._filter = filter

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
        if not isinstance(other, GetHostListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
