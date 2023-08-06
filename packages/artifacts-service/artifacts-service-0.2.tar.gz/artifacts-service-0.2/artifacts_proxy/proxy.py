from http import HTTPStatus
from typing import Optional

from common.data_types import Account
from common.proxies.base import AuthenticatorConfig
from common.proxies.base import BaseProxy
from common.proxies.base import JwtConfig


class InternalArtifactsProxy(BaseProxy):
    def __init__(self,
                 base_url: str,
                 jwt_config: JwtConfig = None,
                 authenticator_config: AuthenticatorConfig = None,
                 retry_attempts: int = None,
                 timeout: int = 10):
        super().__init__(base_url,
                         timeout,
                         retry_attempts,
                         jwt_config,
                         authenticator_config)

    def is_service_available(self) -> bool:
        response = self.get(f'{self._base_url}/is-available')

        if response.status_code != HTTPStatus.OK:
            return False

        response_json = response.json()

        return response_json['is_available']

    def create_reuse_report(self, sha256: str, analysis_id: str, account: Account):
        payload = {
            'sha256': sha256,
            'analysis_id': analysis_id
        }

        response = self.post(f'{self._base_url}/reuse-report', json=payload, account=account)
        response.raise_for_status()

        return response.json()['result']

    def get_reuse_report(self, analysis_id: str, account: Account) -> Optional[dict]:
        response = self.get(f'{self._base_url}/reuse-report/{analysis_id}', account=account)

        response.raise_for_status()

        return response.json()

    def index_file_artifacts(self,
                             sha256: str,
                             index_family_id: str,
                             index_software_type: str,
                             account: Account):
        payload = {
            'index_family_id': index_family_id,
            'index_software_type': index_software_type
        }

        response = self.post(f'{self._base_url}/artifacts/{sha256}/index', json=payload, account=account)
        response.raise_for_status()

        return response.json()['result']
