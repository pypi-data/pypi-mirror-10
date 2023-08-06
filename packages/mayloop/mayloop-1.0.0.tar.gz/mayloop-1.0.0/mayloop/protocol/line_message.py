import os

from .message import Message
from ..limits import get_limits


#receives simple newline terminated message
class LineMessage(Message):
	def __init__(self):
		Message.__init__(self)


	def dataReceived(self, data):
		self._buffer += data
		if len(self._buffer) > get_limits().max_line_message_length:
			self.messageError(self._buffer)
			self._buffer = b''

		if self._buffer.endswith(str.encode(os.linesep)):
			self.messageReceived(self._buffer.rstrip())
			self._buffer = b''


	def connectionLost(self, reason=None):
		self._buffer = b''

