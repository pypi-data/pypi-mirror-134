import io
import unittest
import jsonschema
from installed_packages_diff.config import load_config


class ConfigTest(unittest.TestCase):
  def test_missing_version(self):
    config_yaml = """groups:"""
    with self.assertRaises(jsonschema.exceptions.ValidationError) as ex_ctx:
      load_config(io.StringIO(config_yaml))
    self.assertEqual("'version' is a required property",
                     ex_ctx.exception.message)

  def test_invalid_version(self):
    config_yaml = """version: 'invalid'"""
    with self.assertRaises(jsonschema.exceptions.ValidationError) as ex_ctx:
      load_config(io.StringIO(config_yaml))
    self.assertEqual("'invalid' is not one of ['installed-packages-diff/3']",
                     ex_ctx.exception.message)

  def test_minimal_config(self):
    config_yaml = """version: 'installed-packages-diff/3'"""
    config = load_config(io.StringIO(config_yaml))
    self.assertEqual(0, len(config.groups))

  def test_valid_group_type(self):
    config_yaml = """version: 'installed-packages-diff/3'
groups:
  group:
    type: rpm
    servers:
      - url: ssh://root@host
      - url: ssh://root@host
        type: dpkg
"""
    config = load_config(io.StringIO(config_yaml))
    self.assertEqual("rpm", config.groups[0].type)
    self.assertEqual("rpm", config.groups[0].servers[0].type)
    self.assertEqual("dpkg", config.groups[0].servers[1].type)

  def test_single_server(self):
    config_yaml = """version: 'installed-packages-diff/3'
groups:
  group:
    servers:
      - hostname: host
        username: root
"""
    with self.assertRaises(jsonschema.exceptions.ValidationError) as ex_ctx:
      load_config(io.StringIO(config_yaml))
    self.assertEqual("[{'hostname': 'host', 'username': 'root'}] is too short",
                     ex_ctx.exception.message)

  def test_missing_url(self):
    config_yaml = """version: 'installed-packages-diff/3'
groups:
  db:
    servers:
      - excludes: []
      - excludes: []
"""
    with self.assertRaises(jsonschema.exceptions.ValidationError) as ex_ctx:
      load_config(io.StringIO(config_yaml))
    self.assertEqual("'url' is a required property",
                     ex_ctx.exception.message)

  def test_full(self):
    config_yaml = """version: 'installed-packages-diff/3'
groups:
  db:
    servers:
      - url: ssh://root@dbdev
        excludes:
          - "missing"
      - url: ssh://root@dblive
  web:
    servers:
      - url: ssh://root@webdev
        excludes:
          - "missing"
      - url: ssh://root@weblive
"""
    config = load_config(io.StringIO(config_yaml))
    self.assertEqual([g.name for g in config.groups], ["db", "web"])
    self.assertEqual(
      [(s.url.hostname, s.url.username) for s in config.groups[1].servers],
      [("webdev", "root"), ("weblive", "root")])
    self.assertEqual(config.groups[1].servers[0].excludes, {"missing"})
    self.assertEqual(config.groups[1].servers[1].excludes, set())
