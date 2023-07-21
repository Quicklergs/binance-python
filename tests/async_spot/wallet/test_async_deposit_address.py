import pytest
from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_deposit_address_without_coin():
    """Tests the API endpoint to get deposit address without coin"""

    client = Client(key, secret)
    try:
        response = await client.deposit_address("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/capital/deposit/address\\?coin=BNB", mock_item, 200
)
async def test_deposit_address():
    """Tests the API endpoint to get deposit address"""

    client = Client(key, secret)
    response = await client.deposit_address(coin="BNB")
    response.should.equal(mock_item)
