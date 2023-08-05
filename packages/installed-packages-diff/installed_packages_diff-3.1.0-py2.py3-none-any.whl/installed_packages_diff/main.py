from optparse import OptionParser
import sys

from .config import load_config
from .fetcher import PackageFetcher
from .differ import create_diff
from .printing import print_diff
import logging


def diff_server(serverA, serverB):
  pkgFetcher = PackageFetcher()
  devPkgs = pkgFetcher.get_packages(serverA, type=serverA.type)
  prodPkgs = pkgFetcher.get_packages(serverB, type=serverB.type)
  installed_packages_diff = create_diff(devPkgs, prodPkgs,
                                        aExcludes=serverA.excludes,
                                        bExcludes=serverB.excludes,
                                        includeEqual=False)
  print_diff(serverA.url.hostname, serverB.url.hostname, installed_packages_diff)


def _parse_args():
  opt_parser = OptionParser()
  opt_parser.add_option("-c", "--config", dest="config_file",
                        help="Path to config file", metavar="CONFIG_FILE",
                        default="./config.yaml")
  opt_parser.add_option("-v", "--verbose", dest="verbose",
                        help="Increase output", metavar="VERBOSE",
                        default=False)

  options, args = opt_parser.parse_args()
  option_vars = vars(options)
  return (option_vars, args)


def main():
  logging.basicConfig(stream=sys.stderr,
                      format='%(asctime)s %(message)s',
                      level=logging.INFO)

  option_vars, args = _parse_args()
  logging.getLogger().setLevel(
    logging.INFO if option_vars["verbose"] else logging.WARN)

  config = load_config(option_vars.get("config_file"))
  for group in config.groups:
    baselineServer = group.servers[0]
    for otherServer in group.servers[1:]:
      diff_server(baselineServer, otherServer)
