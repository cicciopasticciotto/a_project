import time
import six
import maggma
import abipy
import abipy.abilab 
import matplotlib
from pymatgen.util.plotting import pretty_plot


matplotlib.use('agg')


def a_sleep_function():
    print("!!! ", abipy.__file__)
    abipy.abilab.TaskManager.from_user_config()
    time.sleep(1)

def plot_something():
    matplotlib.rc('text', usetex=False)
    matplotlib.rc('font', family='serif')
    
    plt = pretty_plot(6, 5.5)
    
    plt.plot([1,2,3], [1,2,3])
    
    plt.tight_layout()
    
    return plt
