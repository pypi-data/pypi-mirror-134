"""
Base class and helper methods for the Service wrappers
"""
import types
from abc import ABC
from typing import Optional, Type, T

from betterproto import Message, ServiceStub
from grpclib.client import Channel

from trinsic.proto.services.account.v1 import AccountProfile
from trinsic.proto.services.common.v1 import ServerConfig
from trinsic.security_providers import OberonSecurityProvider, SecurityProvider
from trinsic.trinsic_util import create_channel

_skip_routes = ["/services.account.v1.Account/SignIn"]


def _update_metadata(route: str, service: "ServiceBase", metadata: "_MetadataLike",
                     request: "_MessageLike") -> "_MetadataLike":
    if route in _skip_routes:
        return metadata
    metadata = metadata or {}
    new_metadata = service.build_metadata(request)
    metadata.update(new_metadata)
    return metadata


class ServiceBase(ABC):
    """
    Base class for service wrapper classes, provides the metadata functionality in a consistent manner.
    """

    def __init__(self, profile: AccountProfile,
                 server_config: ServerConfig,
                 channel: Channel):
        self.profile: AccountProfile = profile
        self._server_config: ServerConfig = server_config
        self._channel: Channel = channel or create_channel(server_config)
        self._security_provider: SecurityProvider = OberonSecurityProvider()

    def close(self):
        """Close the underlying channel"""
        self._channel.close()
        del self._channel

    def build_metadata(self, request: Message):
        """
        Create call metadata by setting required authentication headers via `AccountProfile`
        :return: authentication headers with base-64 encoded Oberon
        """
        if not self.profile:
            raise ValueError("Cannot call authenticated endpoint: profile must be set")

        return {"authorization": self._security_provider.get_auth_header(self.profile, request)}

    def stub_with_metadata(self, stub_type: Type[T]) -> T:
        return self.with_call_metadata(stub_type(self.channel))

    def with_call_metadata(self, stub: ServiceStub) -> ServiceStub:
        # Find the _unary_unary() method
        _cls_unary_unary = getattr(stub, '_unary_unary')

        # Wrap it
        async def wrapped_unary(this,
                                route: str,
                                request: "_MessageLike",
                                response_type: Type[T],
                                *,
                                timeout: Optional[float] = None,
                                deadline: Optional["Deadline"] = None,
                                metadata: Optional["_MetadataLike"] = None) -> Type[T]:
            metadata = _update_metadata(route, self, metadata, request)
            return await this._unary_unary_1(route, request, response_type, timeout=timeout, deadline=deadline,
                                             metadata=metadata)

        stub._unary_unary = types.MethodType(wrapped_unary, stub)
        stub._unary_unary_1 = _cls_unary_unary
        return stub

    @property
    def channel(self):
        """Underlying channel"""
        return self._channel
