from flask import Flask, jsonify
import time
import redis

app = Flask(__name__)

# Connexion à Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def slow_function():
    """Fonction simulant un traitement coûteux"""
    time.sleep(3)  # simule une latence de 3 secondes
    return {"message": "Données traitées"}

@app.route('/data_nocache')
def data_no_cache():
    """Sans cache Redis"""
    result = slow_function()
    return jsonify(result)

@app.route('/data_cache')
def data_cache():
    """Avec cache Redis"""
    cached_result = cache.get('mydata')
    if cached_result:
        return jsonify(eval(cached_result.decode()))
    
    result = slow_function()
    cache.setex('mydata', 60, str(result))  # TTL = 60 secondes
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

