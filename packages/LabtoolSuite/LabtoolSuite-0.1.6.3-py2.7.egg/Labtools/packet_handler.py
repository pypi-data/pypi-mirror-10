from commands_proto import *
import serial

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Handler(object):
	__metaclass__ = Singleton
	def __init__(self,timeout=1.0,**kwargs):
		self.burstBuffer=''
		self.loadBurst=False
		self.inputQueueSize=0
		portname = kwargs.get('port','/dev/TestBench')
		try:
			self.fd = serial.Serial(portname, 9600, stopbits=1, timeout = 0.1)
			self.fd.close()
			time.sleep(0.2)
			self.fd = serial.Serial(portname, 1000000, stopbits=1, timeout = timeout)
			print 'connected TestBench'
		except serial.SerialException as ex:
			print "failed to connect. Check device connections ,Or\nls /dev/TestBench\nOr, check if symlink has been created in /etc/udev/rules.d/proto.rules for the relevant Vid,Pid"
			sys.exit(1)
			
		if(self.fd.inWaiting()):
			self.fd.read(1000)
			self.fd.flush()
		

	def __del__(self):
		print 'closing port'
		try:self.fd.close()
		except: pass

	def __get_ack__(self):
		"""
		fetches the response byte
		 1 SUCCESS
		 2 ARGUMENT_ERROR
		 3 FAILED
		used as a handshake
		"""
		if not self.loadBurst:x=self.fd.read(1)
		else:
			self.inputQueueSize+=1
			x=1
		#print x
		return x

	def __sendInt__(self,val):
		"""
		transmits an integer packaged as two characters
		:params int val: int to send
		"""
		if not self.loadBurst:self.fd.write(InttoString(val))
		else: self.burstBuffer+=InttoString(val)

	def __sendByte__(self,val):
		"""
		transmits a BYTE
		val - byte to send
		"""
		if(type(val)==int):
			if not self.loadBurst:self.fd.write(chr(val))
			else:self.burstBuffer+=chr(val)
		else:
			if not self.loadBurst:self.fd.write(val)
			else:self.burstBuffer+=val
			
	def __getByte__(self):
		"""
		reads a byte from the serial port and returns it
		"""
		ss=self.fd.read(1)
		if len(ss): return ord(ss)
		else:
			print 'comm error.  lower the BAUD maybe'
			sys.exit(1)
	
	def __getInt__(self):
		"""
		reads two bytes from the serial port and
		returns an integer after combining them
		"""
		ss = self.fd.read(2)
		if len(ss)==2: return ord(ss[0])|(ord(ss[1])<<8)
		else:
			print 'comm error.  lower the BAUD maybe'
			sys.exit(1)

	def __getLong__(self):
		"""
		reads four bytes.
		returns long
		"""
		ss = self.fd.read(4)
		if len(ss)==4: return ord(ss[0])|(ord(ss[1])<<8)|(ord(ss[2])<<16)|(ord(ss[3])<<24)
		else:
			print '.'
			return -1
	

	def sendBurst(self):
		"""
		Transmits the commands stored in the burstBuffer.
		empties input buffer
		empties the burstBuffer.
		
		The following example initiates the capture routine and sets OD1 HIGH immediately.
		
		It is used by the Transient response experiment where the input needs to be toggled soon
		after the oscilloscope has been started.
		
		>>> I.loadBurst=True
		>>> I.capture_traces(4,800,2)
		>>> I.set_state(I.OD1,I.HIGH)
		>>> I.sendBurst()
		

		"""
		self.fd.write(self.burstBuffer)
		self.burstBuffer=''
		self.loadBurst=False
		acks=self.fd.read(self.inputQueueSize)
		self.inputQueueSize=0
		return [ord(a) for a in acks]

	def send_char(self,c):
		"""
		Relays a character through the second UART(9-bit mode)

		==============	============================================================================================
		**Arguments** 
		==============	============================================================================================
		c				value to transmit
		==============	============================================================================================

		:return: nothing
		"""
		self.__sendByte__(UART_2)
		self.__sendByte__(SEND_CHAR)
		self.__sendByte__(c)
		self.__get_ack__()

		
