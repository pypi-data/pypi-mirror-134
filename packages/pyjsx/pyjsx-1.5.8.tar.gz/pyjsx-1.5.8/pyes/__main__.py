from pyes.file_interface import *
from pyes.pyjsx import *
import argparse

DEFAULT_INTERFACE_PATH = "C:/Users/bouda/AppData/Roaming/PYJSX/INTFS/intf.json"
PARSER_CFG = {
    'default': DEFAULT_INTERFACE_PATH,
    'type': str

}

def run(path):
    ff = FileInterface(intf_path=path)
    rr = PYJSX.execute_intf(ff.grab_proper())
    ff.update('info/requests_exec', lambda x: x+1)
    ff.update('active_req/crop', rr)
    ff.create_signal()

def main():
    P = argparse.ArgumentParser()
    P.add_argument('-f', '--file-interface', **PARSER_CFG)
    A = P.parse_args()

    run(A.file_interface)

if __name__ == '__main__': main()