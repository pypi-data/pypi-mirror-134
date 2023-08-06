from __future__ import print_function
import asyncio
import os
import boto3
import subprocess
import re
import sys

local_cache_data = "/local_s3_cache/data"
local_cache_metadata = "/local_s3_cache/metadata/"
PREFETCH_SCRIPT = "infin_prefetch.py"
SEP = "-_-"

def printerr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_s3_client(endpointurl=None, proxy_profile=None):
    if proxy_profile:
        session = boto3.Session(profile_name=proxy_profile)
        return session.client('s3', endpoint_url=endpointurl)
    else:
        return boto3.client('s3', endpoint_url=endpointurl)

def download_objects(local_path, tmp_local_file, bucket, remote_path,
                     endpointurl=None, proxy_profile=None):
    printerr("Download from bucket {0}, path {1} to the local path {2} from endpoint {3}"
             .format(bucket, remote_path, tmp_local_file, endpointurl))
    asyncio.run(download_objects_async(tmp_local_file, bucket, remote_path, endpointurl, proxy_profile))
    printerr('rename {0} to {1}'.format(tmp_local_file, local_path))
    os.rename(tmp_local_file, local_path)

async def download_one_object(local_path, bucket, remote_path, endpointurl, proxy_profile):
    s3_client = get_s3_client(endpointurl, proxy_profile)
    s3_client.download_file(bucket, remote_path, local_path)

async def download_objects_async(local_path, bucket, remote_path, endpointurl, proxy_profile):
    ##download the file
    download_task = asyncio.create_task(download_one_object(local_path, bucket, remote_path,
                                                            endpointurl, proxy_profile))

    ##Prefetch in parallel
    #local_parent_dir = os.path.dirname(local_path)
    #remote_parent_dir = os.path.dirname(remote_path)
    #asyncio.run(create_prefetch_task(local_path, local_parent_dir, remote_parent_dir))
    await download_task

def is_prefetch_running():
    out = subprocess.run(['pgrep', '-alf', 'python'], capture_output=True)
    if PREFETCH_SCRIPT in out.stdout.decode("utf-8"):
        return True
    else:
        return False

async def create_prefetch_task(local_path, local_parent_dir, remote_parent_dir):
    #Create a batch for download
    create_prefetch_batch(local_path, local_parent_dir, remote_parent_dir)

    #Check if process already running
    if not is_prefetch_running():
        ##launch the prefetch process
        fh = open('/tmp/logfile.log', 'a')
        subprocess.Popen(['nohup', 'python', "infin_prefetch.py"],
                         stdout=fh,
                         stderr=fh,
                         preexec_fn=os.setpgrp
                         )


def create_prefetch_batch(local_path, local_parent_dir, remote_parent_dir, bucket):
    batch_location =  local_cache_metadata + "/batches"
    batch_dir_name = remote_parent_dir.replace("/", SEP)

    client = get_s3_client()
    dirents = []
    target_obj = os.path.basename(local_path)
    obj_list_response = client.list_objects_v2(Bucket=bucket, Prefix=remote_parent_dir,
                                               StartAfter=target_obj, MaxKeys=100)
    candidate_batch = []
    if 'Contents' in obj_list_response:
        for key in obj_list_response['Contents']:
            remote_path = key['Key']
            candidate_batch.append(remote_path)

    first = os.path.basename(candidate_batch[0])
    last = os.path.basename(candidate_batch[-1])

    batch_file_name = first + SEP + last
    batch_dir_path = batch_location + "/" + batch_dir_name
    batch_file_path = batch_dir_path +"/" + batch_file_name + ".batch"
    redundant = check_redundant_batch(batch_dir_path, first)
    if not redundant:
        with open('batch_file_path', "w") as fh:
            for f in candidate_batch:
                fh.write(f)
                fh.write("/")
    return

def check_redundant_batch(batch_dir_path, first):
    batch_files = os.listdir(batch_dir_path)
    for bfile in batch_files:
        batch_filename = os.path.basename(bfile)
        beginend = re.sub('.batch$', "", batch_filename)
        beginning, end = beginend.split(SEP)
        if first >= beginning and first <= end:
            return True
        else:
            return False



