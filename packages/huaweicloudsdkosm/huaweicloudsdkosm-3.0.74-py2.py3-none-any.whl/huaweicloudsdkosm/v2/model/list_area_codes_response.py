# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAreaCodesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'area_code_list': 'list[AreaCodeSimpleInfoV2]'
    }

    attribute_map = {
        'area_code_list': 'area_code_list'
    }

    def __init__(self, area_code_list=None):
        """ListAreaCodesResponse - a model defined in huaweicloud sdk"""
        
        super(ListAreaCodesResponse, self).__init__()

        self._area_code_list = None
        self.discriminator = None

        if area_code_list is not None:
            self.area_code_list = area_code_list

    @property
    def area_code_list(self):
        """Gets the area_code_list of this ListAreaCodesResponse.

        国家码列表

        :return: The area_code_list of this ListAreaCodesResponse.
        :rtype: list[AreaCodeSimpleInfoV2]
        """
        return self._area_code_list

    @area_code_list.setter
    def area_code_list(self, area_code_list):
        """Sets the area_code_list of this ListAreaCodesResponse.

        国家码列表

        :param area_code_list: The area_code_list of this ListAreaCodesResponse.
        :type: list[AreaCodeSimpleInfoV2]
        """
        self._area_code_list = area_code_list

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
        if not isinstance(other, ListAreaCodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
