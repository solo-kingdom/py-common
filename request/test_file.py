from unittest import TestCase

from common.request.file import upload


class Test(TestCase):
    def test_upload(self):
        res = upload('http://127.0.0.1:8088/api/v1/package', {
            'space': 'global',
            'product': 'test',
            'version': '0.0.1'
        }, {}, '/Users/wii/.vimrc')
        assert res.status_code == 200
