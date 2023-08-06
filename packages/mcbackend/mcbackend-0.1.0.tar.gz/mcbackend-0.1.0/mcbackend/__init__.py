"""
A framework agnostic implementation for storage of MCMC draws.
"""
from .backends.numpy import NumPyBackend
from .core import Backend, Chain, ChainMeta, Run, RunMeta

# Backends
try:
    from .backends import clickhouse
    from .backends.clickhouse import ClickHouseBackend
except ModuleNotFoundError:
    pass

# Adapters
try:
    from .adapters import pymc
    from .adapters.pymc import TraceBackend
except ModuleNotFoundError:
    pass


__version__ = "0.1.0"
