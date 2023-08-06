import logging
from datetime import datetime

from catwalk_client.catwalk_client import CatwalkClient

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    client = CatwalkClient(submitter_name="", submitter_version="",
                           catwalk_url="https://ikp-dev-c2.kubernilla.ersttest.dk/catwalk/api/")
    for case in client.export_cases(from_datetime=datetime(2022, 1, 12), to_datetime=datetime(2022, 1, 13)):
        print(case)
