import logging
from datetime import datetime

from catwalk_client.catwalk_client.client import CatwalkClient

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # catwalk_url can be passed explicitly or can be provided in CATWALK_URL environment variable
    client = CatwalkClient(submitter_name="fatman", submitter_version="1.0.0",
                           catwalk_url="http://localhost:9100/")

    cases = []
    for case in client.export_cases(datetime(2022, 1, 1), datetime(2022, 2, 1), submitter_name="fatman"):
        cases.append(case)

    print(len(cases))