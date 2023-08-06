import os
import multiprocessing
from zope.interface import implementer

from ..imported.twisted.internet_interfaces import ITransport, IReadWriteDescriptor


class ChildPipe:
	'a read or a write pipe from a PipeConnection'
	def __init__(self, pipe, connection):
		self.pipe = pipe
		self.connection = connection


	def fileno(self):
		return self.pipe.fileno()


	def doRead(self):
		self.connection.doRead()


@implementer(ITransport, IReadWriteDescriptor)
class PipeConnection:

	def __init__(self, protocol, reactor=None):
		self.rpipe, self.wpipe = multiprocessing.Pipe()
		self.protocol = protocol

		self._tempDataBuffer = []


	def doRead(self):
		data = self.rpipe.recv()
		self.protocol.dataReceived(data)	#handle multiple messages


	def doWrite(self):
		for data in self._tempDataBuffer:
			self.wpipe.send(data)
			self._tempDataBuffer.remove(data)


	def write(self, data):
		self._tempDataBuffer.append(data)

	
	def write_blocking(self, data):
		self.wpipe.send(data)


	def writeSequence(self, data):
		raise NotImplemented('method not implemented')


	def loseConnection(self):
		pass


	def getHost(self):
		pass


	def getPeer(self):
		pass


	def getReadPipe(self):
		return ChildPipe(self.rpipe, self)


	def getWritePipe(self):
		return ChildPipe(self.wpipe, self)

