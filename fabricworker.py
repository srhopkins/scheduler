import traceback
import base64
import json
from pprint import pprint
from fabric.api import *

env_common = {'abort_on_prompts': True,
              'use_ssh_config': True,
              'keepalive': 15,
              'warn_only': True,
              'skip_bad_hosts': True}

class AttrDict(dict):
    #http://stackoverflow.com/questions/4984647/accessing-dict-keys-like-an-attribute-in-python
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class Worker():
    def __init__(self, env_settings={}):
        self.env = AttrDict(env) # global env from --> from fabric.api import *
        for key, value in env_settings.items():
            if value:
                self.env[key] = value
    
    def do_this(self, cmd, host, *args, **kwargs): #fabric_settings=dict(self.env.items())
        self.env.host_string=host
        with hide('output','running','warnings'), settings(**dict(self.env.items())):
            output = {"host": host,
                      "cmd": {"function": cmd.__name__,
                              "args": args,
                              "kwargs": kwargs}}
            try:
                out = cmd(*args, **kwargs)
                output["type"] = "output"
                output["output"] = out
            except BaseException as e:
                trace = traceback.format_exc()
                output["type"] = "error"
                output["exception"] = type(e).__name__
                output["output"] = trace
        return output
    
    def do_this_json(self, *args, **kwargs):
        return json.dumps(self.do_this(*args, **kwargs), indent=4)
    
    def env_change(self, env_settings):
        # Useful if you have a premade dict of settings otherwise change the objects env
        # attributes already mapped. (e.g.) Worker().env.user = 'steven'
        for key, value in env_settings.items():
            if value:
                self.env[key] = value
