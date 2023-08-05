import logging

from .package import Package
from .transport_factory import TransportFactory


class PackageFetcher(object):
  LIST_PACKAGES_COMMAND = {
    "rpm": ["rpm", "-qa", "--queryformat", "%{NAME}-%{VERSION}\\t%{RELEASE}:%{ARCH}\\n"],
    "dpkg": ["dpkg-query", "--show", "--showformat", "${source:Package}\\t${Version}:${Architecture}\\n"]
  }

  def __init__(self):
    self.transport_factory = TransportFactory()

  def get_packages(self, server, *, type="rpm"):
    logging.info(f"Fetching package from {server.url}...")

    with self.transport_factory.connect(server) as session:
      out_lines, stderr_lines, exit_code = session.exec_command(PackageFetcher.LIST_PACKAGES_COMMAND[type])
      return [Package.parse(line.strip(), type=type) for line in out_lines]
