# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePodDeployment:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'replicas': 'int',
        'template': 'PodRequest'
    }

    attribute_map = {
        'replicas': 'replicas',
        'template': 'template'
    }

    def __init__(self, replicas=None, template=None):
        """UpdatePodDeployment - a model defined in huaweicloud sdk"""
        
        

        self._replicas = None
        self._template = None
        self.discriminator = None

        self.replicas = replicas
        self.template = template

    @property
    def replicas(self):
        """Gets the replicas of this UpdatePodDeployment.

        应用部署副本数，只能为1

        :return: The replicas of this UpdatePodDeployment.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this UpdatePodDeployment.

        应用部署副本数，只能为1

        :param replicas: The replicas of this UpdatePodDeployment.
        :type: int
        """
        self._replicas = replicas

    @property
    def template(self):
        """Gets the template of this UpdatePodDeployment.


        :return: The template of this UpdatePodDeployment.
        :rtype: PodRequest
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this UpdatePodDeployment.


        :param template: The template of this UpdatePodDeployment.
        :type: PodRequest
        """
        self._template = template

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
        if not isinstance(other, UpdatePodDeployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
