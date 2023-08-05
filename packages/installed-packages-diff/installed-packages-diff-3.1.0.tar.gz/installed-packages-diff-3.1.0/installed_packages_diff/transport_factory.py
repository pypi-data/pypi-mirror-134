from installed_packages_diff.local_transport import LocalTransport
from installed_packages_diff.ssh_transport import SshTransport


class TransportFactory(object):
  def connect(self, server):
    if server.url.scheme == "ssh":
      return SshTransport(server)
    else:
      return LocalTransport()
