import os
import re
import sys
import shutil

from vendor import yaml
from vendor import requests

# Temporarily disable warning about SSL on Python < 2.7.9
requests.packages.urllib3.disable_warnings()

_cache = dict()
_home = os.path.dirname(__file__)
_headers = {
  "X-Github-Username": os.environ.get("BE_GITHUB_USERNAME"),
  "X-Github-API-Token": os.environ.get("BE_GITHUB_API_TOKEN")
}
_files = [
    "be.yaml",
    "inventory.yaml",
    "templates.yaml",
    "environment.yaml",
    "tasks.yaml",
    "users.yaml",
]


def projects():
    """Return list of available projects"""
    return os.listdir(os.getcwd())


def presets_dir():
    """Return presets directory"""
    default_root = os.path.join(os.path.expanduser("~"), ".be", "presets")
    root = os.environ.get("BE_PRESETSDIR", default_root)
    if not os.path.exists(root):
        os.makedirs(root)
    return root


def api_from_repo(endpoint):
    """Produce an api endpoint from a repo address"""
    api_endpoint = endpoint.split("github.com", 1)[-1]
    api_endpoint = api_endpoint.rsplit(".git", 1)[0]
    return "https://api.github.com/repos" + api_endpoint


def remove_preset(preset):
    preset_dir = os.path.join(presets_dir(), preset)
    shutil.rmtree(preset_dir)


def pull_preset(repository, preset_dir):
    """Pull remote repository into `presets_dir`"""
    api_endpoint = api_from_repo(repository)

    kwargs = {"verify": False}
    if _headers["X-Github-Username"] is not None:
        kwargs["headers"] = _headers

    response = requests.get(api_endpoint + "/contents", **kwargs)
    if response.status_code == 403:
        raise IOError("Patience: You can't pull more than 40 presets per hour")

    if not os.path.exists(preset_dir):
        os.makedirs(preset_dir)

    for f in response.json():
        fname, download_url = f["name"], f["download_url"]
        if fname not in _files:
            continue

        response = requests.get(download_url, verify=False)
        fpath = os.path.join(preset_dir, fname)
        with open(fpath, "w") as f:
            f.write(response.text)


def local_presets():
    """Return local presets"""
    return os.listdir(presets_dir())


def github_presets():
    """Return remote presets hosted on GitHub"""
    addr = ("https://raw.githubusercontent.com"
            "/mottosso/be-presets/master/presets.json")
    return {package["name"]: package["repository"]
            for package in requests.get(
                addr, verify=False).json().get("presets")}


def project_exists(project):
    return os.path.exists()


def copy_preset(preset_dir, dest):
    os.makedirs(dest)

    for fname in os.listdir(preset_dir):
        src = os.path.join(preset_dir, fname)
        shutil.copy2(src, dest)


def load_templates(project):
    """Return templates given name of project

    Arguments:
        project (str): Name of project

    """

    return resolve_references(load(project, "templates"))


def load_inventory(project):
    """Return available inventory from cwd

    Arguments:
        project (str): Name of project

    """

    return load(project, "inventory")


def load_be(project):
    return load(project, "be")


def load(project, fname):
    if fname not in _cache:
        path = os.path.join(os.getcwd(), project, "%s.yaml" % fname)
        try:
            with open(path) as f:
                _cache[fname] = yaml.load(f) or dict()
        except IOError:
            sys.stderr.write("PROJECT ERROR: %s.yaml not "
                             "defined for project \"%s\"" % (fname, project))
            sys.exit(1)

    return _cache[fname]


def resolve_references(templates):
    """Resolve {@} occurences by expansion

    Given a dictionary {"a": "{@b}/x", "b": "{key}/y"}
    Return {"a", "{key}/y/x", "b": "{key}/y"}

    {
        key: {@reference}/{variable} # pattern
    }

    In plain english, it looks within `pattern` for
    references and replaces them with the value of the
    matching key.

    {
        root: {cwd}/{project}
        item: {@root}/{item}
    }

    In the above case, `item` is referencing `root` which
    is resolved into this.

    {
        item: {cwd}/{project}/{item}
    }

    Example:
        >>> templates = {"a": "{@b}/x", "b": "{key}/y"}
        >>> resolved = _resolve_references(templates)
        >>> assert resolved["a"] == "{key}/y/x"

    """

    def repl(match):
        key = pattern[match.start():match.end()].strip("@{}")
        if key not in templates:
            sys.stderr.write("Unresolvable reference: \"%s\"" % key)
            sys.exit(1)
        return templates[key]

    for key, pattern in templates.copy().iteritems():
        templates[key] = re.sub("{@\w+}", repl, pattern)

    return templates


def test_template():
    os.chdir("../demo")
    print load_templates("thedeal")
