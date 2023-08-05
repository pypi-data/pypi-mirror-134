# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizerResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'authorizer_type': 'str',
        'authorizer_uri': 'str',
        'identities': 'list[Identity]',
        'ttl': 'int',
        'user_data': 'str',
        'ld_api_id': 'str',
        'need_body': 'bool',
        'id': 'str',
        'create_time': 'datetime',
        'roma_app_id': 'str',
        'roma_app_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'authorizer_type': 'authorizer_type',
        'authorizer_uri': 'authorizer_uri',
        'identities': 'identities',
        'ttl': 'ttl',
        'user_data': 'user_data',
        'ld_api_id': 'ld_api_id',
        'need_body': 'need_body',
        'id': 'id',
        'create_time': 'create_time',
        'roma_app_id': 'roma_app_id',
        'roma_app_name': 'roma_app_name'
    }

    def __init__(self, name=None, type=None, authorizer_type=None, authorizer_uri=None, identities=None, ttl=None, user_data=None, ld_api_id=None, need_body=None, id=None, create_time=None, roma_app_id=None, roma_app_name=None):
        """AuthorizerResp - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._type = None
        self._authorizer_type = None
        self._authorizer_uri = None
        self._identities = None
        self._ttl = None
        self._user_data = None
        self._ld_api_id = None
        self._need_body = None
        self._id = None
        self._create_time = None
        self._roma_app_id = None
        self._roma_app_name = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.authorizer_type = authorizer_type
        self.authorizer_uri = authorizer_uri
        if identities is not None:
            self.identities = identities
        if ttl is not None:
            self.ttl = ttl
        if user_data is not None:
            self.user_data = user_data
        if ld_api_id is not None:
            self.ld_api_id = ld_api_id
        if need_body is not None:
            self.need_body = need_body
        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id
        if roma_app_name is not None:
            self.roma_app_name = roma_app_name

    @property
    def name(self):
        """Gets the name of this AuthorizerResp.

        自定义认证的名称。 长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、“_”组成，且只能以英文或中文开头。 

        :return: The name of this AuthorizerResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthorizerResp.

        自定义认证的名称。 长度为3 ~ 64位的字符串，字符串由中文、英文字母、数字、“_”组成，且只能以英文或中文开头。 

        :param name: The name of this AuthorizerResp.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this AuthorizerResp.

        自定义认证类型  - FRONTEND：前端 - BACKEND：后端  不支持修改

        :return: The type of this AuthorizerResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AuthorizerResp.

        自定义认证类型  - FRONTEND：前端 - BACKEND：后端  不支持修改

        :param type: The type of this AuthorizerResp.
        :type: str
        """
        self._type = type

    @property
    def authorizer_type(self):
        """Gets the authorizer_type of this AuthorizerResp.

        只能为：FUNC

        :return: The authorizer_type of this AuthorizerResp.
        :rtype: str
        """
        return self._authorizer_type

    @authorizer_type.setter
    def authorizer_type(self, authorizer_type):
        """Sets the authorizer_type of this AuthorizerResp.

        只能为：FUNC

        :param authorizer_type: The authorizer_type of this AuthorizerResp.
        :type: str
        """
        self._authorizer_type = authorizer_type

    @property
    def authorizer_uri(self):
        """Gets the authorizer_uri of this AuthorizerResp.

        函数地址。

        :return: The authorizer_uri of this AuthorizerResp.
        :rtype: str
        """
        return self._authorizer_uri

    @authorizer_uri.setter
    def authorizer_uri(self, authorizer_uri):
        """Sets the authorizer_uri of this AuthorizerResp.

        函数地址。

        :param authorizer_uri: The authorizer_uri of this AuthorizerResp.
        :type: str
        """
        self._authorizer_uri = authorizer_uri

    @property
    def identities(self):
        """Gets the identities of this AuthorizerResp.

        认证来源

        :return: The identities of this AuthorizerResp.
        :rtype: list[Identity]
        """
        return self._identities

    @identities.setter
    def identities(self, identities):
        """Sets the identities of this AuthorizerResp.

        认证来源

        :param identities: The identities of this AuthorizerResp.
        :type: list[Identity]
        """
        self._identities = identities

    @property
    def ttl(self):
        """Gets the ttl of this AuthorizerResp.

        缓存时间

        :return: The ttl of this AuthorizerResp.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this AuthorizerResp.

        缓存时间

        :param ttl: The ttl of this AuthorizerResp.
        :type: int
        """
        self._ttl = ttl

    @property
    def user_data(self):
        """Gets the user_data of this AuthorizerResp.

        用户数据

        :return: The user_data of this AuthorizerResp.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this AuthorizerResp.

        用户数据

        :param user_data: The user_data of this AuthorizerResp.
        :type: str
        """
        self._user_data = user_data

    @property
    def ld_api_id(self):
        """Gets the ld_api_id of this AuthorizerResp.

        自定义后端服务ID。  暂不支持

        :return: The ld_api_id of this AuthorizerResp.
        :rtype: str
        """
        return self._ld_api_id

    @ld_api_id.setter
    def ld_api_id(self, ld_api_id):
        """Sets the ld_api_id of this AuthorizerResp.

        自定义后端服务ID。  暂不支持

        :param ld_api_id: The ld_api_id of this AuthorizerResp.
        :type: str
        """
        self._ld_api_id = ld_api_id

    @property
    def need_body(self):
        """Gets the need_body of this AuthorizerResp.

        是否发送body

        :return: The need_body of this AuthorizerResp.
        :rtype: bool
        """
        return self._need_body

    @need_body.setter
    def need_body(self, need_body):
        """Sets the need_body of this AuthorizerResp.

        是否发送body

        :param need_body: The need_body of this AuthorizerResp.
        :type: bool
        """
        self._need_body = need_body

    @property
    def id(self):
        """Gets the id of this AuthorizerResp.

        自定义认证编号

        :return: The id of this AuthorizerResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthorizerResp.

        自定义认证编号

        :param id: The id of this AuthorizerResp.
        :type: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this AuthorizerResp.

        创建时间

        :return: The create_time of this AuthorizerResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AuthorizerResp.

        创建时间

        :param create_time: The create_time of this AuthorizerResp.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this AuthorizerResp.

        自定义认证所属应用编号  暂不支持

        :return: The roma_app_id of this AuthorizerResp.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this AuthorizerResp.

        自定义认证所属应用编号  暂不支持

        :param roma_app_id: The roma_app_id of this AuthorizerResp.
        :type: str
        """
        self._roma_app_id = roma_app_id

    @property
    def roma_app_name(self):
        """Gets the roma_app_name of this AuthorizerResp.

        自定义认证所属应用名称  暂不支持

        :return: The roma_app_name of this AuthorizerResp.
        :rtype: str
        """
        return self._roma_app_name

    @roma_app_name.setter
    def roma_app_name(self, roma_app_name):
        """Sets the roma_app_name of this AuthorizerResp.

        自定义认证所属应用名称  暂不支持

        :param roma_app_name: The roma_app_name of this AuthorizerResp.
        :type: str
        """
        self._roma_app_name = roma_app_name

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
        if not isinstance(other, AuthorizerResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
