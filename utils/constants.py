NEGATIVE_INF = -100000.0

with open('.perspective_api_key', 'r') as f:
    key = f.read().strip()
PERSPECTIVE_API_KEY = key

PERSPECTIVE_API_ATTRIBUTES = {
    'TOXICITY'
}

PERSPECTIVE_API_ATTRIBUTES_LOWER = tuple(a.lower() for a in PERSPECTIVE_API_ATTRIBUTES)
