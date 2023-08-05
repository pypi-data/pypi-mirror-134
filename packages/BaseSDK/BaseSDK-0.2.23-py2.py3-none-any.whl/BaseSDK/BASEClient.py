import requests
import logging
import os

from BaseSDK import Utils
from BaseSDK.Configuration import *
from BaseSDK.ClientException import ResourceException, AuthException

from multiprocessing import Pool

import json
import hashlib


url_dict = {
    'get_dataset':'/sdk/datasets/{dataset_id}/files',
    'get_sampleset': '/sdk/samplesets/{sampleset_id}/files',
    'get_dataset_id_from_sampleset_id':'/sdk/datasetId/samplesetId/{sampleset_id}',
    'get_labels': '/sdk/labels',
    'get_categories': '/sdk/category',
    'get_model_upload_url': '/sdk/models/{model_name}/upload',
    'get_log_upload_url': '/sdk/log/upload',
    'get_pretrain': '/model-store/pretrain-models/{model_name}',
    'get_model': '/sdk/models/{model_id}',
    'get_callback_upload_model':'/sdk/models/upload',
    'get_calibration':'/sdk/calibrations'
}


class BASEClient(metaclass=Singleton):
    def __init__(self, apiKey=None, context='dev'):
        self.logger = logging.getLogger('BASEClient')
        self.config = Configuration(context)
        self.apiKey = apiKey

    def get_dataset_files(self, dataset_id, sensor='all'):
        """

        Args:
            dataset_id: id of the dataset
            sensor: the sensor type of the files to download, the default is 'all'

        Returns:
            files: file list
        """
        payload = {
            'sensor': sensor
        }
        url = self.config.url + url_dict.get('get_dataset').format(dataset_id=dataset_id)
        try:
            dataset_resp = requests.get(url=url,
                                        params=payload,
                                        headers={'apiKey': self.apiKey})

            if dataset_resp.status_code == 200:
                content = dataset_resp.json()
                if content['code'] == 200:
                    return content['data']
                else:
                    raise ResourceException(content['msg'])
            else:
                raise AuthException(dataset_resp.reason)
        except Exception as e:
            raise e

    def download_dataset(self, dataset_id, save_path, sensor='all'):
        """

        Args:
            dataset_id: id of the dataset
            save_path: local path to save the files
            sensor: the sensor type of the files to download, the default is 'all'

        Returns:
            True if the dataset files downloaded successfully.
        """
        Utils.makedir(save_path)
        sensors = self.get_dataset_files(dataset_id, sensor)
        if not sensors:
            self.logger.error("No sensors found in the dataset.")
            return False

        for sensor, files in sensors.items():
            save_path_ = os.path.join(save_path, sensor)
            Utils.makedir(save_path_)
            data = [[os.path.join(save_path_, _file['filename']), _file['url']] for _file in files]
            with Pool(8) as pool:
                pool.map(Utils.download_binary, data)

        return True

    def get_sampleset_files(self, sampleset_id, sensor='all'):
        """

        Args:
            sampleset_id: id of the sampleset to download
            batch: the batch name of the sampleset, the default is 'batch-0'
            sensor: the sensor type of the files to download, the default is 'all'

        Returns:
            files: file list
        """
        payload = {
            'sensor': sensor
        }
        url = self.config.url + url_dict.get('get_sampleset').format(sampleset_id=sampleset_id)
        try:
            sampleset_resp = requests.get(url=url,
                                        params=payload,
                                        headers={'apiKey': self.apiKey})

            if sampleset_resp.status_code == 200:
                content = sampleset_resp.json()
                if content['code'] == 200:
                    return content['data']
                else:
                    raise ResourceException(content['msg'])
            else:
                raise ResourceException(sampleset_resp.reason)
        except Exception as e:
            raise e

    def get_dataset_id(self, sampleset_id):
        """
            Args:
                sampleset_id: id of the sampleset to download

            Returns:
                dataset_id corresponding to the sampleset_id.
        """
        url = self.config.url + url_dict.get('get_dataset_id_from_sampleset_id').format(sampleset_id=sampleset_id)
        try:
            resp = requests.get(url=url,headers={'apiKey':self.apiKey})
            if resp.status_code == 200:
                content = resp.json()
                if content['code'] == 200:
                    return content['data']
                else:
                    raise ResourceException(content)
            else:
                raise ResourceException(resp.reason)
        except Exception as e:
            raise e

    def download_sampleset(self, sampleset_id, save_path, sensor='all'):
        """

        Args:
            sampleset_id: id of the sampleset to download
            save_path: local path to save the files
            batch: the batch name of the sampleset, the default is 'batch-0'
            sensor: the sensor type of the files to download, the default is 'all'

        Returns:
            True if the sampleset files downloaded successfully.
        """
        Utils.makedir(save_path)
        sensors = self.get_sampleset_files(sampleset_id, sensor)
        if not sensors:
            self.logger.error("No sensors found in the sampleset.")
            return False

        for sensor, files in sensors.items():
            save_path_ = os.path.join(save_path, sensor)
            Utils.makedir(save_path_)
            data = [[os.path.join(save_path_, _file['filename']), _file['url']] for _file in files]
            with Pool(8) as pool:
                pool.map(Utils.download_binary, data)

        return True

    def get_label_files(self, sampleset_id, sensor='all'):

        payload = {
            'sensor': sensor
        }
        url = self.config.url + url_dict.get('get_sampleset').format(sampleset_id=sampleset_id)
        try:
            label_resp = requests.get(url=url,
                                        params=payload,
                                        headers={'apiKey': self.apiKey})

            if label_resp.status_code == 200:
                content = label_resp.json()
                if content['code'] == 200:
                    return content['data']
                else:
                    raise ResourceException(content['msg'])
            else:
                raise ResourceException(label_resp.reason)
        except Exception as e:
            raise e


    def request_save_label(self, args):
        sampleset_id, sensor, filename, save_path = args
        payload = {
            'sampleSetId': sampleset_id,
            'sensor': sensor,
            'fileName': filename
        }
        try:
            label_resp = requests.get(url=self.config.url + url_dict.get('get_labels'),
                                        params=payload,
                                        headers={'apiKey': self.apiKey}).json()
            label_info = label_resp['data']
            json_file_name = os.path.join(save_path, os.path.splitext(filename)[0] + '.json')
            with open(json_file_name, 'w') as handle:
                json.dump(label_info, handle)
        except Exception as e:
            raise e
            
            
    def download_labels(self, sampleset_id, save_path, sensor='all', ):
        """

        Args:
            sampleset_id: id of the sampleset to download
            save_path: local path to save the files
            batch: the batch name of the sampleset, the default is 'batch-0'
            sensor: the sensor type of the files to download, the default is 'all'

        Returns:
             True if the sampleset files downloaded successfully.
        """
        Utils.makedir(save_path)
        sensors = self.get_label_files(sampleset_id, sensor)
        if not sensors:
            self.logger.error("No sensors found in the sampleset.")
            return False
        for sensor, files in sensors.items():
            save_path_ = os.path.join(save_path, sensor)
            Utils.makedir(save_path_)
            args = [[sampleset_id, sensor, file['filename'], save_path_] for file in files]
            with Pool(8) as pool:
                pool.map(self.request_save_label, args)
        return True

    def get_categories(self, dataset_id):
        """
        Args:
            dataset_id: id of the dataset

        Returns:

        """
        try:
            payload = {
                'datasetId': dataset_id,
            }
            category_resp = requests.get(
                url=self.config.url + url_dict.get('get_categories'),
                params=payload,
                headers={'apiKey': self.apiKey}).json()
            if category_resp['code'] == 200:
                _categories = category_resp['data']['categories']
                return [(cate['name'],cate['featureType']) for cate in _categories]
            else:
                raise ResourceException(category_resp['msg'])
        except Exception as e:
            raise e

    def upload_model(self, task_id, model_name, model_file):
        """

        Args:
            task_id: unique id of the task
            model_name: model unique name
            model_file: file path of the serializers model to upload

        Returns:
            True if upload successfully.
        """

        try:
            md5 = self.calculate_md5(model_file)
            payload = {
                "taskId":task_id,
                "md5":md5
            }
            upload_resp = requests.get(url=self.config.url + url_dict.get('get_model_upload_url').format(model_name=model_name),
                                       params=payload,
                                       headers={'apiKey': self.apiKey}).json()

            if upload_resp['code'] != 200:
                self.logger.warning(upload_resp['msg'])
                return

            url = upload_resp['data']['key']

            with open(model_file, 'rb') as file_to_upload:
                upload_response = requests.put(url=url, data=file_to_upload)

            self.logger.info(upload_response)

            return True

        except Exception as e:
            raise e

    def upload_log(self, task_id, model_name, log_file):
        """

        Args:
            task_id: unique id of the task
            model_name: model unique name
            log_file: file path of log to upload

        Returns:
            True if upload successfully.
        """

        try:
            payload = {
                "taskId":task_id,
                "modelName":model_name
            }
            upload_resp = requests.get(url=self.config.url + url_dict.get('get_log_upload_url'),
                                       params=payload,
                                       headers={'apiKey': self.apiKey}).json()

            if upload_resp['code'] != 200:
                self.logger.warning(upload_resp['msg'])
                self.logger.warning('request for uploading log file failed')
                return

            url = upload_resp['data']['key']

            with open(log_file, 'rb') as file_to_upload:
                upload_response = requests.put(url=url, data=file_to_upload)

            self.logger.info(upload_response)

            return True

        except Exception as e:
            raise e

    def upload_label(self, label):
        """

        Args:
            label: the result of the model inference in json format

        Returns:
            True if upload successfully.
        """
        try:
            upload_resp = requests.post(
                url=self.config.url + url_dict.get('get_labels'),
                data=label,
                headers={'apiKey': self.apiKey,'Content-Type':'application/json'}).json()

            if upload_resp['code'] != 200:
                self.logger.warning(upload_resp['msg'])
                return

            self.logger.info(upload_resp['code'])
            return True

        except Exception as e:
            raise e


    def download_pretrain(self, model_name, save_path):
        """
        Args:
            model_name: model unique name
            save_path: local path to save the files

        Returns:
            True if download successfully.
        """
        pass

    def get_model(self, model_id):
        """
        Args:
            task_id: the unique id of the task

        Returns:
            model information.
        """
        try:
            header = {'apiKey': self.apiKey}
            model_resp = requests.get(url=self.config.url + url_dict.get("get_model").format(model_id=model_id),headers=header).json()
            if model_resp['code'] != 200:
                self.logger.warning(model_resp['msg'])
                raise ResourceException(model_resp['msg'])

            return model_resp['data']

        except Exception as e:
            raise e


    def download_model(self, model_id, save_path):
        """
        Args:
            model_id: the unique id of the model
            model_name: model unique name
            save_path: local path to save the files

        Returns:
            True if download successfully.
        """
        try:
            Utils.makedir(save_path)
            model_resp = self.get_model(model_id)
            model_url = model_resp['modelUrl']
            md5 = model_resp['md5']
            save_path =os.path.join(save_path, "{}.pth".format('pretrain'))
            data = (save_path, model_url)
            Utils.download_binary(data)
            md5_ = self.calculate_md5(save_path)
            if md5 == md5_:
                return True
            else:
                raise Exception('the md5 of downloaded file is not match that in database!!!')
        except Exception as e:
            raise e

    def callback_upload_model(self, task_id, upload_success=False):
        try:
            if upload_success:
                payload = {
                    'taskId':task_id,
                    'status':1
                }
            else:
                payload = {
                    "taskId":task_id,
                    "status":0
                }
            payload = json.dumps(payload)
            resp = requests.post(url=self.config.url + url_dict.get('get_callback_upload_model'),
                                 data=payload, headers={'apiKey': self.apiKey,'Content-Type':'application/json'}).json()
            if resp['code'] != 200:
                self.logger.warning(resp['msg'])
                return

            self.logger.info(resp['code'])
            return True
        except Exception as e:
            raise e

    def calculate_md5(self, file_path):
        try:
            md5_hash = hashlib.md5()
            with open(file_path,'rb') as f:
                for byte_block in iter(lambda: f.read(4096),b""):
                    md5_hash.update(byte_block)
            return md5_hash.hexdigest()
        except Exception as e:
            raise e

    def download_calibrations(self, dataset_id, save_path):
        Utils.makedir(save_path)
        payload = {
            'datasetId': dataset_id
        }
        url = self.config.url + url_dict.get('get_calibration')
        resp = requests.get(url=url,params=payload,headers={'apiKey': self.apiKey})
        if resp.status_code == 200:
            content = resp.json()
            if content['code'] == 200:
                try:
                    data = content['data']
                    for key in data.keys():
                        json_name = key + '.json'
                        json_save_path = os.path.join(save_path,json_name)
                        with open(json_save_path, 'w') as handle:
                            json.dump(data[key],handle)
                    return True
                except Exception as e:
                    raise e
            else:
                return False
        else:
            raise ResourceException(resp.reason)

        return True

if __name__ == '__main__':

    token = ""
    sampleset_id = ""
    c = BASEClient(token, "dev")  # "prod"

