from cmt.a_converter import AConverter
from cmt.cmap.v1 import *
from cmt.cmap.v2 import *
from cmt.ecmap.v4 import *


class Converter(AConverter):
    @staticmethod
    def convert(source: CMap_2) -> ECMap_4:
        ecmap = ECMap_4()
        ecmap.cmap = source
        ecmap.cmap.checkpoint_times = None
        return ecmap

    @staticmethod
    def downgrade(source: CMap_2) -> CMap_1:
        res = CMap_1()
        res.name = source.name
        res.checkpoint_times = source.checkpoint_times
        res.sun_rotation = source.sun_rotation_hor
        res.sun_angle = source.sun_rotation_ver
        res.camera_pos = source.camera_pos
        res.camera_look = source.camera_look

        for ent in source.entities:
            new_ent = None
            if type(ent) == Block_2:
                new_ent = Block_1()
                new_ent.block_type = ent.block_type
                new_ent.position = (int(ent.position[0]), int(ent.position[1]), int(ent.position[2]))
                new_ent.scale = (int(ent.scale[0]), int(ent.scale[1]), int(ent.scale[2]))
                new_ent.rotation_z = ent.rotation_z
                new_ent.checkpoint_nr = ent.checkpoint_nr
                new_ent.byte_size = ent.byte_size
            elif type(ent) == Sphere_2:
                new_ent = Sphere_1()
                new_ent.position = (int(ent.position[0]), int(ent.position[1]), int(ent.position[2]))
            elif type(ent) == PlayerStart_2:
                new_ent = PlayerStart_1()
                new_ent.position = (int(ent.position[0]), int(ent.position[1]), int(ent.position[2]))
                new_ent.rotation_z = ent.rotation_z
            elif type(ent) == Dummy_2:
                new_ent = Dummy_1()
                new_ent.id = ent.id
                new_ent.position = (int(ent.position[0]), int(ent.position[1]), int(ent.position[2]))
                new_ent.scale = (int(ent.scale[0]), int(ent.scale[1]), int(ent.scale[2]))
                new_ent.rotation_z = ent.rotation_z
            if new_ent is not None:
                res.entities.append(new_ent)
        return res

    @staticmethod
    def upgrade(source: CMap_2) -> 'CMap_3':
        raise ValueError(
            f"Upgrading {source.identifier.name} {source.format_version} to"
            f" {source.identifier.name} {source.format_version + 1} is not supported."
        )
