from typing import Callable, List, Tuple

from .expr import exmat
from .mesh import Mesh, Group
from .planarpy import Nexus


class Dom:
    __nexus: Nexus

    def __init__(self, mesh: Mesh):
        self.__nexus = Nexus(mesh.pts, mesh.edges, mesh.cells)

    def plot_sys(self) -> Tuple[List[float], List[float], List[float]]:
        return self.__nexus.plot_sys()

    def set_boundary(self, *groups):
        for group in groups:
            self.__nexus.set_boundary(group.nodes, group.edges)
        self.__nexus.set_dofs()
        self.__nexus.set_solver()

    def dofs(self) -> Tuple[int, int]:
        return self.__nexus.dofs()

    def embed_bcond(self, bcond: Callable[[float, float], List[float]], group):
        arena, vec = exmat(bcond)
        self.__nexus.embed_bcond(list(group.nodes), list(group.edges), arena, vec)

    def set_force(self, force: Callable[[float, float], List[float]], group: Group = None):
        if group is None:
            arena, vec = exmat(force)
            self.__nexus.set_force(0, set(), arena, vec)
        else:
            arena, vec = exmat(force)
            self.__nexus.set_force(group.id, group.cells, arena, vec)

    def set_consts(self, *consts: float):
        self.__nexus.set_consts(consts)

    def solve(self, tol: float = 1e-10):
        self.__nexus.assemble()
        self.__nexus.solve(tol)

    def plot_disp(self) -> Tuple[List[float], List[float], List[float]]:
        return self.__nexus.plot_disp()
