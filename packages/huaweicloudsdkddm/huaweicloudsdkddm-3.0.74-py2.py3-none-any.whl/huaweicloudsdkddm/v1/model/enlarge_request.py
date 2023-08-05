# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnlargeRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'node_number': 'int'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'node_number': 'node_number'
    }

    def __init__(self, flavor_id=None, node_number=None):
        """EnlargeRequest - a model defined in huaweicloud sdk"""
        
        

        self._flavor_id = None
        self._node_number = None
        self.discriminator = None

        self.flavor_id = flavor_id
        self.node_number = node_number

    @property
    def flavor_id(self):
        """Gets the flavor_id of this EnlargeRequest.

        当前进行节点扩容的DDM实例底层虚机规格id

        :return: The flavor_id of this EnlargeRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this EnlargeRequest.

        当前进行节点扩容的DDM实例底层虚机规格id

        :param flavor_id: The flavor_id of this EnlargeRequest.
        :type: str
        """
        self._flavor_id = flavor_id

    @property
    def node_number(self):
        """Gets the node_number of this EnlargeRequest.

        需要扩容的节点个数

        :return: The node_number of this EnlargeRequest.
        :rtype: int
        """
        return self._node_number

    @node_number.setter
    def node_number(self, node_number):
        """Sets the node_number of this EnlargeRequest.

        需要扩容的节点个数

        :param node_number: The node_number of this EnlargeRequest.
        :type: int
        """
        self._node_number = node_number

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
        if not isinstance(other, EnlargeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
