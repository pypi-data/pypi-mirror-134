# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeApplicationVersionResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'name': 'str',
        'deploy_type': 'str',
        'version': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'state': 'str',
        'liveness_probe': 'ProbeDTO',
        'readiness_probe': 'ProbeDTO',
        'arch': 'list[str]',
        'command': 'list[str]',
        'args': 'list[str]',
        'container_settings': 'ContainerSettingsDTO',
        'outputs': 'list[str]',
        'inputs': 'list[str]',
        'services': 'list[str]',
        'publish_time': 'str',
        'off_shelf_time': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'name': 'name',
        'deploy_type': 'deploy_type',
        'version': 'version',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'state': 'state',
        'liveness_probe': 'liveness_probe',
        'readiness_probe': 'readiness_probe',
        'arch': 'arch',
        'command': 'command',
        'args': 'args',
        'container_settings': 'container_settings',
        'outputs': 'outputs',
        'inputs': 'inputs',
        'services': 'services',
        'publish_time': 'publish_time',
        'off_shelf_time': 'off_shelf_time'
    }

    def __init__(self, edge_app_id=None, name=None, deploy_type=None, version=None, description=None, create_time=None, update_time=None, state=None, liveness_probe=None, readiness_probe=None, arch=None, command=None, args=None, container_settings=None, outputs=None, inputs=None, services=None, publish_time=None, off_shelf_time=None):
        """CreateEdgeApplicationVersionResponse - a model defined in huaweicloud sdk"""
        
        super(CreateEdgeApplicationVersionResponse, self).__init__()

        self._edge_app_id = None
        self._name = None
        self._deploy_type = None
        self._version = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._state = None
        self._liveness_probe = None
        self._readiness_probe = None
        self._arch = None
        self._command = None
        self._args = None
        self._container_settings = None
        self._outputs = None
        self._inputs = None
        self._services = None
        self._publish_time = None
        self._off_shelf_time = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if name is not None:
            self.name = name
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if state is not None:
            self.state = state
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if arch is not None:
            self.arch = arch
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if container_settings is not None:
            self.container_settings = container_settings
        if outputs is not None:
            self.outputs = outputs
        if inputs is not None:
            self.inputs = inputs
        if services is not None:
            self.services = services
        if publish_time is not None:
            self.publish_time = publish_time
        if off_shelf_time is not None:
            self.off_shelf_time = off_shelf_time

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this CreateEdgeApplicationVersionResponse.

        应用ID

        :return: The edge_app_id of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this CreateEdgeApplicationVersionResponse.

        应用ID

        :param edge_app_id: The edge_app_id of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._edge_app_id = edge_app_id

    @property
    def name(self):
        """Gets the name of this CreateEdgeApplicationVersionResponse.

        应用名称

        :return: The name of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEdgeApplicationVersionResponse.

        应用名称

        :param name: The name of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._name = name

    @property
    def deploy_type(self):
        """Gets the deploy_type of this CreateEdgeApplicationVersionResponse.

        部署类型docker|process

        :return: The deploy_type of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this CreateEdgeApplicationVersionResponse.

        部署类型docker|process

        :param deploy_type: The deploy_type of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._deploy_type = deploy_type

    @property
    def version(self):
        """Gets the version of this CreateEdgeApplicationVersionResponse.

        应用版本

        :return: The version of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateEdgeApplicationVersionResponse.

        应用版本

        :param version: The version of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this CreateEdgeApplicationVersionResponse.

        应用描述

        :return: The description of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeApplicationVersionResponse.

        应用描述

        :param description: The description of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this CreateEdgeApplicationVersionResponse.

        创建时间

        :return: The create_time of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateEdgeApplicationVersionResponse.

        创建时间

        :param create_time: The create_time of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateEdgeApplicationVersionResponse.

        最后一次修改时间

        :return: The update_time of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateEdgeApplicationVersionResponse.

        最后一次修改时间

        :param update_time: The update_time of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._update_time = update_time

    @property
    def state(self):
        """Gets the state of this CreateEdgeApplicationVersionResponse.

        应用版本状态

        :return: The state of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateEdgeApplicationVersionResponse.

        应用版本状态

        :param state: The state of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._state = state

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this CreateEdgeApplicationVersionResponse.


        :return: The liveness_probe of this CreateEdgeApplicationVersionResponse.
        :rtype: ProbeDTO
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this CreateEdgeApplicationVersionResponse.


        :param liveness_probe: The liveness_probe of this CreateEdgeApplicationVersionResponse.
        :type: ProbeDTO
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this CreateEdgeApplicationVersionResponse.


        :return: The readiness_probe of this CreateEdgeApplicationVersionResponse.
        :rtype: ProbeDTO
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this CreateEdgeApplicationVersionResponse.


        :param readiness_probe: The readiness_probe of this CreateEdgeApplicationVersionResponse.
        :type: ProbeDTO
        """
        self._readiness_probe = readiness_probe

    @property
    def arch(self):
        """Gets the arch of this CreateEdgeApplicationVersionResponse.

        架构

        :return: The arch of this CreateEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this CreateEdgeApplicationVersionResponse.

        架构

        :param arch: The arch of this CreateEdgeApplicationVersionResponse.
        :type: list[str]
        """
        self._arch = arch

    @property
    def command(self):
        """Gets the command of this CreateEdgeApplicationVersionResponse.

        启动命令

        :return: The command of this CreateEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this CreateEdgeApplicationVersionResponse.

        启动命令

        :param command: The command of this CreateEdgeApplicationVersionResponse.
        :type: list[str]
        """
        self._command = command

    @property
    def args(self):
        """Gets the args of this CreateEdgeApplicationVersionResponse.

        启动参数

        :return: The args of this CreateEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this CreateEdgeApplicationVersionResponse.

        启动参数

        :param args: The args of this CreateEdgeApplicationVersionResponse.
        :type: list[str]
        """
        self._args = args

    @property
    def container_settings(self):
        """Gets the container_settings of this CreateEdgeApplicationVersionResponse.


        :return: The container_settings of this CreateEdgeApplicationVersionResponse.
        :rtype: ContainerSettingsDTO
        """
        return self._container_settings

    @container_settings.setter
    def container_settings(self, container_settings):
        """Sets the container_settings of this CreateEdgeApplicationVersionResponse.


        :param container_settings: The container_settings of this CreateEdgeApplicationVersionResponse.
        :type: ContainerSettingsDTO
        """
        self._container_settings = container_settings

    @property
    def outputs(self):
        """Gets the outputs of this CreateEdgeApplicationVersionResponse.

        应用输出路由端点

        :return: The outputs of this CreateEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this CreateEdgeApplicationVersionResponse.

        应用输出路由端点

        :param outputs: The outputs of this CreateEdgeApplicationVersionResponse.
        :type: list[str]
        """
        self._outputs = outputs

    @property
    def inputs(self):
        """Gets the inputs of this CreateEdgeApplicationVersionResponse.

        应用输入路由

        :return: The inputs of this CreateEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this CreateEdgeApplicationVersionResponse.

        应用输入路由

        :param inputs: The inputs of this CreateEdgeApplicationVersionResponse.
        :type: list[str]
        """
        self._inputs = inputs

    @property
    def services(self):
        """Gets the services of this CreateEdgeApplicationVersionResponse.

        应用实现的服务列表

        :return: The services of this CreateEdgeApplicationVersionResponse.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this CreateEdgeApplicationVersionResponse.

        应用实现的服务列表

        :param services: The services of this CreateEdgeApplicationVersionResponse.
        :type: list[str]
        """
        self._services = services

    @property
    def publish_time(self):
        """Gets the publish_time of this CreateEdgeApplicationVersionResponse.

        发布时间

        :return: The publish_time of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this CreateEdgeApplicationVersionResponse.

        发布时间

        :param publish_time: The publish_time of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._publish_time = publish_time

    @property
    def off_shelf_time(self):
        """Gets the off_shelf_time of this CreateEdgeApplicationVersionResponse.

        下线时间

        :return: The off_shelf_time of this CreateEdgeApplicationVersionResponse.
        :rtype: str
        """
        return self._off_shelf_time

    @off_shelf_time.setter
    def off_shelf_time(self, off_shelf_time):
        """Sets the off_shelf_time of this CreateEdgeApplicationVersionResponse.

        下线时间

        :param off_shelf_time: The off_shelf_time of this CreateEdgeApplicationVersionResponse.
        :type: str
        """
        self._off_shelf_time = off_shelf_time

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
        if not isinstance(other, CreateEdgeApplicationVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
