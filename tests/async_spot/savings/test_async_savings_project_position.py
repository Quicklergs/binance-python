import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import mock_async_http_response
from tests.util import random_str

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v1/lending/project/position/list", mock_item, 200
)
async def test_savings_fixed_activity_project():
    """Tests the API endpoint to purchase Fixed/Activity project position"""

    client = Client(key, secret)
    response = await client.savings_project_position()
    response.should.equal(mock_item)
