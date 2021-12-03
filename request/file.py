# coding: utf-8
import os

import requests


def upload(uri: str, query: dict, params: dict, fp: str) -> bool:
    assert os.path.exists(fp), 'file not exists. [file=%s]' % fp
    with open(fp, 'rb') as f:
        files = {'file': f}
        return requests.post(uri, files=files, params=query, data=params).status_code == 200
