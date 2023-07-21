import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from urllib.parse import urlencode
from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()

params = {
    "asset": "BNB",
    "startTime": "1590969041003",
    "endTime": "1590969041003",
    "size": 10,
    "recvWindow": 1000,
}


@pytest.mark.asyncio
@mock_async_http_response(
    "GET",
    "/sapi/v1/margin/interestHistory\\?" + urlencode(params),
    mock_item,
    200,
)
async def test_margin_interest_history():
    """Tests the API endpoint to query margin interest history"""

    client = Client(key, secret)
    response = await client.margin_interest_history(**params)
    response.should.equal(mock_item)
