import sys
import os
from fuse import FUSE, fuse_exit
import subprocess
import time
import mlflow
import glob
import json

import infinstor
from infinstor.infinfs.infinfs import InfinFS

INPUT_SPEC_CONFIG = os.getcwd() + "/infin-input-spec.conf"

def launch_fuse_infinfs(ifs):
    mountpath = ifs.get_mountpoint()
    print("Unmount " + mountpath)
    umountp = subprocess.Popen(['umount', '-lf', mountpath], stdout=sys.stdout, stderr=subprocess.STDOUT)
    umountp.wait()
    FUSE(ifs, mountpath, nothreads=True, foreground=True)
    print("exiting")

def infin_declare_input(*mountpaths):
    if 'INFINSTOR_SERVICE' not in os.environ:
        print("No action needed")
        return

    service_name = os.environ.get('INFINSTOR_SERVICE')
    print('Infinstor service: ' + service_name)

    ##Always re-mount if a mountpoint exists
    force = True
    index = -1
    for mpath in mountpaths:
        index = index+1
        if not mpath or mpath[0] != '/':
            raise Exception("Mountpath must be an absolute path")
        mpath = mpath.rstrip('/')

        if not os.path.exists(mpath):
            os.makedirs(mpath)

        print("Mounting...")
        fuse_process = subprocess.Popen(['python', os.path.realpath(__file__), mpath, str(index)],
                          stdout=sys.stdout, stderr=subprocess.STDOUT)
    ##Wait for some time for mounts to become visible
    time.sleep(3)
    print("Mounted")

def infin_log_output(output_dir):
    if 'INFINSTOR_SERVICE' not in os.environ:
        print("No action needed")
        return
    if mlflow.active_run():
        infinstor.log_all_artifacts_in_dir(None, None, output_dir, delete_output=False)
    else:
        print('No active run')

if __name__ == '__main__':
    mountpoint = sys.argv[1]
    spec_index = sys.argv[2]
    with open(INPUT_SPEC_CONFIG) as fp:
        specs = json.load(fp)

    spec = None
    int_index = int(spec_index)
    if int_index == 0:
        if type(specs) == list:
            spec = specs[0]
        else:
            spec = specs
    else:
        if type(specs) == list:
            spec = specs[int_index]

    if spec == None:
        print('Error no input spec found, skipping mount')
        exit(-1)

    service_name = os.environ.get('INFINSTOR_SERVICE')
    ifs = InfinFS(mountpoint, spec, service_name)
    launch_fuse_infinfs(ifs)
    exit(0)
