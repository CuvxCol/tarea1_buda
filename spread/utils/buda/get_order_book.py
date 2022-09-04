from spread.environment.APIs import budaURLs

from spread.utils.request import generate_request
from django.http import Http404

def get_order_book(market_id):
    response = generate_request(budaURLs.BUDA_MARKET_API_URL + "/" + market_id + "/order_book", 'GET')
    if(response.status_code == 200):
        return response.json()
    elif(response.status_code == 404):
        raise Http404(response.reason)
    else:
        raise Exception("httpCode " + response.status_code + " - " + response.reason)