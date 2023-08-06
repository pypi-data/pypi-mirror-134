# Catwalk Client

Catwalk is case aggregator for ML solutions where model query/responses can be collected for the later evaluation.   
This is client library helping to perform some common operations on the Catwalk API using python code.

## Install

Run `pip install catwalk-client`

## Sending cases

To send new open cases to the Catwalk instance you can use snippet below.

```python

    from catwalk_client import CatwalkClient
    
    # catwalk_url can be passed explicitly or can be provided in CATWALK_URL environment variable
    client = CatwalkClient(submitter_name="fatman", submitter_version="1.0.0", catwalk_url="http://localhost:9100")

    # direct call with dict to create new case
    client.send({
        "metadata": {"someint": 20},
        "query": [
            {"name": "lokalid", "value": "7386259234132", "type": "string"},
            {"name": "test3", "value": "yup", "type": "string"},
            {"name": "test2", "value": "yup", "type": "string"},
            {"name": "test1", "value": "yup", "type": "string"}
        ],
        "context": [],
        "response": [
            {
                "name": "predictions",
                "type": {
                    "name": "prediction",
                    "thresholds": [
                        {"from": 0, "to": 0.02, "label": "NO"},
                        {"from": 0.02, "to": 0.6, "label": "PERHAPS"},
                        {"from": 0.6, "to": 1, "label": "YES"}
                    ]
                },
                "value": {
                    "477110": 0.1493704617023468,
                    "477111": 0.3493704617023468,
                    "477112": 0.6493704617023468
                },
                "evaluation": [
                    {
                        "name": "choice",
                        "question": "Which branchcode is correct?",
                        "choices": ["477110", "477111", "477112"],
                        "multi": True
                    }
                ]
            }
        ]
    })

    # fluent API to create new cases
    client.new_case().add_query(
        name="some query key", value="1345243", type="str"
    ).add_query(
        name="other query key", value="1345243", type="str"
    ).add_context(
        name="photo", value="url", type="image"
    ).add_response(
        name="is_valid", value=True, type="bool", evaluation=[
            {"question": "Choose one", "name": "choice", "choices": ["YES", "NO"]}
        ]
    ).set_metadata(
        caller="esc-1"
    ).send()

```

## Exporting cases

To export cases from the Catwalk instance there is `export_cases` generator function available.

```python

    # catwalk_url can be passed explicitly or can be provided in CATWALK_URL environment variable
    client = CatwalkClient(catwalk_url="https://ikp-dev-c2.kubernilla.ersttest.dk/catwalk/api/")

    for case in client.export_cases(
            from_datetime=datetime(2022, 1, 1),
            to_datetime=datetime(2022, 2, 1),
            submitter_name="fatman",  # submitter_name is an optional filter,
            submitter_version="1.0.0",  # submitter_version is an optional filter,
            max_retries=10
    ):
        print(case)


```