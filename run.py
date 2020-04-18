import os

from twisted.internet import reactor
from twisted.internet.serialport import SerialPort
from service.protocol import SerialProtocol

base_dir = os.getcwd()

# def log_init(server):
#     '''
#
#     :return:
#     '''
#     # 初始化日志
#     logPath  = base_dir + os.sep + "logs"
#     Log.msg("初始化日志路径为：{}".format(GlobalObject().config["LOG_PATH"]))
#
#     if os.path.isdir(GlobalObject().config.get("LOG_PATH")) == False:  # 设置生产日志路径
#         os.mkdir(GlobalObject().config.get("LOG_PATH"))
#     log.FileLogObserver.timeFormat = '%Y-%m-%d %H:%M:%S'
#
#     if GlobalObject().config.get("DEBUG", False):  # 若是debug模式
#         # f = sys.stdout
#         f = DailyLogFile(server.lower() + ".log", GlobalObject().config.get("LOG_PATH"))
#         Log.msg("当前为DEBUG模式，设置日志为屏幕输出")
#     else:
#         f = DailyLogFile(server.lower() + ".log", GlobalObject().config.get("LOG_PATH"))
#         Log.msg("当前为常规模式，设置日志路径，且将日志运行于每日分割模式")
#
#     log_level = GlobalObject().config.get("LOG_LEVEL", "DEBUG")
#
#     if log_level.upper() == "DEBUG":
#         logger = LevelFileLogObserver(f, logging.DEBUG)
#     else:
#         logger = LevelFileLogObserver(f, logging.INFO)
#
#     log.startLoggingWithObserver(logger.emit, setStdout=False)

if __name__ == '__main__':
    port = SerialPort(SerialProtocol(None), 'COM5', reactor, baudrate=115200)
    
    # reactor.callLater(10, reactor.stop)
    reactor.run()