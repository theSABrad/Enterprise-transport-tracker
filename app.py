from flask import Flask, render_template, jsonify
import sys

app = Flask(__name__)

# Telemetry data representing live school bus routes
MOCK_BUS_ROUTES = [
    {"route_id": "ROUTE-A1", "driver": "Sarah Jenkins", "status": "In Transit", "capacity": "24/30", "next_stop": "Primary Gate"},
    {"route_id": "ROUTE-B4", "driver": "Michael Chang", "status": "Delayed", "capacity": "18/35", "next_stop": "Oxford Intersection"},
    {"route_id": "ROUTE-C2", "driver": "David Nkosi", "status": "Completed", "capacity": "0/28", "next_stop": "Main Terminal"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/transport/status', methods=['GET'])
def get_transport_status():
    return jsonify({
        "system_status": "ONLINE",
        "active_routes_count": len(MOCK_BUS_ROUTES),
        "data": MOCK_BUS_ROUTES
    })

if __name__ == '__main__':
    print("Initializing Enterprise Transport Tracker Engine...", file=sys.stderr)
    app.run(host='0.0.0.0', port=8080, debug=True)
