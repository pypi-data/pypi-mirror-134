import os
import csv
import subprocess
from glob import glob
from pathlib import Path
from typing import List, Dict
from collections import namedtuple

# https://github.com/nosarthur/durl/blob/main/LICENSE#L12
# TODO: site => sep
sep = '#L'
sep = '#'
b_red = '\x1b[31;1m'
end = '\x1b[0m'



Repo = namedtuple('Repo', 'url path')


def get_config_dir() -> Path:
    root = os.environ.get('XDG_CONFIG_HOME') or os.path.join(
        os.path.expanduser('~'), '.config')
    return Path(root) / 'durl'


def get_repos() -> Dict[str, Repo]:
    """

    """
    repo_config = get_config_dir() / 'repos.csv'
    if not repo_config.is_file() or repo_config.stat().st_size == 0:
        return {}
    with open(repo_config) as f:
        rows = csv.DictReader(f, ['name', 'url', 'path'],
                              restval='')  # it's actually a reader
        repos = {r['name']: Repo(r['url'], r['path'])
                for r in rows}
    return repos


def format_output(prefix, filename: str, linenumber: str=None, hit: str=None) -> str:
    """
    """
    if linenumber:
        return f'{prefix}{filename}{sep}{linenumber} {b_red}{hit}{end}'
    return prefix + filename



def grep(path:str, keyword:str) -> List[str]:
    """

    """
    cmd = f"grep -rinI --exclude-dir='.*' '{keyword}' *"
    cmd = f"rg -Sn '{keyword}' "
    # TODO: use string template to encode the command in a config file
    p = subprocess.run(cmd, shell=True, text=True, capture_output=True,
            cwd=path,)
    if p.stdout:
        return [l for l in p.stdout.split('\n') if l]
    return []


def find(path:str, keyword:str) -> List[str]:
    """

    """
    os.chdir(path)
    return glob('**/' + keyword, recursive=True)
