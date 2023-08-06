import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

from core import Mobj, wrap_run


class Mwebui(Mobj):
    def __init__(self):
        super(Mwebui, self).__init__()
        op = Options()
        # op.add_argument("start-maximized")
        self.dv = webdriver.Chrome(options=op)
        self.dv.implicitly_wait(3)
        self.cmd_get(self.conf['base_url'])
        pos = self.conf['pos']
        self.dv.set_window_position(x=pos[0], y=pos[1])
        self.dv.set_window_size(width=pos[2], height=pos[3])

    def load_conf(self):
        super(Mwebui, self).load_conf()
        conf = os.path.join(self.base_path, 'conf', f'{self.__class__.__name__.lower()}.xlsx')
        self.cmds = pd.read_excel(conf, sheet_name='cmds', dtype='object')
    
    def x(self, cmd):
        xpath = cmd if isinstance(cmd, str) else cmd['xpath']
        return self.dv.find_element(By.XPATH, xpath)
    
    def cmd_js(self, cmd):
        if isinstance(cmd, dict):
            self.dv.execute_script(f'var e = arguments[0]; e.{cmd["js"]}', self.x(cmd))
        elif isinstance(cmd, str):
            self.dv.execute_script(cmd)

    def cmd_get(self, url):
        self.dv.get(url)

    def cmd_cs(self, xpaths):
        return [self.x(p).click() for p in xpaths]

    @wrap_run
    def run(self, cmd):
        print(f'P2.{self.optd}')
