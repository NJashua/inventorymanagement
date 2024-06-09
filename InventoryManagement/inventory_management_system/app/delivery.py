import requests

class DeliveryService:
    def __init__(self):
        self.orders = []

    def create_order(self, order_id, product_name, number_shipped, order_date, origin, destination):
        order = {
            'order_id': order_id,
            'product_name': product_name,
            'number_shipped': number_shipped,
            'order_date': order_date,
            'origin': origin,
            'destination': destination,
            'status': 'Created'
        }
        self.orders.append(order)
        return order

    def find_shortest_route(self, origin, destination):
        try:
            response = requests.get(f'https://api.mapbox.com/directions/v5/mapbox/driving/{origin};{destination}?access_token=pk.eyJ1Ijoibml0aGluamFzaHVhIiwiYSI6ImNsd3h0MnFhdTE2OXIyenIxYmR3OTgxdXEifQ.gwR13HViM7k_Gba6RY9X4Q')
            data = response.json()
            routes = data['routes']
            if routes:
                shortest_route = min(routes, key=lambda route: route['duration'])
                return {
                    'distance': shortest_route['distance'],
                    'duration': shortest_route['duration'],
                    'geometry': shortest_route['geometry']
                }
            else:
                return {'error': 'No routes found'}
        except Exception as e:
            return {'error': str(e)}

    def track_order(self, order_id):
        for order in self.orders:
            if order['order_id'] == order_id:
                return order
        return {'error': 'Order not found'}

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = status
                return order
        return {'error': 'Order not found'}

delivery_service = DeliveryService()
