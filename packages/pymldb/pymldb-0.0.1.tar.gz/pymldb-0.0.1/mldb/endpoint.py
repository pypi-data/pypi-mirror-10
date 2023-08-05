import requests, json, mldb


def decorate_response(fn):
    def inner(*args, **kwargs):
        return mldb.add_repr_html_to_response(fn(*args, **kwargs))
    return inner

class Endpoint():
    def __init__(self, uri="http://localhost"):
        if not uri.startswith("http"): 
            raise Exception("URIs must start with 'http'")
        self.uri = uri.strip("/")
    
    def __repr__(self):
        return self.uri

    def __str__(self):
        return self.uri
    
    def __call__(self, frag):
        return Endpoint(self.uri+"/"+str(frag).strip("/"))
                                              
    def __getattr__(self, frag): 
        return Endpoint(self.uri+"/"+str(frag).strip("/"))
    
    @decorate_response
    def get(self, *args, **kwargs): 
        return requests.get(self.uri, **kwargs)
    
    @decorate_response
    def get_query(self, *args, **kwargs): 
        return requests.get(self.uri, 
            params= {k: (json.dumps(v) if isinstance(v, dict) else v) 
                 for k,v in dict(**kwargs).iteritems() })
    
    @decorate_response
    def put(self, *args, **kwargs): 
        return requests.put(self.uri, **kwargs)
    
    @decorate_response
    def put_json(self, payload): 
        return requests.put(self.uri, data=json.dumps(payload))
    
    @decorate_response
    def post(self, *args, **kwargs): 
        return requests.post(self.uri, **kwargs)
    
    @decorate_response
    def post_json(self, payload): 
        return requests.post(self.uri, data=json.dumps(payload))
    
    @decorate_response
    def delete(self, *args, **kwargs): 
        return requests.delete(self.uri, **kwargs)
    
