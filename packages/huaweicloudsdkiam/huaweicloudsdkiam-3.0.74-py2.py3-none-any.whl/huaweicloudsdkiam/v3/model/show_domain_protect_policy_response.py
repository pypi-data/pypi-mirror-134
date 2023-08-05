# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainProtectPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'protect_policy': 'ProtectPolicyResult'
    }

    attribute_map = {
        'protect_policy': 'protect_policy'
    }

    def __init__(self, protect_policy=None):
        """ShowDomainProtectPolicyResponse - a model defined in huaweicloud sdk"""
        
        super(ShowDomainProtectPolicyResponse, self).__init__()

        self._protect_policy = None
        self.discriminator = None

        if protect_policy is not None:
            self.protect_policy = protect_policy

    @property
    def protect_policy(self):
        """Gets the protect_policy of this ShowDomainProtectPolicyResponse.


        :return: The protect_policy of this ShowDomainProtectPolicyResponse.
        :rtype: ProtectPolicyResult
        """
        return self._protect_policy

    @protect_policy.setter
    def protect_policy(self, protect_policy):
        """Sets the protect_policy of this ShowDomainProtectPolicyResponse.


        :param protect_policy: The protect_policy of this ShowDomainProtectPolicyResponse.
        :type: ProtectPolicyResult
        """
        self._protect_policy = protect_policy

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
        if not isinstance(other, ShowDomainProtectPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
