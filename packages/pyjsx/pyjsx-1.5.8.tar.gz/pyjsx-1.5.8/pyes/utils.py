# Utils

# imports:
#   json (data ser/deser)
#   sys  (path append)
#   os   (path operations)
#   schema (Schema detection/validation)
import json, os, sys
from schema import Schema, Use, Optional

class Utils():

    @classmethod
    # make dir and file if they don't exist
    def make_file(self, pp, cc = None): #cc: contents
        ppp = os.path.dirname(pp)
        if(not os.path.exists(ppp)):
            os.makedirs(ppp)
        if(not os.path.exists(pp)):
            with open(pp, 'w') as f: f.write(cc or "")
            return True
        if(cc is not None):
            with open(pp, 'w') as f: f.write(str(cc))
            return True
        return False

    @classmethod
    def file_name(self, pp):
        return '.'.join(pp.split('/')[-1].split('.')[0:-1])

    @classmethod
    def get_user(self):
        return os.path.split(os.path.expanduser('~'))[-1]


class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def update(self, key_path, value):
        keys = key_path.split('/')
        data = 'self'

        for i in range(0, len(keys)):
            data = data + "[\"{0}\"]".format(keys[i])
        
        # preprocess the crop value before
        # if value is a function:
        if(callable(value)):
            value = value.__call__(self.find(key_path))

        if(type(value) == str):
            value = "\"{0}\"".format(value.replace('\n', '\\n'))

        data = "{0} = {1}".format(data, value)
        exec(data)

        return self
        
    def find(self, key_path):
        keys = key_path.split('/')
        curr = self

        for i in range(0, len(keys)):
            try: curr = curr[keys[i]]
            except: return None
        return curr