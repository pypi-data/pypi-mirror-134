# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListL7RulesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'l7policy_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'compare_type': 'list[str]',
        'provisioning_status': 'list[str]',
        'invert': 'bool',
        'admin_state_up': 'bool',
        'value': 'list[str]',
        'key': 'list[str]',
        'type': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'l7policy_id': 'l7policy_id',
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'compare_type': 'compare_type',
        'provisioning_status': 'provisioning_status',
        'invert': 'invert',
        'admin_state_up': 'admin_state_up',
        'value': 'value',
        'key': 'key',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, l7policy_id=None, limit=None, marker=None, page_reverse=None, id=None, compare_type=None, provisioning_status=None, invert=None, admin_state_up=None, value=None, key=None, type=None, enterprise_project_id=None):
        """ListL7RulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._l7policy_id = None
        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._compare_type = None
        self._provisioning_status = None
        self._invert = None
        self._admin_state_up = None
        self._value = None
        self._key = None
        self._type = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.l7policy_id = l7policy_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if compare_type is not None:
            self.compare_type = compare_type
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if invert is not None:
            self.invert = invert
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if value is not None:
            self.value = value
        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def l7policy_id(self):
        """Gets the l7policy_id of this ListL7RulesRequest.

        策略ID。

        :return: The l7policy_id of this ListL7RulesRequest.
        :rtype: str
        """
        return self._l7policy_id

    @l7policy_id.setter
    def l7policy_id(self, l7policy_id):
        """Sets the l7policy_id of this ListL7RulesRequest.

        策略ID。

        :param l7policy_id: The l7policy_id of this ListL7RulesRequest.
        :type: str
        """
        self._l7policy_id = l7policy_id

    @property
    def limit(self):
        """Gets the limit of this ListL7RulesRequest.

        每页返回的个数。

        :return: The limit of this ListL7RulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListL7RulesRequest.

        每页返回的个数。

        :param limit: The limit of this ListL7RulesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListL7RulesRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListL7RulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListL7RulesRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListL7RulesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListL7RulesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。  使用说明： - 必须与limit一起使用。

        :return: The page_reverse of this ListL7RulesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListL7RulesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。  使用说明： - 必须与limit一起使用。

        :param page_reverse: The page_reverse of this ListL7RulesRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListL7RulesRequest.

        转发规则ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListL7RulesRequest.

        转发规则ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListL7RulesRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def compare_type(self):
        """Gets the compare_type of this ListL7RulesRequest.

        转发规则的匹配方式。  type为HOST_NAME时可以为EQUAL_TO。  type为PATH时可以为Perl类型的REGEX， STARTS_WITH，EQUAL_TO。  支持多值查询，查询条件格式：*compare_type=xxx&compare_type=xxx*。

        :return: The compare_type of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this ListL7RulesRequest.

        转发规则的匹配方式。  type为HOST_NAME时可以为EQUAL_TO。  type为PATH时可以为Perl类型的REGEX， STARTS_WITH，EQUAL_TO。  支持多值查询，查询条件格式：*compare_type=xxx&compare_type=xxx*。

        :param compare_type: The compare_type of this ListL7RulesRequest.
        :type: list[str]
        """
        self._compare_type = compare_type

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListL7RulesRequest.

        转发规则的配置状态。取值：ACTIVE 表示正常。  支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。

        :return: The provisioning_status of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListL7RulesRequest.

        转发规则的配置状态。取值：ACTIVE 表示正常。  支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。

        :param provisioning_status: The provisioning_status of this ListL7RulesRequest.
        :type: list[str]
        """
        self._provisioning_status = provisioning_status

    @property
    def invert(self):
        """Gets the invert of this ListL7RulesRequest.

        是否反向匹配。固定为false。该字段能更新但不会生效。

        :return: The invert of this ListL7RulesRequest.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this ListL7RulesRequest.

        是否反向匹配。固定为false。该字段能更新但不会生效。

        :param invert: The invert of this ListL7RulesRequest.
        :type: bool
        """
        self._invert = invert

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListL7RulesRequest.

        转发规则的管理状态，默认为true。  不支持该字段，请勿使用。

        :return: The admin_state_up of this ListL7RulesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListL7RulesRequest.

        转发规则的管理状态，默认为true。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this ListL7RulesRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def value(self):
        """Gets the value of this ListL7RulesRequest.

        匹配内容的值。  支持多值查询，查询条件格式：*value=xxx&value=xxx*。

        :return: The value of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListL7RulesRequest.

        匹配内容的值。  支持多值查询，查询条件格式：*value=xxx&value=xxx*。

        :param value: The value of this ListL7RulesRequest.
        :type: list[str]
        """
        self._value = value

    @property
    def key(self):
        """Gets the key of this ListL7RulesRequest.

        匹配内容的键值，用于标识规则。  支持多值查询，查询条件格式：*key=xxx&key=xxx*。  不支持该字段，请勿使用。

        :return: The key of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ListL7RulesRequest.

        匹配内容的键值，用于标识规则。  支持多值查询，查询条件格式：*key=xxx&key=xxx*。  不支持该字段，请勿使用。

        :param key: The key of this ListL7RulesRequest.
        :type: list[str]
        """
        self._key = key

    @property
    def type(self):
        """Gets the type of this ListL7RulesRequest.

        匹配类别，可以为HOST_NAME，PATH。  一个l7policy下创建的l7rule的type不能重复。  支持多值查询，查询条件格式：*type=xxx&type=xxx*。

        :return: The type of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListL7RulesRequest.

        匹配类别，可以为HOST_NAME，PATH。  一个l7policy下创建的l7rule的type不能重复。  支持多值查询，查询条件格式：*type=xxx&type=xxx*。

        :param type: The type of this ListL7RulesRequest.
        :type: list[str]
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListL7RulesRequest.

        企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The enterprise_project_id of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListL7RulesRequest.

        企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param enterprise_project_id: The enterprise_project_id of this ListL7RulesRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListL7RulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
