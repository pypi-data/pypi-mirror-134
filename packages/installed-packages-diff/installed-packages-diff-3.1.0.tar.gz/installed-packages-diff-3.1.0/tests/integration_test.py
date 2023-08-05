import io
import unittest

from installed_packages_diff.differ import create_diff
from installed_packages_diff.package import Package
from installed_packages_diff.printing import print_diff

input1 = """abrt-addon-kerneloops-2.14.6	9.fc35:x86_64
annobin-plugin-gcc-9.87	2.fc35:x86_64
erlang-kernel-24.1.2	2.fc35:x86_64
gcc-11.2.1	2.fc35:x86_64
gcc-c++-11.2.1	1.fc35:x86_64
gcc-gdb-plugin-11.2.1	1.fc35:x86_64
kernel-5.14.10	300.fc35:x86_64
kernel-5.14.11	200.fc34:x86_64
kernel-5.14.16	301.fc35:x86_64
kernel-core-5.14.10	300.fc35:x86_64
kernel-core-5.14.11	200.fc34:x86_64
kernel-core-5.14.16	301.fc35:x86_64
kernel-devel-5.14.10	300.fc35:x86_64
kernel-devel-5.14.11	200.fc34:x86_64
kernel-devel-5.14.16	301.fc35:x86_64
kernel-headers-5.14.9	300.fc35:x86_64
kernel-modules-5.14.10	300.fc35:x86_64
kernel-modules-5.14.11	200.fc34:x86_64
kernel-modules-5.14.16	301.fc35:x86_64
kernel-modules-extra-5.14.10	300.fc35:x86_64
kernel-modules-extra-5.14.11	200.fc34:x86_64
kernel-modules-extra-5.14.16	301.fc35:x86_64
kernel-srpm-macros-1.0	6.fc35:noarch
kernel-tools-5.14.9	300.fc35:x86_64
kernel-tools-libs-5.14.9	300.fc35:x86_64
libgcc-11.2.1	1.fc35:x86_64
libreport-plugin-kerneloops-2.15.2	6.fc35:x86_64
"""

input2 = """abrt-addon-kerneloops-2.14.6	9.fc35:x86_64
annobin-plugin-gcc-9.87	2.fc35:x86_64
erlang-kernel-24.1.2	2.fc35:x86_64
gcc-11.2.1	1.fc35:x86_64
gcc-c++-11.2.1	1.fc35:x86_64
gcc-gdb-plugin-11.2.1	1.fc35:x86_64
kernel-5.14.10	300.fc35:x86_64
kernel-5.14.11	200.fc34:x86_64
kernel-5.14.16	301.fc35:x86_64
kernel-core-5.14.10	300.fc35:x86_64
kernel-core-5.14.11	200.fc34:x86_64
kernel-core-5.14.16	301.fc35:x86_64
kernel-devel-5.14.10	300.fc35:x86_64
kernel-devel-5.14.11	200.fc34:x86_64
kernel-devel-5.14.16	301.fc35:x86_64
kernel-headers-5.14.9	300.fc35:x86_64
kernel-modules-5.14.10	300.fc35:x86_64
kernel-modules-5.14.11	200.fc34:x86_64
kernel-modules-5.14.16	301.fc35:x86_64
kernel-modules-extra-5.14.10	300.fc35:x86_64
kernel-modules-extra-5.14.11	200.fc34:x86_64
kernel-modules-extra-5.14.16	301.fc35:x86_64
kernel-tools-5.14.9	300.fc35:x86_64
kernel-tools-libs-5.14.9	300.fc35:x86_64
libgcc-11.2.1	1.fc35:i686
libgcc-11.2.1	1.fc35:x86_64
libreport-plugin-kerneloops-2.15.2	6.fc35:x86_64
"""


class IntegerationTest(unittest.TestCase):
  def test_all(self):
    aPackages = [Package.parse(line) for line in input1.splitlines()]
    bPackages = [Package.parse(line) for line in input2.splitlines()]
    installed_packages_diff = create_diff(aPackages, bPackages, includeEqual=False)
    with io.StringIO() as buf:
      print_diff("serverA", "serverB", installed_packages_diff, file=buf)
      print(buf.getvalue())
      self.assertEqual([l.strip() for l in """
= serverA serverB =
gcc-11.2.1                               2.fc35:x86_64                            1.fc35:x86_64
kernel-srpm-macros-1.0                   6.fc35:noarch                            missing
libgcc-11.2.1                            1.fc35:x86_64                            1.fc35:i686""".splitlines()],
                       [l.strip() for l in buf.getvalue().splitlines()])
