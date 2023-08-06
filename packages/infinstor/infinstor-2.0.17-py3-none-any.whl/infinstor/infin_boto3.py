from datetime import datetime, timezone
import builtins
import boto3
from botocore.response import StreamingBody
import functools
import os
import sys
from os.path import expanduser
import json
import mlflow
import infinstor_mlflow_plugin
from mlflow.tracking import MlflowClient
from urllib.parse import urlparse, quote
from urllib.request import urlretrieve, urlopen
from requests.exceptions import HTTPError
import requests
from infinstor import bootstrap

INPUT_SPEC_CONFIG = os.getcwd() + "/infin-input-spec.conf"
declared_input_sources = []

class ListObjectsPaginator():
    def __init__(self, type2, infin_boto_client, bucketlist):
        self.type2 = type2
        self.infin_boto_client = infin_boto_client
        self.bucketlist = bucketlist
        self.next_token = None
        self.finished = False

    def paginate(self, **kwargs):
        if 'Bucket' not in kwargs:
            raise ValueError("Bucket must be specified for list-objects-v2 paginate")
        self.bucket = kwargs['Bucket']
        if self.bucket not in self.bucketlist:
            passthru = self.infin_boto_client.defaultClient.get_paginator('list_objects_v2')
            return passthru.paginate(**kwargs)
        else:
            self.kwargs = kwargs
            return self

    def __iter__(self):
        return self
    def __next__(self):
        if self.finished:
            raise StopIteration
        if (self.next_token):
            if self.type2:
                self.kwargs['ContinuationToken'] = self.next_token
            else:
                self.kwargs['Marker'] = self.next_token
        if self.type2:
            rv = self.infin_boto_client.list_objects_v2(None, **self.kwargs)
            if 'NextContinuationToken' in rv:
                self.next_token = rv['NextContinuationToken']
                del rv['NextContinuationToken']
            else:
                self.finished = True
            return rv
        else:
            rv = self.infin_boto_client.list_objects(None, **self.kwargs)
            if 'NextMarker' in rv:
                self.next_token = rv['NextMarker']
                del rv['NextMarker']
            else:
                self.finished = True
            return rv

class Bucket():
    def __init__(self, name):
        self.name = name

class BucketsCollection():
    def __init__(self, allbuckets):
        self.buckets=[]
        for b in allbuckets:
            self.buckets.append(Bucket(b))
    def all(self):
        return self.buckets

class InfinBotoResource():
    def __init__(self, defaultResource, bucketlist):
        self.defaultResource = defaultResource
        self.bucketscollection = BucketsCollection(bucketlist)

    def __getattr__(self, attr):
        if attr == 'buckets':
            return self.bucketscollection
        else:
            return getattr(self.defaultResource, attr)

class InfinBotoClient():
    def __init__(self, defaultClient, spec, bucket, prefix):
        # self.__class__ = type(baseObject.__class__.__name__,
        #                       (self.__class__, baseObject.__class__),
        #                       {})
        # self.__dict__ = baseObject.__dict__
        self.defaultClient = defaultClient
        self.input_spec = spec
        # for infinsnap and infinslice, bucket and prefix are from the
        # INPUT_SPEC_CONFIG file. For infinsnap-implicit, bucket and prefix are
        # specified in the call that we are intercepting
        self.bucket = bucket
        self.prefix = prefix

    def list_objects(self, *args, **kwargs):
        if self.input_spec['type'] == 'mlflow-run-artifacts':
            request_bucket = kwargs['Bucket']
            request_prefix = kwargs.get('Prefix')
            if is_declared_source(request_bucket, request_prefix):
                kwargs['Bucket'] = self.bucket
                if request_prefix:
                    kwargs['Prefix'] = self.prefix + "/" + request_prefix.lstrip('/')
                else:
                    kwargs['Prefix'] = self.prefix
                return self.defaultClient.list_objects(*args, **kwargs)
        elif self.input_spec['type'] == 'infinsnap' or self.input_spec['type'] == 'infinslice':
            if self.bucket:
                request_bucket = self.bucket
                request_prefix = self.prefix
            elif kwargs['Bucket']:
                request_bucket = kwargs['Bucket']
                request_prefix = kwargs['Prefix']
            else:
                raise ValueError("bucket must be specified")
            if request_bucket in self.input_spec['bucketlist']:
                kwargs['Bucket'] = request_bucket
                kwargs['Prefix'] = request_prefix
                return self.list_objects_at(False, *args, **kwargs)
            else:
                return self.defaultClient.list_objects(*args, **kwargs)
        elif self.input_spec['type'] == 'infinsnap-implicit':
            if kwargs['Bucket'] in self.input_spec['bucketlist']:
                return self.list_objects_at(False, *args, **kwargs)
            else:
                return self.defaultClient.list_objects(*args, **kwargs)
        else:
            return self.defaultClient.list_objects(*args, **kwargs)

    def list_objects_v2(self, *args, **kwargs):
        if self.input_spec['type'] == 'mlflow-run-artifacts':
            request_bucket = kwargs['Bucket']
            request_prefix = kwargs.get('Prefix')
            if is_declared_source(request_bucket, request_prefix):
                kwargs['Bucket'] = self.bucket
                if request_prefix:
                    kwargs['Prefix'] = self.prefix + "/" + request_prefix.lstrip('/')
                else:
                    kwargs['Prefix'] = self.prefix
                return self.defaultClient.list_objects_v2(*args, **kwargs)
        elif self.input_spec['type'] == 'infinsnap' or self.input_spec['type'] == 'infinslice':
            if self.bucket:
                request_bucket = self.bucket
                request_prefix = self.prefix
            elif kwargs['Bucket']:
                request_bucket = kwargs['Bucket']
                request_prefix = kwargs['Prefix']
            else:
                raise ValueError("bucket must be specified")
            if request_bucket in self.input_spec['bucketlist']:
                kwargs['Bucket'] = request_bucket
                kwargs['Prefix'] = request_prefix
                return self.list_objects_at(True, *args, **kwargs)
            else:
                return self.defaultClient.list_objects_v2(*args, **kwargs)
        elif self.input_spec['type'] == 'infinsnap-implicit':
            if kwargs['Bucket'] in self.input_spec['bucketlist']:
                return self.list_objects_at(True, *args, **kwargs)
            else:
                return self.defaultClient.list_objects_v2(*args, **kwargs)
        else:
            return self.defaultClient.list_objects_v2(*args, **kwargs)

    def download_file(self, *args, **kwargs):
        if self.input_spec['type'] == 'mlflow-run-artifacts':
            request_bucket = args[0]
            request_file = args[1]
            if is_declared_source(request_bucket, request_file):
                arglist = list(args)
                arglist[0] = self.bucket
                if request_file:
                    arglist[1] = self.prefix + "/" + request_file.lstrip('/')
                else:
                    arglist[1] = self.prefix
                args = tuple(arglist)
                return self.defaultClient.download_file(*args, **kwargs)
        elif self.input_spec['type'] == 'infinsnap' or self.input_spec['type'] == 'infinslice'\
                                            or self.input_spec['type'] == 'infinsnap-implicit':
            request_bucket = args[0]
            request_file = args[1]
            if request_bucket in self.input_spec['bucketlist']:
                versionId, presignedUrl = self.get_version_id(request_bucket, request_file)
                if (versionId != None):
                    if 'ExtraArgs' in kwargs:
                        kwargs['ExtraArgs']['VersionId'] = versionId
                    else:
                        kwargs['ExtraArgs'] = {'VersionId': versionId}
                    return self.defaultClient.download_file(*args, **kwargs)
                else:
                    raise ValueError('download_file: versionId not present. Is InfinSnap enabled?')
            else:
                return self.defaultClient.download_file(*args, **kwargs)
        else:
            return self.defaultClient.download_file(*args, **kwargs)

    def get_version_id(self, bucket, prefix):
        tokfile = os.path.join(expanduser("~"), ".infinstor", "token")
        attempt = 0
        while attempt < 2:
            if attempt == 0:
                force = False
            else:
                print('get_version_id: attempt = ' + str(attempt) + ', force True')
                force = True
            attempt = attempt + 1
            token, service = infinstor_mlflow_plugin.tokenfile.get_token(builtins.region,
                tokfile, force)
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': token
                }
            url = 'https://' + builtins.apiserver + '/webhdfs/v1/' + quote(prefix)\
                    + '?op=GETFILESTATUS&bucket=' + bucket\
                    + '&gets3url=true'
            if self.input_spec['type'] == 'infinsnap-implicit':
                url = url + '&time=' + str(self.input_spec['epoch_time'])
            elif self.input_spec['type'] == 'infinsnap':
                time_spec = self.input_spec['time_spec']
                url = url + '&time=' + str(self.infinsnap_to_epoch(time_spec))
            elif self.input_spec['type'] == 'infinslice':
                time_spec = self.input_spec['time_spec']
                st, en = self.infinslice_to_epochs(time_spec)
                url = url + '&timeBegin=' + str(st) + '&time=' + str(en)
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
            except HTTPError as http_err:
                print('HTTP error occurred: ' + str(http_err))
                raise
            except Exception as err:
                print('Other error occurred: ' + str(err))
                raise
            if 'Login expired. Please login again' in response.text:
                continue
            js = response.json()
            if 'versionId' in js:
                return js['versionId'], js['s3url']
            else:
                print('get_version_id: versionId not present in response')
                return None, None
        print('get_version_id: Tried twice. Giving up')
        return None, None

    def list_objects_at(self, type2, *args, **kwargs):
        request_bucket = kwargs['Bucket']
        request_prefix = kwargs.get('Prefix')
        tokfile = os.path.join(expanduser("~"), ".infinstor", "token")
        attempt = 0
        while attempt < 2:
            if attempt == 0:
                force = False
            else:
                force = True
            attempt = attempt + 1
            token, service = infinstor_mlflow_plugin.tokenfile.get_token(builtins.region,
                tokfile, force)
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': token
                }
            if type2:
                list_type = 2
            else:
                list_type = 1
            if not request_prefix:
                request_prefix = ''
            url = 'https://' + builtins.apiserver + '/s3metadata/' + request_prefix\
                    + '?op=list-objects&bucket=' + request_bucket + '&list-type=' + str(list_type)\
                    + '&output-format=json'
            if self.input_spec['type'] == 'infinsnap-implicit':
                url = url + '&endTime=' + str(self.input_spec['epoch_time'])
            elif self.input_spec['type'] == 'infinsnap':
                time_spec = self.input_spec['time_spec']
                url = url + '&endTime=' + str(self.infinsnap_to_epoch(time_spec))
            elif self.input_spec['type'] == 'infinslice':
                time_spec = self.input_spec['time_spec']
                st, en = self.infinslice_to_epochs(time_spec)
                url = url + '&startTime=' + str(st) + '&endTime=' + str(en)
            if ('Delimiter' in kwargs):
                url = url + '&Delimiter=' + kwargs['Delimiter']
            if ('Marker' in kwargs):
                url = url + '&Marker=' + kwargs['Marker']
            if ('ContinuationToken' in kwargs):
                url = url + '&ContinuationToken=' + kwargs['ContinuationToken']
            if ('StartAfter' in kwargs):
                url = url + '&StartAfter=' + kwargs['StartAfter']
            if ('MaxKeys' in kwargs):
                url = url + '&MaxKeys=' + str(kwargs['MaxKeys'])
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
            except HTTPError as http_err:
                print('HTTP error occurred: ' + str(http_err))
                raise
            except Exception as err:
                print('Other error occurred: ' + str(err))
                raise
            if 'Login expired. Please login again' in response.text:
                continue
            respj = response.json()
            if 'Contents' in respj:
                for one in respj['Contents']:
                    if 'LastModified' in one:
                        one['LastModified'] = datetime.fromtimestamp(one['LastModified']/1000)
            return respj
        print('list_objects_at: Tried twice. Giving up')
        return None

    def infinsnap_to_epoch(self, time_spec):
        if (len(time_spec) != 16 or not time_spec.startswith("tm")):
            raise ValueError('Incorrectly formatted infinsnap time_spec ' + time_spec)
        year = int(time_spec[2:6])
        month = int(time_spec[6:8])
        day = int(time_spec[8:10])
        hour = int(time_spec[10:12])
        minute = int(time_spec[12:14])
        second = int(time_spec[14:])
        dt = datetime(year, month, day, hour, minute, second, 0, tzinfo=timezone.utc)
        return int(dt.timestamp() * 1000.0)

    def infinslice_to_epochs(self, time_spec):
        if (len(time_spec) != 33 or not time_spec.startswith("tm")):
            raise ValueError('Incorrectly formatted infinslice time_spec ' + time_spec)
        year = int(time_spec[2:6])
        month = int(time_spec[6:8])
        day = int(time_spec[8:10])
        hour = int(time_spec[10:12])
        minute = int(time_spec[12:14])
        second = int(time_spec[14:16])
        dt1 = datetime(year, month, day, hour, minute, second, 0, tzinfo=timezone.utc)
        year = int(time_spec[19:23])
        month = int(time_spec[23:25])
        day = int(time_spec[25:27])
        hour = int(time_spec[27:29])
        minute = int(time_spec[29:31])
        second = int(time_spec[31:])
        dt2 = datetime(year, month, day, hour, minute, second, 0, tzinfo=timezone.utc)
        return int(dt1.timestamp() * 1000.0), int(dt2.timestamp() * 1000.0)

    def get_object(self, **kwargs):
        if self.input_spec['type'] == 'mlflow-run-artifacts':
            request_bucket = kwargs['Bucket']
            request_file = kwargs['Key']
            if is_declared_source(request_bucket, request_file):
                kwargs['Bucket'] = self.bucket
                if request_file:
                    kwargs['Key'] = self.prefix + "/" + request_file.lstrip('/')
                else:
                    kwargs['Key'] = self.prefix
                return self.defaultClient.get_object(**kwargs)
        elif self.input_spec['type'] == 'infinsnap' or self.input_spec['type'] == 'infinslice'\
                                            or self.input_spec['type'] == 'infinsnap-implicit':
            request_bucket = kwargs['Bucket']
            request_file = kwargs['Key']
            if request_bucket in self.input_spec['bucketlist']:
                versionId, presignedUrl = self.get_version_id(request_bucket, request_file)
                if (versionId != None):
                    kwargs['VersionId'] = versionId
                    return self.defaultClient.get_object(**kwargs)
                else:
                    raise ValueError('get_object: versionId not present. Is InfinSnap enabled?')
            else:
                return self.defaultClient.get_object(**kwargs)
        else:
            return self.defaultClient.get_object(**kwargs)

    def get_paginator(self, operation_name):
        if operation_name == 'list_objects':
            bucketlist = get_infinsnap_bucketlist()
            return ListObjectsPaginator(False, self, bucketlist)
        elif operation_name == 'list_objects_v2':
            bucketlist = get_infinsnap_bucketlist()
            return ListObjectsPaginator(True, self, bucketlist)
        else:
            return self.defaultClient.get_paginator(operation_name)

    def __getattr__(self, attr):
        if attr == 'list_objects':
            return self.list_objects
        elif attr == 'list_objects_v2':
            return self.list_objects_v2
        elif attr == 'download_file':
            return self.download_file
        elif attr == 'get_object':
            return self.get_object
        elif attr == 'get_paginator':
            return self.get_paginator
        else:
            return getattr(self.defaultClient, attr)

def get_infinsnap_bucketlist():
    tokfile = os.path.join(expanduser("~"), ".infinstor", "token")
    token, service = infinstor_mlflow_plugin.tokenfile.get_token(builtins.region, tokfile, False)
    payload = "ProductCode=9fcazc4rbiwp6ewg4xlt5c8fu"
    headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': token
            }

    url = 'https://' + builtins.apiserver + '/customerinfo'

    try:
        response = requests.post(url, data=payload+'&clientType=browser', headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return []
    except Exception as err:
        print(f'Other error occurred: {err}')
        return []
    else:
        rv = []
        rj = response.json()
        if 'InfinSnapBuckets' in rj:
            for onebucket in rj['InfinSnapBuckets']:
                rv.append(onebucket['bucketname'])
        return rv

##Decorators are specific to functions

##Decorator for boto3.Session.client
def decorate_boto3_client(client_func):
    orig_func = client_func
    @functools.wraps(client_func)
    def wrapper(*args, **kwargs):
        defaultClient = orig_func(*args, **kwargs)
        if args[1] == 's3':
            if builtins.infinstor_time_spec:
                print('infinstor: Activating time_spec=' + builtins.infinstor_time_spec)
                bucketlist = get_infinsnap_bucketlist()
                if (len(builtins.infinstor_time_spec) == 33):
                    input_spec = {
                        'type': 'infinslice',
                        'time_spec': builtins.infinstor_time_spec,
                        'bucketlist': bucketlist
                        }
                elif (len(builtins.infinstor_time_spec) == 16):
                    input_spec = {
                        'type': 'infinsnap',
                        'time_spec': builtins.infinstor_time_spec,
                        'bucketlist': bucketlist
                        }
                else:
                    raise ValueError('Incorrectly formatted builtins.infinstor_time_spec '
                            + str(builtins.infinstor_time_spec))
                return InfinBotoClient(defaultClient, input_spec, None, None)
            elif os.path.exists(INPUT_SPEC_CONFIG):
                specs, bucket, prefix = parse_input_spec(INPUT_SPEC_CONFIG)
                if specs['type'] == 'infinsnap' or specs['type'] == 'infinslice':
                    specs['bucketlist'] = get_infinsnap_bucketlist()
                    print('infinstor: Activating INPUT_SPEC_CONFIG file present. '
                            'infinsnap/slice. Buckets=' + specs['bucketlist']
                            + ', input_spec=' + str(input_spec))
                    return InfinBotoClient(defaultClient, specs, bucket, prefix)
                elif specs['type'] == 'mlflow-run-artifacts':
                    print('infinstor: Activating INPUT_SPEC_CONFIG file present. run artifacts'
                            ', input_spec=mlflow-run-artifacts')
                    return InfinBotoClient(defaultClient, specs, bucket, prefix)
            elif builtins.mlflowserver and mlflow.active_run() != None:
                if ('INFINSTOR_SNAPSHOT_TIME' in os.environ):
                    epoch_time = get_epoch_time_from_env(os.environ['INFINSTOR_SNAPSHOT_TIME'])
                else:
                    epoch_time = mlflow.active_run().info.start_time
                mlflow.log_param('infinstor_snapshot_time', epoch_time)
                bucketlist = get_infinsnap_bucketlist()
                input_spec = {
                        'type':'infinsnap-implicit',
                        'bucketlist': bucketlist,
                        'epoch_time': epoch_time
                            }
                print('infinstor: Activating implicit infinsnap/slice. Snapshot time='
                    + datetime.fromtimestamp(epoch_time/1000).strftime("%m/%d/%Y %H:%M:%S"))
                return InfinBotoClient(defaultClient, input_spec, None, None)
        return defaultClient
    return wrapper

def get_epoch_time_from_env(envvar):
    if envvar.startswith('run:/'):
        client = MlflowClient()
        run = client.get_run(envvar[5:])
        for key, value in run.data.params.items():
            if key == 'infinstor_snapshot_time':
                return int(value)
        # No infinstor_snapshot_time param. use run start time
        return run.info.start_time
    else:
        return int(envvar)

##Decorator for boto3.Session.resource
def decorate_boto3_resource(resource_func):
    orig_func = resource_func
    @functools.wraps(resource_func)
    def wrapper(*args, **kwargs):
        defaultResource = orig_func(*args, **kwargs)
        bucketlist = get_infinsnap_bucketlist()
        if bucketlist:
            return InfinBotoResource(defaultResource, bucketlist)
        else:
            return defaultResource
    return wrapper

def parse_input_spec(config):
    with open(config) as fp:
        specs = json.load(fp)
        print("Loading specs#")
        print(specs)
    if specs['type'] == 'infinsnap' or specs['type'] == 'infinslice':
        time_spec = specs['time_spec']
        bucket = specs['bucketname']
        prefix = specs['prefix']
        service = specs['service']
        if is_declared_source(bucket, prefix):
            return specs, bucket, prefix
        else:
            return specs, None, None
    elif specs['type'] == 'mlflow-run-artifacts':
        artifact_bucket, artifact_prefix = get_infin_output_location(run_id=specs['run_id'])
        if 'prefix' in specs:
            prefix = specs['prefix']
        else:
            prefix = artifact_prefix
        return specs, artifact_bucket, prefix
    return specs, None, None

def is_declared_source(bucket, prefix):
    for entry in declared_input_sources:
        if entry['bucket'] == bucket:
            return True
    return False

def declare_s3_source(bucket, prefix):
    src = {'bucket': bucket, 'prefix': prefix}
    declared_input_sources.append(src)

def get_infin_output_location(run_id=None, default_bucket=None, default_prefix="/"):
    if not run_id:
        active_run = mlflow.active_run()
        if active_run:
            run_id = mlflow.active_run().info.run_id
    if run_id:
        client = mlflow.tracking.MlflowClient()
        run = client.get_run(run_id)
        artifact_uri = run.info.artifact_uri
        parse_result = urlparse(artifact_uri)
        if (parse_result.scheme != 's3'):
            raise ValueError('Error. Do not know how to deal with artifacts in scheme ' \
                             + parse_result.scheme)
        bucketname = parse_result.netloc
        prefix = parse_result.path.lstrip('/')
        return bucketname, prefix
    else:
        return default_bucket, default_prefix

bootstrap._bootstrap_config_values_from_mlflow_rest_if_needed()
boto3.Session.client = decorate_boto3_client(boto3.Session.client)
boto3.Session.resource = decorate_boto3_resource(boto3.Session.resource)

###Intercepting Logic####
"""
1. User declares an input bucket
2. If input spec is infinsnap or infinslice
    If bucket in inputspec is same as declared input bucket
        change the endpoint url
        don't intercept any other calls --> THIS WILL CHANGE FOR PARTITIONING
    else
        don't change anything
3. If the input spec is mlflow artifact
    Don't change the endpoint url, but intercept the read/list
    if bucket in the call is same as declared input bucket
        change the bucket to the mlflow artifact uri bucket
    else
        don't do anything
"""
