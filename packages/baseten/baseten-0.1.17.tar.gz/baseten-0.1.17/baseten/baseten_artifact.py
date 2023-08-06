import logging
import tarfile
import tempfile

import requests
from colorama import Fore
from tqdm import tqdm

from baseten import baseten_deployed_model
from baseten.common import api

logger = logging.getLogger(__name__)


class BasetenArtifact:
    """An artifact stored on the BaseTen backend"""
    def __init__(
        self,
        artifact_id: str,
        name: str = None,
        description: str = None,
    ):
        if not artifact_id:
            raise ValueError("Must provide the artifact's id")

        self._id = artifact_id
        self._name = name
        self._description = description

    def __repr__(self):
        attr_info = [f'id={self._id}']
        if self._name:
            attr_info.append(f'name={self._name}')
        if self._description:
            attr_info.append(f'description={self._description}')

        info_str = '\n  '.join(attr_info)

        return f'BasetenArtifact<\n  {info_str}\n>'

    def create_link(self, model_id: str = None, model_version_id: str = None):
        if not model_id and not model_version_id:
            raise ValueError('Either model_id or model_version_id must be provided.')
        if model_id and model_version_id:
            raise ValueError('Must provide either model_id or model_version_id; not both.')
        resp = api.create_artifact_link(self._id, model_id=model_id, model_version_id=model_version_id)
        logger.info('⛓ Successfully linked artifact ⛓')
        return resp

    def links(self):
        links = api.artifact_links(self._id)
        return [
            baseten_deployed_model.BasetenDeployedModel(model_version_id=model_version_id)
            for model_version_id in links['model_version_ids']
        ] + [
            baseten_deployed_model.BasetenDeployedModel(model_id=model_id)
            for model_id in links['model_ids']
        ]

    def url(self):
        # todo(alex): worth it to introduce a library to cache a TTL here?
        return api.artifact_url(self._id)

    def download(self, target_directory):
        artifact_response = requests.get(self.url(), stream=True)
        logger.info('📁 Downloading artifact archive from BaseTen 📁')
        block_size = 1024  # 1 Kibibyte
        total_size_in_bytes = int(artifact_response.headers.get('content-length', 0))
        progress_bar = tqdm(
            total=total_size_in_bytes,
            unit='iB',
            unit_scale=True,
            bar_format="Download Progress: "
                       "{percentage:3.0f}%% |%s{bar:100}%s| {n_fmt}/{total_fmt}" % (Fore.BLUE, Fore.RESET)
        )

        temp_tgz = tempfile.NamedTemporaryFile(mode='w+b')
        for content in artifact_response.iter_content(block_size):
            temp_tgz.write(content)
            progress_bar.update(len(content))
        temp_tgz.file.seek(0)
        progress_bar.close()

        logger.info('🔮 Download successful!🔮')

        with tarfile.open(temp_tgz.name, 'r') as tar:
            tar.extractall(target_directory)
        logger.info(f'📁 Successfully extracted artifact to {target_directory} 📁')
