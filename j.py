import json
meta = json.loads(open('meta.json').read())
print(meta['timestamp'])
print(meta['provider_scene'])
data = {}
data['timestamp'] = meta['timestamp']
data['provider_scene'] = meta['provider_scene']
print(data)
