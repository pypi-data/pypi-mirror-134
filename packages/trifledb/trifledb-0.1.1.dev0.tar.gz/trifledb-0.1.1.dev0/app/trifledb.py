class TrifleDB:
    def __init__(self):
        self.db = {}
        return

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __delitem__(self, key):
        return self.delete(key)
    
    def get(self, key):
        if key in self.db:
            return self.db[key]
        return False

    def put(self, key, value):
        self.db[key] = value
        return True

    def delete(self, key):
        if key in self.db:
    	    del self.db[key]
    	    return True
        return False