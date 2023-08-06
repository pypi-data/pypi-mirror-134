from cmt.a_converter import AConverter
from cmt.a_map import AMap, MapType
from cmt.converter import *

_CONVERTER_MAP = {
    (MapType.CMAP, 0): Converter_cmap_0,
    (MapType.CMAP, 1): Converter_cmap_1,
    (MapType.CMAP, 2): Converter_cmap_2,
    (MapType.ECMAP, 0): Converter_ecmap_0,
    (MapType.ECMAP, 1): Converter_ecmap_1,
    (MapType.ECMAP, 2): Converter_ecmap_2,
    (MapType.ECMAP, 4): Converter_ecmap_4,
}


def _get_converter(map_type: MapType, version: int) -> AConverter:
    """
    :raises ValueError: something failed
    """
    conv = _CONVERTER_MAP.get((map_type, version), None)
    if conv is None:
        raise ValueError(f"Converter for {map_type.name} {version} does not exist.")
    return conv()


def convert(source: AMap, version: int, target: MapType) -> AMap:
    """
    First convert to the target type and down/upgrade to the correct version.
    :raises ValueError: something failed
    """
    res = source
    if res.identifier != target:
        res = _get_converter(res.identifier, res.format_version).convert(res)

    while res.format_version != version:
        if res.format_version > version:
            res = _get_converter(res.identifier, res.format_version).downgrade(res)
        else:
            res = _get_converter(res.identifier, res.format_version).upgrade(res)
    return res
