import traceback
from collections import namedtuple

TraceNode = namedtuple('TraceNode', 'file_name, code_line, func_name, text')

class ExceptionBus(Exception):
  def __init__(self, msg, trace = []):
    self.what = msg
    self.traceback = trace
    if 0 == len(self.traceback):
      stack = traceback.extract_stack()
      for i in range(len(stack) - 1):
        (file_name, code_line, func_name, text) = stack[i]
        self.traceback.append(TraceNode(file_name, code_line, func_name, text))

  def printError(self, trace = True):
    print('Error: {0}'.format(self.what))
    if trace:
      print('Trace:')
      i = 1
      for tr in self.traceback:
        print('{0}. {1} -> {2} -> {3}'.format(i, tr.file_name, tr.code_line, tr.func_name))
        i += 1
