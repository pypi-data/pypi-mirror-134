import os
from typing import Any, Dict, List, Tuple

import codefast as cf
import pydantic

from dofast.web.celeryapi import produce_app


class FileDownloader(object):
    def download(self, url: str, name: str) -> bool:
        cf.info(f'Downloading {url}')
        cf.net.download(url, name)
        return True


class TaskDescriptor(pydantic.BaseModel):
    url: str
    name: str

    def __repr__(self) -> str:
        return str(self.dict())


class PcloudFileUploader(object):
    def __init__(self, pcloud_cli: str = '') -> None:
        # pcloud cli is binary file path
        self.cli = pcloud_cli
        if not self.cli:
            candidates = [
                '/usr/local/bin/uix', '/root/uix', '~/.cargo/bin/uix',
                '/usr/bin/uix'
            ]
            for c in candidates:
                full = os.path.expanduser(c)
                if cf.io.exists(full):
                    cf.info(f'Found {full}')
                    self.cli = full
                    break

    def upload(self, fpath: str, remove_after_upload: bool = True) -> bool:
        # upload file to pcloud vps directory
        cf.info(f'Uploading {fpath} to pcloud')
        resp = cf.shell(f'{self.cli} -pc -vps {fpath}')
        cf.info('{}, {}'.format(self.__class__.__name__, resp))

        if remove_after_upload:
            cf.info("Removing {}".format(fpath))
            cf.io.rm(fpath)

        return True

    def parse_url(self, text: str) -> TaskDescriptor:
        # parse pcloud url
        cf.info(f'Parsing {text}')
        placeholder = 'TEXT'
        _, url, name = ' '.join([text, placeholder]).split(' ')[:3]
        if name == placeholder:
            name = cf.io.basename(url)
        return TaskDescriptor(url=url, name=name)


app = produce_app('files')


@app.task
def cloudsync(text: str):
    pc = PcloudFileUploader()
    td = pc.parse_url(text)
    cf.info('Task descriptor {}'.format(repr(td)))

    downloader = FileDownloader()
    downloader.download(td.url, td.name)
    cf.info('Downloaded {}'.format(td.name))

    pc.upload(td.name, remove_after_upload=True)
    cf.info('Uploaded {}'.format(td.name))
    return True
