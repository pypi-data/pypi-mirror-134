from pathlib import Path

from cmt import utils
from cmt.a_map import AMap, MapType
from cmt.cmap.v0 import *
from cmt.cmap.v1 import *
from cmt.cmap.v2 import *
from cmt.ecmap.v0 import *
from cmt.ecmap.v1 import *
from cmt.ecmap.v2 import *
from cmt.ecmap.v4 import *


_TYPE_MAP = {
    (MapType.CMAP, 0): CMap_0,
    (MapType.CMAP, 1): CMap_1,
    (MapType.CMAP, 2): CMap_2,
    (MapType.ECMAP, 0): ECMap_0,
    (MapType.ECMAP, 1): ECMap_1,
    (MapType.ECMAP, 2): ECMap_2,
    (MapType.ECMAP, 4): ECMap_4,
}


def decode(file: Path, debug: bool = False) -> AMap:
    """
    :raises ValueError: something failed
    """
    with file.open("rb") as reader:
        data = reader.read()

    identifier = data[0:11].decode("utf-8")
    if debug:
        utils.debug_print(data[0:11], "identifier", identifier, 0)
    offset = 11

    if identifier != MapType.CMAP.value and identifier != MapType.ECMAP.value:
        raise ValueError("given data is not a .cmap or .ecmap")

    version = utils.unpack_from('<B', data, offset, ("version",), debug)[0]
    offset += 1

    map_cls = _TYPE_MAP.get((MapType(identifier), version), None)
    if map_cls is None:
        raise ValueError(f"reading {identifier} version {version} is not supported")

    return map_cls.decode(data, offset, debug)


def encode(source: AMap, file: Path):
    with file.open("wb") as writer:
        writer.write(source.encode())
