txsh is a dynamic wrapper around Twisted ProcessProtocol and
spawnProcess that allows you to call any program as if it were
a function and return a deferred with its exit code and output.

from twisted.internet import reactor
from txsh import ls

def my_callback(exc_info):
    print 'Exit Code:', exc_info.status
    print 'Output:', exc_info.stdout
    print 'Errors:', exc_info.stderr
    reactor.stop()

d = ls()
d.addCallback(my_callback)

reactor.run()


