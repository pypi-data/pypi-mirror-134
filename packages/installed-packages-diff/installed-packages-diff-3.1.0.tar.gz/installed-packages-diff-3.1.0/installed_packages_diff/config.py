from urllib.parse import urlparse
import logging

from yaml import load
import jsonschema

try:
  from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
  from yaml import Loader, Dumper

CONFIG_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "id": "config-0.json",
  "type": "object",
  "required": ["version"],
  "properties": {
    "version": {
      "type": "string",
      "enum": [
        "installed-packages-diff/3"
      ]
    },
    "groups": {
      "id": "#/properties/groups",
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9._-]+$": {
          "$ref": "#/definitions/group"
        }
      },
      "additionalProperties": False
    }
  },
  "additionalProperties": False,
  "definitions": {
    "group": {
      "id": "#/definitions/group",
      "type": "object",
      "properties": {
        "type": {
          "$ref": "#/definitions/pkg-type"
        },
        "servers": {
          "type": "array",
          "minItems": 2,
          "items": {
            "$ref": "#/definitions/server"
          }
        }
      },
      "additionalProperties": False
    },
    "server": {
      "id": "#/definitions/server",
      "type": "object",
      "properties": {
        "type": {
          "$ref": "#/definitions/pkg-type"
        },
        "url": {"type": "string"},
        "excludes": {"type": "array",
                     "items": {
                       "type": "string"
                     }},
      },
      "additionalProperties": False,
      "required": ["url"]
    },
    "pkg-type": {
      "id": "#/definitions/pkg-type",
      "type": "string",
      "enum": ["dpkg", "rpm"]
    }
  }
}


class Server(object):
  def __init__(self, raw, *, type_from_group=None):
    self.url = urlparse(raw["url"])
    self.excludes = {e for e in raw.get("excludes", [])}
    self.type = raw.get("type", type_from_group)


class Group(object):
  def __init__(self, name, raw):
    self.name = name
    self.type = raw.get("type", "rpm")
    self.servers = [Server(server, type_from_group=self.type) for server in
                    raw["servers"]]


class Config(object):
  def __init__(self, raw):
    self.raw = raw
    groups_dict = self.raw.get("groups", {})
    self.groups = [Group(name, groups_dict[name]) for name in groups_dict]


def load_config(input):
  if isinstance(input, str):
    logging.info(f"Opening config {input}...")
    input = open(input, 'rb')

  with input as stream:
    data = load(stream, Loader=Loader)
    jsonschema.validate(data, schema=CONFIG_SCHEMA)
    return Config(data)
