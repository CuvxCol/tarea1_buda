def calculate_spread(data, from_api_buda = "ticker"):
    try:
        if from_api_buda == 'ticker':
            ticker = data['ticker']
            iso_code = ticker['min_ask'][1]
            min_ask = float(ticker['min_ask'][0])
            max_bid = float(ticker['max_bid'][0])
            return [str(abs(max_bid - min_ask)), iso_code]
        elif from_api_buda == 'order_book':
            order_book = data['order_book']
            price_min_sell = float(order_book['asks'][0][0])
            price_max_buy = float(order_book['bids'][0][0])
            return abs(price_max_buy - price_min_sell)
        else:
            raise Exception(f"the api_buda: {from_api_buda} is not implemented")
    except Exception as ex:
        raise Exception(str(ex))