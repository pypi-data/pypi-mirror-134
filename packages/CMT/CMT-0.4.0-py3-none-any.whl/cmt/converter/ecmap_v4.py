from cmt.a_converter import AConverter
from cmt.cmap.v2 import *
from cmt.converter.cmap_v2 import Converter as Converter_cmap_2
from cmt.ecmap.v2 import *
from cmt.ecmap.v4 import *


class Converter(AConverter):
    @staticmethod
    def convert(source: ECMap_4) -> 'CMap_2':
        return source.cmap

    @staticmethod
    def downgrade(source: ECMap_4) -> ECMap_2:
        res = ECMap_2()
        res.cmap = Converter_cmap_2.downgrade(source.cmap)
        return res

    @staticmethod
    def upgrade(source: ECMap_4) -> 'ECMap_5':
        raise ValueError(
            f"Upgrading {source.identifier.name} {source.format_version} to"
            f" {source.identifier.name} {source.format_version + 1} is not supported."
        )
