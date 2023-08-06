import json
import os
import subprocess
import sys
import threading
import time
from typing import Any, Dict, List, Tuple

import codefast as cf
from codefast.patterns.singleton import SingletonMeta


class Authentication(object):
    """ Authentication with C++.
    """
    @staticmethod
    def run() -> Dict[str, str]:
        bin: str
        stdout: str
        _accounts = {}
        try:
            which_bin = 'bin/dauth' if sys.platform == 'darwin' else 'bin/lauth'
            cmd = os.path.join(cf.io.dirname(), which_bin) + ' -a'
            stdout = subprocess.check_output(
                cmd, shell=True,
                stderr=subprocess.DEVNULL).decode('utf-8').strip()
            _accounts = json.loads(stdout)
            _accounts = dict(sorted([(k, v) for k, v in _accounts.items()]))
        except json.decoder.JSONDecodeError as e:
            cf.io.copy(bin, '/tmp/auth')
            cf.error('failed to decode json {}, '.format(stdout, e))
        except Exception as e:
            cf.error('failed to query secrets: {}'.format(e))
        finally:
            return _accounts


def authc() -> Dict[str, str]:
    def _fetch_account(_lst):
        _lst.append(Authentication.run())

    lst = []

    for _ in range(7):
        threading.Thread(target=_fetch_account, args=(lst, ),
                         daemon=True).start()

    for _ in range(100):
        if lst:
            return lst.pop()
        time.sleep(0.1)

    return {}


class AuthOnce(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._info = {}

    def info(self):
        if not self._info:
            self._info = authc()
        return self._info

