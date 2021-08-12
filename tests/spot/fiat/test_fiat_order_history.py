import responses

from tests.util import random_str, timestamp
from tests.util import mock_http_response
from urllib.parse import urlencode
from binance.spot import Spot as Client

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

transactionType = 0

params = {
    "beginTime": timestamp(),
    "endTime": timestamp(),
    "page": 1,
    "rows": 100,
}


@mock_http_response(
    responses.GET,
    "/sapi/v1/fiat/orders\\?transactionType=0&" + urlencode(params),
    mock_item,
    200,
)
def test_fiat_order_history():
    """Tests the API endpoint to get fiat order history"""

    client = Client(key, secret)
    response = client.fiat_order_history(transactionType, **params)
    response.should.equal(mock_item)
