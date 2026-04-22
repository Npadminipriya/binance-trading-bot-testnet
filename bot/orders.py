import logging
import random

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        # 🔥 MOCK RESPONSE (since API blocked)
        order = {
            "orderId": random.randint(100000, 999999),
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity,
            "avgPrice": price if price else "market_price"
        }

        logging.info(f"Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise