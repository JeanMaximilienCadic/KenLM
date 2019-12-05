from kenlm import *
import os
from gnutools.utils import parent

def bin(binary):
    os.system(os.path.join(parent(os.path.abspath(__file__)), "bin/{}".format(binary)))
