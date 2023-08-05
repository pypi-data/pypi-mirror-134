from typing import List
import logging
import subprocess

from .transport import Transport


class LocalTransport(Transport):
  def exec_command(self, command: List) -> [str, str, int]:
    logging.info(f"Fetching packages locally...")

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    out, err = proc.communicate()
    out_lines = out.decode("utf-8").splitlines()
    err_lines = err.decode("utf-8").splitlines()
    exit_status = proc.returncode
    if exit_status != 0:
      print(err.splitlines())
      raise ValueError(
        f"Querying packages failed with exit status {exit_status}")
    return out_lines, err_lines, exit_status
