"""Agent and Agent group definitions and settings dataclasses."""
import dataclasses
import io
from typing import List, Optional

from ostorlab.agent.schema import loader
from ostorlab.runtimes.proto import agent_instance_settings_pb2
from ostorlab.utils import defintions


@dataclasses.dataclass
class AgentSettings:
    """Agent instance lists the settings of running instance of an agent."""
    key: str
    bus_url: Optional[str] = None
    bus_exchange_topic: Optional[str] = None
    bus_managment_url: Optional[str] = None
    bus_vhost: Optional[str] = None
    args: List[defintions.Arg] = dataclasses.field(default_factory=list)
    constraints: List[str] = dataclasses.field(default_factory=list)
    mounts: Optional[List[str]] = dataclasses.field(default_factory=list)
    restart_policy: str = 'any'
    mem_limit: Optional[int] = None
    open_ports: List[defintions.PortMapping] = dataclasses.field(default_factory=list)
    replicas: int = 1
    healthcheck_host: str = '0.0.0.0'
    healthcheck_port: int = 5000

    @property
    def container_image(self):
        """Agent image name."""
        image = self.key.replace('/', '_')
        # TODO (alaeddine): add container tag resolution.
        return image

    @classmethod
    def from_proto(cls, proto: bytes) -> 'AgentSettings':
        """Constructs an agent definition from a binary proto settings.

        Args:
            proto: binary proto settings file.

        Returns:
            AgentInstanceSettings object.
        """
        instance = agent_instance_settings_pb2.AgentInstanceSettings()
        instance.ParseFromString(proto)
        return cls(
            key=instance.key,
            bus_url=instance.bus_url,
            bus_exchange_topic=instance.bus_exchange_topic,
            bus_managment_url=instance.bus_managment_url,
            bus_vhost=instance.bus_vhost,
            args=[defintions.Arg(
                name=a.name,
                type=a.type,
                value=a.value
            ) for a in instance.args],
            constraints=instance.constraints,
            mounts=instance.mounts,
            restart_policy=instance.restart_policy,
            mem_limit=instance.mem_limit,
            open_ports=[defintions.PortMapping(
                source_port=p.source_port,
                destination_port=p.destination_port
            ) for p in instance.open_ports],
            replicas=instance.replicas,
            healthcheck_host=instance.healthcheck_host,
            healthcheck_port=instance.healthcheck_port,
        )

    def to_raw_proto(self) -> bytes:
        """Transforms agent instance settings into a raw proto bytes.

        Returns:
            Bytes as a serialized proto.
        """
        instance = agent_instance_settings_pb2.AgentInstanceSettings()
        instance.key = self.key
        instance.bus_url = self.bus_url
        instance.bus_exchange_topic = self.bus_exchange_topic
        instance.bus_managment_url = self.bus_managment_url
        instance.bus_vhost = self.bus_vhost

        for arg in self.args:
            arg_instance = instance.args.add()
            arg_instance.name = arg.name
            arg_instance.type = arg.type
            arg_instance.value = arg.value

        instance.constraints.extend(self.constraints)
        instance.mounts.extend(self.mounts)
        instance.restart_policy = self.restart_policy
        if self.mem_limit is not None:
            instance.mem_limit = self.mem_limit

        for open_port in self.open_ports:
            open_port_instance = instance.open_ports.add()
            open_port_instance.source_port = open_port.source_port
            open_port_instance.destination_port = open_port.destination_port

        instance.replicas = self.replicas
        instance.healthcheck_host = self.healthcheck_host
        instance.healthcheck_port = self.healthcheck_port

        return instance.SerializeToString()


@dataclasses.dataclass
class AgentGroupDefinition:
    """Data class holding the attributes of an agent."""
    agents: List[AgentSettings]

    @classmethod
    def from_yaml(cls, group: io.FileIO):
        """Construct AgentGroupDefinition from yaml file.

        Args:
            group : agent group .yaml file.
        """
        agent_group_def = loader.load_agent_group_yaml(group)
        agent_settings = []
        for agent in agent_group_def['agents']:
            agent_def = AgentSettings(
                key=agent.get('key'),
                args=[defintions.Arg(name=a.get('name'), description=a.get('description'), type=a.get('type'),
                                     value=a.get('value')) for a in
                      agent.get('args', [])],
                constraints=agent.get('constraints'),
                mounts=agent.get('mounts'),
                restart_policy=agent.get('restart_policy'),
                mem_limit=agent.get('mem_limit'),
                open_ports=[defintions.PortMapping(source_port=p.get('src_port'), destination_port=p.get('dest_port'))
                            for p
                            in agent.get('open_ports', [])]
            )

            agent_settings.append(agent_def)

        return cls(agent_settings)
