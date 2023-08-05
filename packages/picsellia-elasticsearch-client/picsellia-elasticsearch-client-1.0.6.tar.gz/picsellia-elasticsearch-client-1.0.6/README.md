# Picsellia Elasticsearch Client

Picsellia Elasticsearch Client is a Python library that wraps Elasticsearch Python Client in order to push Picsellia metrics.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install picsellia-elasticsearch-client
```

## Usage

```python
from picsellia_elasticsearch_client.client import PicselliaELKClient

client = PicselliaELKClient(host="localhost", port=443)

metric = PicselliaMetric(service="service", data={ "hello" : "world" })

client.push(metric)

error = PicselliaError(service="service", exception=KeyError('key'))

client.push(error)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)