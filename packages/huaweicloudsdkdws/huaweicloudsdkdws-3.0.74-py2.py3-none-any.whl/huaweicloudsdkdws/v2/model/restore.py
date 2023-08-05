# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Restore:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'enterprise_project_id': 'str',
        'public_ip': 'PublicIp',
        'port': 'int',
        'vpc_id': 'str',
        'name': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'enterprise_project_id': 'enterprise_project_id',
        'public_ip': 'public_ip',
        'port': 'port',
        'vpc_id': 'vpc_id',
        'name': 'name',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, availability_zone=None, enterprise_project_id=None, public_ip=None, port=None, vpc_id=None, name=None, security_group_id=None, subnet_id=None):
        """Restore - a model defined in huaweicloud sdk"""
        
        

        self._availability_zone = None
        self._enterprise_project_id = None
        self._public_ip = None
        self._port = None
        self._vpc_id = None
        self._name = None
        self._security_group_id = None
        self._subnet_id = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if public_ip is not None:
            self.public_ip = public_ip
        if port is not None:
            self.port = port
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.name = name
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Restore.

        指定集群可用区。默认值与原集群相同

        :return: The availability_zone of this Restore.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Restore.

        指定集群可用区。默认值与原集群相同

        :param availability_zone: The availability_zone of this Restore.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Restore.

        企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。

        :return: The enterprise_project_id of this Restore.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Restore.

        企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。

        :param enterprise_project_id: The enterprise_project_id of this Restore.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def public_ip(self):
        """Gets the public_ip of this Restore.


        :return: The public_ip of this Restore.
        :rtype: PublicIp
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this Restore.


        :param public_ip: The public_ip of this Restore.
        :type: PublicIp
        """
        self._public_ip = public_ip

    @property
    def port(self):
        """Gets the port of this Restore.

        指定集群服务端口

        :return: The port of this Restore.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Restore.

        指定集群服务端口

        :param port: The port of this Restore.
        :type: int
        """
        self._port = port

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Restore.

        指定虚拟私有云ID，用于集群网络配置。默认值与原集群相同。

        :return: The vpc_id of this Restore.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Restore.

        指定虚拟私有云ID，用于集群网络配置。默认值与原集群相同。

        :param vpc_id: The vpc_id of this Restore.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def name(self):
        """Gets the name of this Restore.

        集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线，下划线，长度为4~64个字符。

        :return: The name of this Restore.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Restore.

        集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线，下划线，长度为4~64个字符。

        :param name: The name of this Restore.
        :type: str
        """
        self._name = name

    @property
    def security_group_id(self):
        """Gets the security_group_id of this Restore.

        指定安全组ID，用于集群网络配置。默认值与原集群相同。

        :return: The security_group_id of this Restore.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this Restore.

        指定安全组ID，用于集群网络配置。默认值与原集群相同。

        :param security_group_id: The security_group_id of this Restore.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this Restore.

        指定子网ID，用于集群网络配置。默认值与原集群相同。

        :return: The subnet_id of this Restore.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this Restore.

        指定子网ID，用于集群网络配置。默认值与原集群相同。

        :param subnet_id: The subnet_id of this Restore.
        :type: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, Restore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
