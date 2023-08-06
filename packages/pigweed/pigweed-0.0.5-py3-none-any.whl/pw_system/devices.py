"""Device classes to interact with targets via RPC."""

import logging
from typing import Any

from pw_hdlc.decode import Frame
from pw_log.proto import log_pb2
from pw_protobuf_compiler import python_protos
from pw_rpc import callback_client, Channel, Client, console_tools
from pw_status import Status

from p29.network import ChannelId, Chip, HdlcAddress
from p29.transport import Transport
from p29 import protos

# Internal log for troubleshooting this tool (the console).
_LOG = logging.getLogger('p29_tools')
DEFAULT_DEVICE_LOGGER = logging.getLogger('p29_device')


class Device:
    """Represents an RPC Client for a device running a Pigweed target.

    The target must have and RPC support, RPC logging.
    Note: use this class as a base for specialized device representations.
    """
    def __init__(self,
                 chip: Chip,
                 channel_id: ChannelId,
                 proto_library: python_protos.Library,
                 transport: Transport,
                 rpc_timeout_s=5):
        self.chip = chip
        self.channel_id = channel_id
        self.protos = proto_library
        self.transport = transport

        hdlc_address = HdlcAddress(self.chip, Chip.HOST)
        self.transport.set_handler(self.chip.value, self._handle_rpc_frame)

        self.logger = DEFAULT_DEVICE_LOGGER
        self.logger.setLevel(logging.DEBUG)  # Allow all device logs through.
        self.rpc_timeout_s = rpc_timeout_s

        def channel_output(data):
            return self.transport.write(hdlc_address.address, data)

        self.client = Client.from_modules(
            callback_client.Impl(
                default_unary_timeout_s=self.rpc_timeout_s,
                default_stream_timeout_s=self.rpc_timeout_s,
            ),
            [Channel(self.channel_id.value, channel_output)],
            self.protos.modules(),
        )

        # Start listening to logs as soon as possible.
        self.listen_to_log_stream()

    def info(self) -> console_tools.ClientInfo:
        return console_tools.ClientInfo(self.name.lower(), self, self.client)

    @property
    def name(self):
        return self.chip.chip_name()

    @property
    def rpcs(self) -> Any:
        """Returns an object for accessing services on the specified channel."""
        return next(iter(self.client.channels())).rpcs

    def __repr__(self) -> str:
        return f'<{self.name}: {self.rpcs}>'

    def _handle_rpc_frame(self, frame: Frame) -> None:
        address = HdlcAddress.parse(frame.address)
        # Addressing is done from the perspective of the server: the source is
        # this device representation an the destination is the host console.
        _LOG.debug('HDLC frame from %s to %s', address.source,
                   address.destination)
        if address.source != self.chip:
            return

        self.client.process_packet(frame.data)

    def listen_to_log_stream(self):
        """Opens a log RPC for the device's unrequested log stream.

        The RPCs remain open until the server cancels or closes them, either
        with a response or error packet.
        """
        self.rpcs.pw.log.Logs.Listen.open(
            on_next=lambda _, log_entries_proto: self.
            _log_entries_proto_parser(log_entries_proto),
            on_completed=lambda _, status: _LOG.info(
                'Log stream completed for source: %s, status: %s', self.name,
                status),
            on_error=lambda _, error: self._handle_log_stream_error(error))

    def _handle_log_stream_error(self, error: Status):
        """Resets the log stream RPC on error to avoid losing logs."""
        _LOG.error('Log stream error for source: %s, error: %s', self.name,
                   error)
        self.listen_to_log_stream()

    def _log_entries_proto_parser(self, log_entries_proto: log_pb2.LogEntries):
        for log_entry_proto in log_entries_proto.entries:
            decoded_message = str(log_entry_proto.message.decode("utf-8"))
            # TODO(cachinchilla): remove this level hack once the tokenized log
            # backend is used.
            level = logging.NOTSET
            if 'DBG' in decoded_message:
                level = logging.DEBUG
            elif 'INF' in decoded_message:
                level = logging.INFO
            elif 'WRN' in decoded_message:
                level = logging.WARNING
            elif 'ERR' in decoded_message:
                level = logging.ERROR
            elif 'FTL' in decoded_message:
                level = logging.CRITICAL
            message = decoded_message
            if level != logging.NOTSET:
                message = str(
                    log_entry_proto.message.split(b'\033[0m  ')[-1].decode(
                        "utf-8"))
            fields = dict()
            fields['source_name'] = self.chip.log_name
            fields['timestamp'] = '%16.3f' % log_entry_proto.timestamp
            fields['msg'] = message
            self.logger.log(level,
                            '[%s] %16.3f %s',
                            self.chip.log_name,
                            log_entry_proto.timestamp,
                            decoded_message,
                            extra=dict(extra_metadata_fields=fields))


class LpA32(Device):
    """Represents the LPA32."""
    def __init__(self, transport: Transport, rpc_timeout_s=5):
        super().__init__(Chip.LPA32, ChannelId.HOST_LPA32, protos.all_protos(),
                         transport, rpc_timeout_s)


class AoM33(Device):
    """Represents the AOM33."""
    def __init__(self, transport: Transport, rpc_timeout_s=5):
        super().__init__(Chip.AOM33, ChannelId.HOST_AOM33, protos.all_protos(),
                         transport, rpc_timeout_s)


class AoM0(Device):
    """Represents the AOM0."""
    def __init__(self, transport: Transport, rpc_timeout_s=5):
        super().__init__(Chip.AOM0, ChannelId.HOST_AOM0, protos.all_protos(),
                         transport, rpc_timeout_s)
