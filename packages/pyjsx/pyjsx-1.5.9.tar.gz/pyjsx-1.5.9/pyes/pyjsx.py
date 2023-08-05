from pyes.utils import *
# PYJSX
class PYJSX():

    @classmethod
    def jspy_args(self, ss):
        
        #boolean
        if(ss in ['true', 'false']): return ss.title()
        #string
        if(type(ss) == str):         return '\"{0}\"'.format(ss)
        
        #any
        return str(ss)
    
    @classmethod
    def extract_request(self, intf):

        # Super basic request checking:
        pp = intf['active_req']['road']
        ff = intf['active_req']['trac']
        ss = intf['active_req']['seed']
        if(not os.path.exists(pp)): raise ValueError("Python:PYJSX:process_intf: Invalid Road")
        if(not type(ff) == str):    raise ValueError("Python:PYJSX:process_intf: Invalid Trac")
        if(not type(ss) == dict):   raise ValueError("Python:PYJSX:process_intf: Invalid Seed")

        all_args   = ','.join(self.jspy_args(arg) for arg in ss['args'])
        all_kwargs = ','.join(('{0}={1}'.format(k, self.jspy_args(v))) for (k,v) in ss['kwargs'].items())

        return dotdict({

            "path": pp,
            "name": Utils.file_name(pp),
            "func": ff,
            "args": '{0},{1}'.format(all_args, all_kwargs) 
        })
    
    @classmethod
    def execute_request(self, request):

        # append to sys path
        sys.path.append(os.path.dirname(request.path))

        n = request.name
        n_as = n.replace('.', '_')
        f = request.func
        a = request.args
        # execute and harvest
        try:
            exec('import {0} as {1}'.format(n, n_as))
            result = eval('{name_as}.{func}({args})'.format(
                        name_as = n_as,
                        func = f, args = a )
                    )

        except Exception as e:
            result = 'PYJSX:execute_request:{err}'.format(err = str(e).replace('\'', '\\\''))
        
        return result

    @classmethod
    def execute_intf(self, intf):
        return self.execute_request(
            self.extract_request(intf)
        )