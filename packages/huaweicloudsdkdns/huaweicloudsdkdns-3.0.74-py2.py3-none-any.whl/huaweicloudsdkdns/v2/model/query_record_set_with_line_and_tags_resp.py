# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRecordSetWithLineAndTagsResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'zone_id': 'str',
        'zone_name': 'str',
        'type': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'created_at': 'str',
        'updated_at': 'str',
        'status': 'str',
        'default': 'bool',
        'project_id': 'str',
        'links': 'PageLink',
        'tags': 'list[Tag]',
        'line': 'str',
        'weight': 'int',
        'health_check_id': 'str',
        'alias_target': 'AliasTarget'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'zone_id': 'zone_id',
        'zone_name': 'zone_name',
        'type': 'type',
        'ttl': 'ttl',
        'records': 'records',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'default': 'default',
        'project_id': 'project_id',
        'links': 'links',
        'tags': 'tags',
        'line': 'line',
        'weight': 'weight',
        'health_check_id': 'health_check_id',
        'alias_target': 'alias_target'
    }

    def __init__(self, id=None, name=None, description=None, zone_id=None, zone_name=None, type=None, ttl=None, records=None, created_at=None, updated_at=None, status=None, default=None, project_id=None, links=None, tags=None, line=None, weight=None, health_check_id=None, alias_target=None):
        """QueryRecordSetWithLineAndTagsResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._description = None
        self._zone_id = None
        self._zone_name = None
        self._type = None
        self._ttl = None
        self._records = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._default = None
        self._project_id = None
        self._links = None
        self._tags = None
        self._line = None
        self._weight = None
        self._health_check_id = None
        self._alias_target = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name
        if type is not None:
            self.type = type
        if ttl is not None:
            self.ttl = ttl
        if records is not None:
            self.records = records
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if default is not None:
            self.default = default
        if project_id is not None:
            self.project_id = project_id
        if links is not None:
            self.links = links
        if tags is not None:
            self.tags = tags
        if line is not None:
            self.line = line
        if weight is not None:
            self.weight = weight
        if health_check_id is not None:
            self.health_check_id = health_check_id
        if alias_target is not None:
            self.alias_target = alias_target

    @property
    def id(self):
        """Gets the id of this QueryRecordSetWithLineAndTagsResp.

        Record Set的ID。

        :return: The id of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryRecordSetWithLineAndTagsResp.

        Record Set的ID。

        :param id: The id of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this QueryRecordSetWithLineAndTagsResp.

        Record Set的名称。

        :return: The name of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryRecordSetWithLineAndTagsResp.

        Record Set的名称。

        :param name: The name of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this QueryRecordSetWithLineAndTagsResp.

        Record Set的描述信息。

        :return: The description of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryRecordSetWithLineAndTagsResp.

        Record Set的描述信息。

        :param description: The description of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._description = description

    @property
    def zone_id(self):
        """Gets the zone_id of this QueryRecordSetWithLineAndTagsResp.

        托管该记录的zone_id。

        :return: The zone_id of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this QueryRecordSetWithLineAndTagsResp.

        托管该记录的zone_id。

        :param zone_id: The zone_id of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this QueryRecordSetWithLineAndTagsResp.

        托管该记录的zone_name。

        :return: The zone_name of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this QueryRecordSetWithLineAndTagsResp.

        托管该记录的zone_name。

        :param zone_name: The zone_name of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._zone_name = zone_name

    @property
    def type(self):
        """Gets the type of this QueryRecordSetWithLineAndTagsResp.

        记录类型。

        :return: The type of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryRecordSetWithLineAndTagsResp.

        记录类型。

        :param type: The type of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._type = type

    @property
    def ttl(self):
        """Gets the ttl of this QueryRecordSetWithLineAndTagsResp.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :return: The ttl of this QueryRecordSetWithLineAndTagsResp.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this QueryRecordSetWithLineAndTagsResp.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :param ttl: The ttl of this QueryRecordSetWithLineAndTagsResp.
        :type: int
        """
        self._ttl = ttl

    @property
    def records(self):
        """Gets the records of this QueryRecordSetWithLineAndTagsResp.

        域名解析后的值。

        :return: The records of this QueryRecordSetWithLineAndTagsResp.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this QueryRecordSetWithLineAndTagsResp.

        域名解析后的值。

        :param records: The records of this QueryRecordSetWithLineAndTagsResp.
        :type: list[str]
        """
        self._records = records

    @property
    def created_at(self):
        """Gets the created_at of this QueryRecordSetWithLineAndTagsResp.

        创建时间。

        :return: The created_at of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this QueryRecordSetWithLineAndTagsResp.

        创建时间。

        :param created_at: The created_at of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this QueryRecordSetWithLineAndTagsResp.

        更新时间。

        :return: The updated_at of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this QueryRecordSetWithLineAndTagsResp.

        更新时间。

        :param updated_at: The updated_at of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this QueryRecordSetWithLineAndTagsResp.

        资源状态。

        :return: The status of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryRecordSetWithLineAndTagsResp.

        资源状态。

        :param status: The status of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._status = status

    @property
    def default(self):
        """Gets the default of this QueryRecordSetWithLineAndTagsResp.

        标识是否由系统默认生成，系统默认生成的Record Set不能删除。

        :return: The default of this QueryRecordSetWithLineAndTagsResp.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this QueryRecordSetWithLineAndTagsResp.

        标识是否由系统默认生成，系统默认生成的Record Set不能删除。

        :param default: The default of this QueryRecordSetWithLineAndTagsResp.
        :type: bool
        """
        self._default = default

    @property
    def project_id(self):
        """Gets the project_id of this QueryRecordSetWithLineAndTagsResp.

        该Record Set所属的项目ID。

        :return: The project_id of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this QueryRecordSetWithLineAndTagsResp.

        该Record Set所属的项目ID。

        :param project_id: The project_id of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._project_id = project_id

    @property
    def links(self):
        """Gets the links of this QueryRecordSetWithLineAndTagsResp.


        :return: The links of this QueryRecordSetWithLineAndTagsResp.
        :rtype: PageLink
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this QueryRecordSetWithLineAndTagsResp.


        :param links: The links of this QueryRecordSetWithLineAndTagsResp.
        :type: PageLink
        """
        self._links = links

    @property
    def tags(self):
        """Gets the tags of this QueryRecordSetWithLineAndTagsResp.

        资源标签。

        :return: The tags of this QueryRecordSetWithLineAndTagsResp.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryRecordSetWithLineAndTagsResp.

        资源标签。

        :param tags: The tags of this QueryRecordSetWithLineAndTagsResp.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def line(self):
        """Gets the line of this QueryRecordSetWithLineAndTagsResp.

        解析线路ID。

        :return: The line of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this QueryRecordSetWithLineAndTagsResp.

        解析线路ID。

        :param line: The line of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._line = line

    @property
    def weight(self):
        """Gets the weight of this QueryRecordSetWithLineAndTagsResp.

        解析记录的权重。

        :return: The weight of this QueryRecordSetWithLineAndTagsResp.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this QueryRecordSetWithLineAndTagsResp.

        解析记录的权重。

        :param weight: The weight of this QueryRecordSetWithLineAndTagsResp.
        :type: int
        """
        self._weight = weight

    @property
    def health_check_id(self):
        """Gets the health_check_id of this QueryRecordSetWithLineAndTagsResp.

        健康检查ID。

        :return: The health_check_id of this QueryRecordSetWithLineAndTagsResp.
        :rtype: str
        """
        return self._health_check_id

    @health_check_id.setter
    def health_check_id(self, health_check_id):
        """Sets the health_check_id of this QueryRecordSetWithLineAndTagsResp.

        健康检查ID。

        :param health_check_id: The health_check_id of this QueryRecordSetWithLineAndTagsResp.
        :type: str
        """
        self._health_check_id = health_check_id

    @property
    def alias_target(self):
        """Gets the alias_target of this QueryRecordSetWithLineAndTagsResp.


        :return: The alias_target of this QueryRecordSetWithLineAndTagsResp.
        :rtype: AliasTarget
        """
        return self._alias_target

    @alias_target.setter
    def alias_target(self, alias_target):
        """Sets the alias_target of this QueryRecordSetWithLineAndTagsResp.


        :param alias_target: The alias_target of this QueryRecordSetWithLineAndTagsResp.
        :type: AliasTarget
        """
        self._alias_target = alias_target

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
        if not isinstance(other, QueryRecordSetWithLineAndTagsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
