import json
import os
import subprocess

from ios_device.servers.crash_log import CrashLogService
from ios_device.util.lockdown import LockdownClient


def get_crash_list(udid=None):
    return CrashLogService(udid=udid).crash_server.read_directory('/')


def get_app_crash_list(udid=None, app=''):
    crash_list = get_crash_list(udid=udid)
    return sorted(list(filter(lambda x: app in x, crash_list)), reverse=True)


def delete_crash(udid=None, app=''):
    app_crash_list = get_app_crash_list(udid=udid, app=app)
    for x in app_crash_list:
        CrashLogService(udid=udid).crash_server.file_remove('//' + x)


def export_crash(udid=None, app='', path=None):
    app_crash_list = get_app_crash_list(udid=udid, app=app)
    if len(app_crash_list) == 0:
        raise Exception(f'没有名称包含{app}的crash文件' )
    else:
        data = CrashLogService(udid=udid).crash_server.get_file_contents('//' + app_crash_list[0])
        local_crash_file = os.path.join(path, 'crash.ips')
        print(local_crash_file)
        with open(local_crash_file, 'wb') as (fp):
            fp.write(data)


def analyze_crash(file_path):
    if os.path.getsize(file_path) <= 0:
        return

    with open(file_path, 'r') as f:
        data = f.readlines()[0]
        print(json.loads(data))
        return f.read()


if __name__ == '__main__':
    # delete_crash(app='Lark')
    # export_crash(app='DUApp', path='/Users/zhuhuiping/Desktop/')
    # print(get_app_crash_list(app='DUApp'))
    analyze_crash('/Users/zhuhuiping/Desktop/crash.ips')
