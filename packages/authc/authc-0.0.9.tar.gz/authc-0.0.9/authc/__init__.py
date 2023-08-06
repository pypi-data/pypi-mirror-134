import json
import os
import subprocess
import sys
import threading
import time
from typing import Any, Dict, List, Tuple

import codefast as cf
from codefast.patterns.singleton import SingletonMeta
from codefast.utils import sleep


class Authentication(object):
    """ Authentication with C++.
    """
    def __init__(self) -> None:
        self.bin = 'bin/dauth' if sys.platform == 'darwin' else 'bin/lauth'
        self.bin_path: str = os.path.join(cf.io.dirname(), self.bin)

    def get_accounts(self) -> Dict[str, str]:
        stdout: str = ''
        _accounts = {}
        try:
            cmd = self.bin_path + ' -a'
            stdout = subprocess.check_output(
                cmd, shell=True,
                stderr=subprocess.DEVNULL).decode('utf-8').strip()
            _accounts = json.loads(stdout)
            _accounts = dict(sorted([(k, v) for k, v in _accounts.items()]))
        except json.decoder.JSONDecodeError as e:
            cf.io.copy(self.bin_path, '/tmp/auth')
            cf.error('failed to decode json {}, '.format(stdout, e))
        except Exception as e:
            cf.error('failed to query secrets: {}'.format(e))
        finally:
            return _accounts

    def register(self):
        cmd = self.bin_path + ' -r'
        try:
            subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            pass

    def update(self):
        cmd = self.bin_path + ' -u'
        try:
            subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            pass


def authc() -> Dict[str, str]:
    _auth = Authentication()
    if len(sys.argv) > 1 and sys.argv[1] == '-r':
        cf.info('registering...')
        _auth.register()
        return

    lst, thread_number = [], 7
    for _ in range(thread_number):
        threading.Thread(target=lambda d: d.append(_auth.get_accounts()),
                         args=(lst, ),
                         daemon=True).start()

    # Also add a thread to update local cache
    threading.Thread(target=lambda d: d.append(_auth.update()),
                     args=(lst, ),
                     daemon=True).start()

    TIMEOUT, sleep_time = 10, 0.1
    while TIMEOUT >= 0:
        time.sleep(sleep_time)
        TIMEOUT -= sleep_time
        if lst:
            return lst[0]
    return {}


class AuthOnce(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._info = {}

    def info(self):
        if not self._info:
            self._info = authc()
        return self._info
