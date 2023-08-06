from cmt.a_converter import AConverter
from cmt.converter.cmap_v1 import Converter as Converter_cmap_1
from cmt.ecmap.v1 import *
from cmt.ecmap.v2 import *
from cmt.ecmap.v4 import *


class Converter(AConverter):
    @staticmethod
    def convert(source: ECMap_2) -> 'CMap_1':
        return source.cmap

    @staticmethod
    def downgrade(source: ECMap_2) -> ECMap_1:
        res = ECMap_1()
        res.cmap = source.cmap
        return res

    @staticmethod
    def upgrade(source: ECMap_2) -> ECMap_4:
        res = ECMap_4()
        res.cmap = Converter_cmap_1.upgrade(source.cmap)
        return res
