from cmt.a_converter import AConverter
from cmt.converter.cmap_v1 import Converter as Converter_cmap_1
from cmt.cmap.v1 import *
from cmt.ecmap.v0 import *
from cmt.ecmap.v1 import *
from cmt.ecmap.v2 import *


class Converter(AConverter):
    @staticmethod
    def convert(source: ECMap_1) -> CMap_1:
        return source.cmap

    @staticmethod
    def downgrade(source: ECMap_1) -> ECMap_0:
        res = ECMap_0()
        res.cmap = Converter_cmap_1.downgrade(source.cmap)
        return res

    @staticmethod
    def upgrade(source: ECMap_1) -> ECMap_2:
        res = ECMap_2()
        res.cmap = source.cmap
        return res
