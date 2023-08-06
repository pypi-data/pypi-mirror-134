from .bespoke import BespokeModule
from .modules import Module, ModuleName
from .schemathesis import SchemathesisModule
from .ssrfmap import SsrfmapModule


def initialize_module(name: str) -> Module:
    if name == ModuleName.Schemathesis.upper():
        return SchemathesisModule(name)
    elif name == ModuleName.Bespoke.upper():
        return BespokeModule(name)
    elif name == ModuleName.Ssrfmap.upper():
        return SsrfmapModule(name)
    else:
        raise Exception(f"Unrecognized module: {name}")
