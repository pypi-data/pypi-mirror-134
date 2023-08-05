from pyes.utils import *
# File Interface Class
class FileInterface():

    _key_paths = {
        'info/contacts': list,
        'info/requests_made': int,
        'info/requests_exec': int,
        'info/requests_arch': list,
        'active_req/road': str,
        'active_req/trac': str,
        'active_req/seed': dict,
        'active_req/crop': str
    }

    _default_value = dotdict({
            "info": {"contacts": [], "requests_arch": [], "requests_made":0, "requests_exec": 0},
            "active_req": {"road": "", "trac": "", "seed": {"args": [], "kwargs":{}}, "crop": ""}
    })

    _schema_lambs = dotdict({
        
        "seed_dict": lambda sd: 
        sd if(type(sd) == dict and type(sd["args"]) == list 
                and type(sd["kwargs"]) == dict)
            else {"args":[], "kwargs": {}},
        "listt" : lambda c: c if (type(c) == list) else {},
        "pintt" : lambda n: n if (type(n) == int and n>0) else 0,
        "pathh" : lambda p: p if os.path.exists(p) else ""
    })

    _default_schema = Schema({

            "info":
            {
                "contacts": Use(_schema_lambs.listt),
                "requests_arch": Use(_schema_lambs.listt),
                "requests_made": Use(_schema_lambs.pintt),
                "requests_exec": Use(_schema_lambs.pintt)
            },
            
            "active_req":
            {
                "road": Use(_schema_lambs.pathh),
                "trac": Use(str),
                "seed": Use(_schema_lambs.seed_dict),
                "crop": Use(lambda s:s)
            }
        }, ignore_extra_keys=True, description= "File Interface Schema")

    def __init__(self, intf_path = "C:/Users/{0}/AppData/Roaming/PYJSX/INTFS/intf.json".format(Utils.get_user())):

        self.value = self._default_value
        self.path = intf_path

        #if pulled is invalid: recover remains/push
        self.pull(auto_repair=True)
    
    # [VALIDATORS]
    def validate(self, oo):
        return self._default_schema.is_valid(oo)

    # Handle missing and existing args:
    def recover(self, oo):

        try:
            recovered = self._default_schema.validate(oo)
        except:
            recovered = dotdict(self._default_value)
            oo = dotdict(oo)

            for k, v in self._key_paths.items():
                val = oo.find(k)
                if(val and type(val) == v):
                    recovered.update(k, val)
        
        return recovered

    # [GRABBERS]
    def grab_raw(self):
        with open(self.path, 'r') as f: c = f.read()
        return c

    def grab_proper(self):

        if(not os.path.exists(self.path)): return None
        with open(self.path ,'r') as f:
            cc = json.loads(f.read() or "") 
            
        return self.recover(cc)

    def pull(self, auto_repair = False):
        proper_pulled = self.grab_proper() 
        if(proper_pulled is not None): 
            self.value = proper_pulled
            if(auto_repair):
                self.push(new_value= proper_pulled)
            return True
        
        return False

    def grab_signal(self):

        return '{dir_name}/executed_{intf_name}.tmp'.format(
                            dir_name  = os.path.dirname(self.path),
                            intf_name = os.path.basename(self.path)
                    )

    # [SETTERS/MODIFIERS]
    def push(self, new_value = None):
        return Utils.make_file(self.path, cc = json.dumps(
            new_value if self.validate(new_value) else self.value,
            ensure_ascii= False, indent=4  
        ))
    
    def update(self, k_path, val, source = True):

        self.value = dotdict(self.value).update(k_path, val)
        if(source): self.push()
    
    def create_signal(self):
        with open(self.grab_signal(), '+w') as f: 0