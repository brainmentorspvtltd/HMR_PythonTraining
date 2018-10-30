# Run 'python setup.py build' on cmd

import sys
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options = {
    'build_exe': {
        'include_files': [
            'background.png',
            'background_2.png',
            'homeBackground.jpg',
            'shot_sound.wav',
            'aim_pointer.png',
            'gun.png',
            'gun_1.png',
            'zombie_1.png',
            'zombie_2.png',
            'zombie_3.png',
            'zombie_4.png'
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('game.py')
]

setup(name='Zombie Killer',
      version='0.1',
      description='Python Game Demo',
      options=options,
      executables=executables
      )