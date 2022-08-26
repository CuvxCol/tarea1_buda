from django.http import Http404

from spread.utils import buda
from spread.utils import operations

def get_spread(market_id):
    try:
        ticker = buda.get_ticker(market_id)
        spread = operations.calculate_spread(data=ticker)
        data = {
            market_id: spread
        }
        return data
    except Http404 as ex:
        raise Http404(str(ex))
    except Exception as ex:
        raise Exception(str(ex))