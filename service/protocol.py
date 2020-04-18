import datetime
import time

from twisted.protocols.basic import LineOnlyReceiver
from twisted.internet import reactor

class SerialProtocol(LineOnlyReceiver):
    
    
    def __init__(self,tcpFactory = None):
        self.tcpFactory = tcpFactory
        self.factory = SerialFactory()
    
    def connectionMade(self):
        '''
        
        :return:
        '''
        # print('connection made')
        self.factory.doConnectionMade()              #
        
    def connectionLost(self, reason):
        '''
        
        :param reason:
        :return:
        '''
        self.factory.doConnectionLost()
    
    def dataReceived(self, data):
        # print("当前时间;{time} 收到数据:{data}".format(time = datetime.datetime.now(),data = [hex(item) for item in data]))
        # print("当前时间;{time} 收到数据:{data}".format(time = datetime.datetime.now(),data = data.decode()))
        self._buffer += data
        for i in range(len(self._buffer)):
            if self._buffer[i:i+1] == b"\n":
                data_ = self._buffer[0:i+1]
                self._buffer = self._buffer[i+1:]
                print("当前时间;{time} :{data}".format(time = datetime.datetime.now(),data = data_))
        # self.transport.write()
        
    
    def dataHandleCoroutine(self):
        """
        """
        while True:
            data = yield
            self._recv_buffer += data
            if len(self._recv_buffer) >= 4:
                pass
                # length, = unpack("<I", self._recv_buffer[0:4])  # 按小字节序转int
                # if len(self._recv_buffer) >= length + 4:
                #     unpackdata = self.factory.dataprotocl.unpack(self._recv_buffer[4:4 + length])
                #     if not unpackdata.get('result'):
                #         Log.err(
                #             "客户端:{} {} 指令发送错误,错误指令为{}..."
                #                 .format(self.transport.client[0], self.transport.client[1], [hex(item) for item in
                #                 data]))
                #         self.transport.loseConnection()
                #         break
                #     else:
                #         commandID = unpackdata.get('command')  # 指令ID 在这里必然是 “forwarding” 因为需要发送给gateway来分发
                #         request = unpackdata.get('request')  # 请求内容 真正的 协议内容在这里
                #
                #         self._recv_buffer = self._recv_buffer[4 + length:]
                #
                #         d = self.factory.doDataReceived(self, commandID, request)
                #         if not d:
                #             continue
                #
                #         d.addCallback(self.processCommand).addErrback(DefferedErrorHandle)
                #         d.addCallback(self.safeToWriteData).addErrback(DefferedErrorHandle)
    
    def safeToWriteData(self,command):
        '''
        线程安全的向客户端发送数据
        @param data: str 要向客户端写的数据
        '''
        if not self.transport.connected or not command:
            return
        messages = self.factory.produceResult(command)
        for message in messages:
            reactor.callFromThread(self._send_message, message)
        
    def _send_message(self, data):  # 将数据构造好并发送
        '''
        发送函数的封装
        :param data:
        :return:
        '''
        # self.transport.write(pack(Len_Encode, len(data) + 3))  # 构造帧头
        # self.transport.write(pack(Header_Encode, HeaderData))  # 构造标识符
        # self.transport.write(data)  # 文件body
        # self.transport.write(pack(End_Encode, EndData))  # 构造尾
    
class SerialFactory():
    
    protocol = SerialProtocol

    def __init__(self, dataprotocl = None):
        '''
        初始化
        '''
        self.service = None
        self.dataprotocl = dataprotocl  # 协议类
    
    def setDataProtocl(self, dataprotocl):
        '''
        '''
        self.dataprotocl = dataprotocl          # 设置协议类
    
    def doConnectionMade(self):
        """
        
        :return:
        """

    def doConnectionLost(self, conn):
        '''
        连接断开时的处理
        '''
        
    def doDataReceived(self, conn, commandID, data):
        '''
        数据到达时的处理
            在这个系统内，这里的数据全部都通过 forwarding 发送给gateway
            通过gateway分发
        '''
    
    def produceResult(self, command):
        '''
        产生客户端需要的最终结果
        @param response: str 分布式客户端获取的结果
        '''
        # return command.get("message",[])
    
    def loseConnection(self, connID):
        """
        主动端口与客户端的连接
        """
        
    
    # def onDataR