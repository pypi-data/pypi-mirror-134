import json
import logging
import os
from datetime import datetime, timedelta
from urllib.parse import urlencode

import requests
from .case_builder import CaseBuilder
from catwalk_common import CommonCaseFormat, OpenCase

logger = logging.getLogger("catwalk_client")


def _hour_range(start, end):
    while start < end:
        yield start
        start += timedelta(hours=1)


class CatwalkClient:
    submitter_name: str
    submitter_version: str
    catwalk_url: str

    def __init__(self, submitter_name: str, submitter_version: str, catwalk_url: str = None):
        self.submitter_name = submitter_name
        self.submitter_version = submitter_version
        self.catwalk_url = catwalk_url or os.environ.get("CATWALK_URL")

    def new_case(self) -> CaseBuilder:
        return CaseBuilder(client=self)

    def _get_url(self, path: str):
        return self.catwalk_url.rstrip('/') + path

    def send(self, case: dict):
        case = CommonCaseFormat(
            submitter={"name": self.submitter_name, "version": self.submitter_version},
            **case
        )

        response = requests.post(self._get_url("/api/cases/collect"), data=case.json())

        if response.ok:
            data = json.loads(response.text)
            logger.info(f"Collected catwalk case: {data['id']}")

    def export_cases(self, from_datetime: datetime, to_datetime: datetime,
                     submitter_name: str = None, submitter_version: str = None):

        filters = {"submitter_name": submitter_name, "submitter_version": submitter_version}
        filters = {k: v for k, v in filters.items() if v is not None}

        for date in _hour_range(from_datetime, to_datetime):

            path = f"/api/cases/export/{date.year}/{date.month}/{date.day}/{date.hour}"

            if filters:
                path += f'?{urlencode(filters)}'

            next_token = self._get_url(path)

            while next_token:
                response = requests.get(next_token)
                next_token = None

                if not response.ok:
                    raise Exception(response.text)

                data = json.loads(response.text)
                for item in data['items']:
                    yield OpenCase.parse_obj(item)

                if data['next_part'] and data['items']:
                    next_token = data['next_part']
