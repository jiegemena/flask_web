
class ILogTools:
    def __init__(self, log):
        self.log = log

    def info(self,str):
        self.log.info(str)

    def error(self,str):
        self.log.error(str)

    def fatal(self,str):
        self.log.exception(str)

    def debug(self,str):
        self.log.debug(str)