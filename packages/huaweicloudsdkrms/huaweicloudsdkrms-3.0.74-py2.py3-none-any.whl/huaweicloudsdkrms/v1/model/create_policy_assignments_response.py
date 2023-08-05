# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyAssignmentsResponse(SdkResponse):


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
        'policy_filter': 'PolicyFilterDefinition',
        'state': 'str',
        'created': 'str',
        'updated': 'str',
        'policy_definition_id': 'str',
        'parameters': 'dict(str, PolicyParameterValue)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'policy_filter': 'policy_filter',
        'state': 'state',
        'created': 'created',
        'updated': 'updated',
        'policy_definition_id': 'policy_definition_id',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, name=None, description=None, policy_filter=None, state=None, created=None, updated=None, policy_definition_id=None, parameters=None):
        """CreatePolicyAssignmentsResponse - a model defined in huaweicloud sdk"""
        
        super(CreatePolicyAssignmentsResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._policy_filter = None
        self._state = None
        self._created = None
        self._updated = None
        self._policy_definition_id = None
        self._parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if policy_filter is not None:
            self.policy_filter = policy_filter
        if state is not None:
            self.state = state
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if policy_definition_id is not None:
            self.policy_definition_id = policy_definition_id
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        """Gets the id of this CreatePolicyAssignmentsResponse.

        规则ID

        :return: The id of this CreatePolicyAssignmentsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatePolicyAssignmentsResponse.

        规则ID

        :param id: The id of this CreatePolicyAssignmentsResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreatePolicyAssignmentsResponse.

        规则名字

        :return: The name of this CreatePolicyAssignmentsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePolicyAssignmentsResponse.

        规则名字

        :param name: The name of this CreatePolicyAssignmentsResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreatePolicyAssignmentsResponse.

        规则描述

        :return: The description of this CreatePolicyAssignmentsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePolicyAssignmentsResponse.

        规则描述

        :param description: The description of this CreatePolicyAssignmentsResponse.
        :type: str
        """
        self._description = description

    @property
    def policy_filter(self):
        """Gets the policy_filter of this CreatePolicyAssignmentsResponse.


        :return: The policy_filter of this CreatePolicyAssignmentsResponse.
        :rtype: PolicyFilterDefinition
        """
        return self._policy_filter

    @policy_filter.setter
    def policy_filter(self, policy_filter):
        """Sets the policy_filter of this CreatePolicyAssignmentsResponse.


        :param policy_filter: The policy_filter of this CreatePolicyAssignmentsResponse.
        :type: PolicyFilterDefinition
        """
        self._policy_filter = policy_filter

    @property
    def state(self):
        """Gets the state of this CreatePolicyAssignmentsResponse.

        规则状态

        :return: The state of this CreatePolicyAssignmentsResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreatePolicyAssignmentsResponse.

        规则状态

        :param state: The state of this CreatePolicyAssignmentsResponse.
        :type: str
        """
        self._state = state

    @property
    def created(self):
        """Gets the created of this CreatePolicyAssignmentsResponse.

        规则创建时间

        :return: The created of this CreatePolicyAssignmentsResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreatePolicyAssignmentsResponse.

        规则创建时间

        :param created: The created of this CreatePolicyAssignmentsResponse.
        :type: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this CreatePolicyAssignmentsResponse.

        规则更新时间

        :return: The updated of this CreatePolicyAssignmentsResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CreatePolicyAssignmentsResponse.

        规则更新时间

        :param updated: The updated of this CreatePolicyAssignmentsResponse.
        :type: str
        """
        self._updated = updated

    @property
    def policy_definition_id(self):
        """Gets the policy_definition_id of this CreatePolicyAssignmentsResponse.

        规则的策略ID

        :return: The policy_definition_id of this CreatePolicyAssignmentsResponse.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        """Sets the policy_definition_id of this CreatePolicyAssignmentsResponse.

        规则的策略ID

        :param policy_definition_id: The policy_definition_id of this CreatePolicyAssignmentsResponse.
        :type: str
        """
        self._policy_definition_id = policy_definition_id

    @property
    def parameters(self):
        """Gets the parameters of this CreatePolicyAssignmentsResponse.

        规则参数

        :return: The parameters of this CreatePolicyAssignmentsResponse.
        :rtype: dict(str, PolicyParameterValue)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CreatePolicyAssignmentsResponse.

        规则参数

        :param parameters: The parameters of this CreatePolicyAssignmentsResponse.
        :type: dict(str, PolicyParameterValue)
        """
        self._parameters = parameters

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
        if not isinstance(other, CreatePolicyAssignmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
