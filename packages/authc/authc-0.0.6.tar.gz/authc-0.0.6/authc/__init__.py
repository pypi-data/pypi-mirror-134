import codefast as cf
import threading
from typing import List, Dict, Any, Tuple
import os
import subprocess
import json
import sys
import time


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


def _fetch_account(lst):
    lst.append(Authentication.run())


def authc() -> Dict[str, str]:
    lst = []
    for _ in range(7):
        threading.Thread(target=_fetch_account, args=(lst, ),
                         daemon=True).start()

    for _ in range(100):
        if lst:
            return lst.pop()
        time.sleep(0.1)

    return {}
