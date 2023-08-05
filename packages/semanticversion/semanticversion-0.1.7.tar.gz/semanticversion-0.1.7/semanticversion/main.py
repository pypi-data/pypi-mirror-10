import copy
import datetime
import json
import time


class Repository(object):

    def __init__(self):
        self.data = {
            'released': [],
        }
        self.names = {
            'change': ['time', 'category', 'description', ],
            'bump': {
                'minor': ["minor"],
                'major': ["major"],
                'patch': ["patch"],
            },
        }
        self.init_release()

    def init_release(self):
        self.data["unreleased"] = {}
        self.data["unreleased"]["changes"] = []
        self.data["unreleased"]["properties"] = {
            "date": "Not released",
            "semver": "-",
        }

    def append(self, category, description):
        c = {
            'time': datetime.datetime.now().strftime("%Y-%m-%d"),
            'category': category,
            'description': description,
        }
        r = []
        for k in self.names["change"]:
            r.append(c[k])
        self.data["unreleased"]["changes"].append(r)
        return self

    def get_bump(self, release):

        minor = 0
        major = 0
        patch = 0

        r_index = self.names['change'].index("category")
        for r in release["changes"]:
            x = r[r_index]
            if x in self.names["bump"]["minor"]:
                minor = 1
            elif x in self.names["bump"]["major"]:
                major = 1
            elif x in self.names["bump"]["patch"]:
                patch = 1

        if major:
            return 1, 0, 0
        if minor:
            return 0, 1, 0
        if patch:
            return 0, 0, 1
        return major, minor, patch

    def dumps(self):
        return json.dumps(self.data, indent=2, sort_keys=True)

    @classmethod
    def loads(cls, jsdump):
        r = cls()
        r.data = json.loads(jsdump)
        return r

    def release(self, text=u""):
        semver = self.versions()[-1]
        r = self.data["unreleased"]
        major, minor, patch = self.get_bump(r)
        if patch:
            semver[2] += 1
        if minor:
            semver[1] += 1
            semver[2] = 0
        if major:
            semver[0] += major
            semver[1] = 0
            semver[2] = 0

        r["properties"]["semver"] = semver
        r["properties"]["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
        self.data["released"].append(r)
        self.init_release()

    def versions(self):
        versions = [x["properties"]["semver"] for x in self.data["released"]]
        versions.append([0, 0, 0])
        return copy.deepcopy(sorted(versions))

    def _package(self):
        pages = []
        for r in self.data["released"]:
            page = {}
            for date, category, comment in r["changes"]:
                if category not in page:
                    page[category] = []
                page[category].append(comment)
            # for k in page:
            #    page[k] = "\n".join(page[k])

            page["properties"] = r["properties"]
            pages.append(page)
        return sorted(
            pages, key=lambda x: x["properties"]["semver"], reverse=True)

    def export_json(self):
        return json.dumps(self._package())

    def export_version(self):
        v =  ".".join([str(x) for x in self.versions()[-1]])
        
        return v 
    
    def export_python(self):
        v =  ".".join([str(x) for x in self.versions()[-1]])
        return "__version__ = '%s'"%v

    def export_md(self):
        text = ""
        for r in self._package():
            ver = "%s\n" % (
                ".".join([str(x) for x in r["properties"]["semver"]]))
            text += ver
            text += "=" * len(ver.strip())
            text += "\n"
            text += "\n"
            if "change" in r:
                text += "## Changes ##\n"
                for t in r["change"]:
                    text += "* %s\n" % (t)
                text += "\n"

            if "new" in r:
                text += "## New ##\n"
                for t in r["new"]:
                    text += "* %s\n" % (t)
                text += "\n"

            if "fix" in r:
                text += "## Fixes ##\n"
                for t in r["fix"]:
                    text += "* %s\n" % (t)
                text += "\n"
        return text.strip()
