from typing import List, Callable
import re


def _filter_diff(diffAB: list, aExcludes: List[Callable], bExcludes: List[Callable], includeEqual):
  filtered = []
  for (packageName, versionA, versionB) in diffAB:
    excluded = [packageName for exclude in aExcludes if exclude(packageName)] \
               or [packageName for exclude in bExcludes if exclude(packageName)] \
               or [versionA for exclude in aExcludes if exclude(versionA)] \
               or [versionB for exclude in bExcludes if exclude(versionB)]
    if not excluded and (versionA != versionB or includeEqual):
      filtered.append((packageName, versionA, versionB))

  return filtered


def _to_package_map(packageList):
  packageMap = {}
  for package in packageList:
    versions = packageMap.get(package.name, [])
    versions.append(package.version)
    packageMap[package.name] = versions
  return packageMap


def _to_matcher_list(list: List[str]) -> List[Callable]:
  matcher_list = []
  for s in list:
    if s.startswith("/") and s.endswith("/"):
      regex = re.compile(s)
      matcher_list.append(lambda x: regex.match(x))
    else:
      matcher_list.append(lambda x: x and x.startswith(s))
  return matcher_list


def create_diff(listA, listB, *, aExcludes=None, bExcludes=None,
                includeEqual=False):
  aExcludes = _to_matcher_list(aExcludes or [])
  bExcludes = _to_matcher_list(bExcludes or [])

  mapA = _to_package_map(listA)
  mapB = _to_package_map(listB)
  diff = []
  for packageName in mapA:
    versionsA = mapA[packageName]
    versionsB = mapB.get(packageName, [])
    if len(versionsA) == 1 and len(versionsB):
      diff.append((packageName, versionsA[0], versionsB[0]))
    else:
      for versionA in versionsA:
        if versionA in versionsB:
          diff.append((packageName, versionA, versionA))
          versionsB.remove(versionA)
        elif not versionA in versionsB:
          diff.append((packageName, versionA, "missing"))
      for versionB in versionsB:
        if not versionB in versionsA:
          diff.append((packageName, "missing", versionB))
  for packageName in mapB:
    if packageName not in mapA:
      for versionB in mapB[packageName]:
        diff.append((packageName, "missing", versionB))

  return _filter_diff(diff, aExcludes, bExcludes, includeEqual)
