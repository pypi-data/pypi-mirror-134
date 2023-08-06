#!/usr/bin/env python
# -*- coding utf-8 -*-

import _io
import os
import time
import json
import requests
import urllib.parse
import tempfile
import shutil
import mlflow
import base64
import string
import numpy as np
from chassisml import __version__
from ._utils import zipdir,fix_dependencies,write_modzy_yaml,NumpyEncoder

###########################################
MODEL_ZIP_NAME = 'model.zip'
MODZY_YAML_NAME = 'model.yaml'
CHASSIS_TMP_DIRNAME = 'chassis_tmp'

routes = {
    'build': '/build',
    'job': '/job',
    'test': '/test'
}

###########################################

class ChassisModel(mlflow.pyfunc.PythonModel):
    """The Chassis Model object.

    This class inherits from mlflow.pyfunc.PythonModel and adds Chassis functionality.

    Attributes:
        predict (function): MLflow pyfunc compatible predict function. 
            Will wrap user-provided function which takes two arguments: model_input (bytes) and model_context (dict).
        chassis_build_url (str): The build url for the Chassis API.
    """

    def __init__(self,model_context,process_fn,batch_process_fn,batch_size,chassis_base_url):

        if process_fn and batch_process_fn:
            if not batch_size:
                raise ValueError("Both batch_process_fn and batch_size must be provided for batch support.")
            self.predict = self._gen_predict_method(process_fn,model_context)
            self.batch_predict = self._gen_predict_method(batch_process_fn,model_context,batch=True)
            self.batch_input = True
            self.batch_size = batch_size
        elif process_fn and not batch_process_fn:
            self.predict = self._gen_predict_method(process_fn,model_context)
            self.batch_input = False
            self.batch_size = None
        elif batch_process_fn and not process_fn:
            if not batch_size:
                raise ValueError("Both batch_process_fn and batch_size must be provided for batch support.")
            self.predict = self._gen_predict_method(batch_process_fn,model_context,batch_to_single=True)
            self.batch_predict = self._gen_predict_method(batch_process_fn,model_context,batch=True)
            self.batch_input = True
            self.batch_size = batch_size
        else:
            raise ValueError("At least one of process_fn or batch_process_fn must be provided.")

        self.chassis_build_url = urllib.parse.urljoin(chassis_base_url, routes['build'])
        self.chassis_test_url = urllib.parse.urljoin(chassis_base_url, routes['test'])

    def _gen_predict_method(self,process_fn,model_context,batch=False,batch_to_single=False):
        def predict(_,model_input):
            if batch_to_single:
                output = process_fn([model_input],model_context)[0]
            else:
                output = process_fn(model_input,model_context)
            if batch:
                return [json.dumps(out,separators=(",", ":"),cls=NumpyEncoder).encode() for out in output]
            else:
                return json.dumps(output,separators=(",", ":"),cls=NumpyEncoder).encode()
        return predict

    def test(self,test_input):
        if isinstance(test_input,_io.BufferedReader):
            result = self.predict(None,test_input.read())
        elif isinstance(test_input,bytes):
            result = self.predict(None,test_input)
        elif isinstance(test_input,str):
            if os.path.exists(test_input):
                result = self.predict(None,open(test_input,'rb').read())
            else:
                result = self.predict(None,bytes(test_input,encoding='utf8'))
        else:
            print("Invalid input. Must be buffered reader, bytes, valid filepath, or text input.")
            return False
        return result

    def test_batch(self,test_input):
        if not self.batch_input:
            raise NotImplementedError("Batch inference not implemented.")

        if hasattr(self,'batch_predict'):
            batch_method = self.batch_predict
        else:
            batch_method = self.predict

        if isinstance(test_input,_io.BufferedReader):
            results = batch_method(None,[test_input.read() for _ in range(self.batch_size)])
        elif isinstance(test_input,bytes):
            results = batch_method(None,[test_input for _ in range(self.batch_size)])
        elif isinstance(test_input,str):
            if os.path.exists(test_input):
                results = batch_method(None,[open(test_input,'rb').read() for _ in range(self.batch_size)])
            else:
                results = batch_method(None,[bytes(test_input,encoding='utf8') for _ in range(self.batch_size)])
        else:
            print("Invalid input. Must be buffered reader, bytes, valid filepath, or text input.")
            return False
        return results

    def test_env(self,test_input_path,conda_env=None,fix_env=True):
        model_directory = os.path.join(tempfile.mkdtemp(),CHASSIS_TMP_DIRNAME)
        mlflow.pyfunc.save_model(path=model_directory, python_model=self, conda_env=conda_env, 
                                extra_pip_requirements = None if conda_env else ["chassisml=={}".format(__version__)])

        if fix_env:
            fix_dependencies(model_directory)

        # Compress all files in model directory to send them as a zip.
        tmppath = tempfile.mkdtemp()
        zipdir(model_directory,tmppath,MODEL_ZIP_NAME)
        
        with open('{}/{}'.format(tmppath,MODEL_ZIP_NAME),'rb') as model_f, \
                open(test_input_path,'rb') as test_input_f:
            files = [
                ('sample_input', test_input_f),
                ('model', model_f)
            ]

            print('Starting test job... ', end='', flush=True)
            res = requests.post(self.chassis_test_url, files=files)
            res.raise_for_status()
        print('Ok!')

        shutil.rmtree(tmppath)
        shutil.rmtree(model_directory)

        return res.json()

    def save(self,path,conda_env=None,overwrite=False):
        if overwrite and os.path.exists(path):
            shutil.rmtree(path)
        mlflow.pyfunc.save_model(path=path, python_model=self, conda_env=conda_env)
        print("Chassis model saved.")

    def publish(self,model_name,model_version,registry_user,registry_pass,
                conda_env=None,fix_env=True,gpu=False,modzy_sample_input_path=None,
                modzy_api_key=None):

        if (modzy_sample_input_path or modzy_api_key) and not \
            (modzy_sample_input_path and modzy_api_key):
            raise ValueError('"modzy_sample_input_path", and "modzy_api_key" must both be provided to publish to Modzy.')

        try:
            model_directory = os.path.join(tempfile.mkdtemp(),CHASSIS_TMP_DIRNAME)
            mlflow.pyfunc.save_model(path=model_directory, python_model=self, conda_env=conda_env, 
                                    extra_pip_requirements = None if conda_env else ["chassisml=={}".format(__version__)])

            if fix_env:
                fix_dependencies(model_directory)

            # Compress all files in model directory to send them as a zip.
            tmppath = tempfile.mkdtemp()
            zipdir(model_directory,tmppath,MODEL_ZIP_NAME)
            
            image_name = "-".join(model_name.translate(str.maketrans('', '', string.punctuation)).lower().split())
            image_data = {
                'name': "{}/{}".format(registry_user,"{}:{}".format(image_name,model_version)),
                'model_name': model_name,
                'model_path': tmppath,
                'registry_auth': base64.b64encode("{}:{}".format(registry_user,registry_pass).encode("utf-8")).decode("utf-8"),
                'publish': True,
                'gpu': gpu
            }

            if modzy_sample_input_path and modzy_api_key:
                modzy_metadata_path = os.path.join(tmppath,MODZY_YAML_NAME)
                modzy_data = {
                    'metadata_path': modzy_metadata_path,
                    'sample_input_path': modzy_sample_input_path,
                    'deploy': True,
                    'api_key': modzy_api_key
                }
                write_modzy_yaml(model_name,model_version,modzy_metadata_path,batch_size=self.batch_size,gpu=gpu)
            else:
                modzy_data = {}

            with open('{}/{}'.format(tmppath,MODEL_ZIP_NAME),'rb') as f:
                files = [
                    ('image_data', json.dumps(image_data)),
                    ('modzy_data', json.dumps(modzy_data)),
                    ('model', f)
                ]
                file_pointers = []
                for key, file_key in [('metadata_path', 'modzy_metadata_data'),
                                ('sample_input_path', 'modzy_sample_input_data')]:
                    value = modzy_data.get(key)
                    if value:
                        fp = open(value, 'rb')
                        file_pointers.append(fp)  
                        files.append((file_key, fp))

                print('Starting build job... ', end='', flush=True)
                res = requests.post(self.chassis_build_url, files=files)
                res.raise_for_status()
            print('Ok!')

            for fp in file_pointers:
                fp.close()

            shutil.rmtree(tmppath)
            shutil.rmtree(model_directory)

            return res.json()
        
        except Exception as e:
            print(e)
            if os.path.exists(tmppath):
                shutil.rmtree(tmppath)
            if os.path.exists(model_directory):
                shutil.rmtree(model_directory)
            return False

###########################################

class ChassisClient:
    """The Chassis Client object.

    This class is used to interact with the Kaniko service.

    Attributes:
        base_url (str): The base url for the API.
    """

    def __init__(self,base_url='http://localhost:5000'):
        self.base_url = base_url

    def get_job_status(self, job_id):
        route = f'{urllib.parse.urljoin(self.base_url, routes["job"])}/{job_id}'
        res = requests.get(route)
        data = res.json()
        return data

    def block_until_complete(self,job_id,timeout=1800,poll_interval=5):
        endby = time.time() + timeout if (timeout is not None) else None
        while True:
            status = self.get_job_status(job_id)
            if status['status']['succeeded'] or status['status']['failed']:
                return status
            if (endby is not None) and (time.time() > endby - poll_interval):
                print('Timed out before completion.')
                return False
            time.sleep(poll_interval)

    def download_tar(self, job_id, output_filename):
        url = f'{urllib.parse.urljoin(self.base_url, routes["job"])}/{job_id}/download-tar'
        r = requests.get(url)

        if r.status_code == 200:
            with open(output_filename, 'wb') as f:
                f.write(r.content)
        else:
            print(f'Error download tar: {r.text}')

    def create_model(self,context,process_fn=None,batch_process_fn=None,batch_size=None):
        if not (process_fn or batch_process_fn):
            raise ValueError("At least one of process_fn or batch_process_fn must be provided.")

        if (batch_process_fn and not batch_size) or (batch_size and not batch_process_fn):
            raise ValueError("Both batch_process_fn and batch_size must be provided for batch support.")

        return ChassisModel(context,process_fn,batch_process_fn,batch_size,self.base_url)
