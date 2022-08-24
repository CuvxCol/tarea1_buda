def calculate_spread(data):
    try:
        min_sell = float(data['order_book']['asks'][0][0])
        max_buy = float(data['order_book']['bids'][0][0])
        return abs(max_buy - min_sell)
    except Exception as ex:
        return None