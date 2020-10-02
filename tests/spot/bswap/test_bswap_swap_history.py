import responses
from binance.spot import Spot as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.error import ParameterRequiredError

mock_item = {'key_1': 'value_1', 'key_2': 'value_2'}
key = random_str()
secret = random_str()


@mock_http_response(responses.GET, '/sapi/v1/bswap/swap', mock_item, 200)
def test_bswap_swap_history():
    """ Tests the API endpoint to get swap history."""

    client = Client(key, secret)
    response = client.bswap_swap_history()
    response.should.equal(mock_item)
