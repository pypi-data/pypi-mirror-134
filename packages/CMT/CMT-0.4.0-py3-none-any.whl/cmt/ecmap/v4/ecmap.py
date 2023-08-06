import struct

from cmt import utils
from cmt.cmap.v2 import *
from cmt.ecmap.a_ecmap import AECMap


class ECMap(AECMap):
    """
    Celaria .ecmap format (version 4)

    **Datatypes**

    .. list-table::
        :header-rows: 1

        * - Abbreviation
          - Type
          - Byte size
        * - uByte
          - unsigned byte
          - 1
        * - uShort
          - unsigned short
          - 2
        * - uInt
          - unsigned int
          - 4
        * - sShort
          - signed short
          - 2
        * - sInt
          - signed int
          - 4
        * - f32
          - float
          - 4
        * - f64
          - double
          - 8

    **Description format**

    ``> <datatype> (<number of datatypes in sequence>) // <description>``

    or

    ``> [<variable name>] : <datatype> (<number of datatypes in sequence>) // <description>``

    Difference regarding to the .cmap begins with a '!!'.

    Comparing to CMap v2.

    **Format**

    .. code-block:: none

        > uByte (11) // string identifier
        > uByte (1) // version

        > nameLen : uByte (1) // number of characters in map name
        > uByte (nameLen) // map name as String

        > uByte (1) // unused - gamemode

        !! // checkpoint times are missing

        > f32 (1) // sun rotation horizontal
        > f32 (1) // sun rotation vertical (between 0 and 90 degrees)

        ... same as cmap v2 ...
    """

    def __init__(self):
        super().__init__(4)
        self.cmap: CMap_2 = CMap_2()

    def __str__(self):
        return f"identifier: {self.identifier.name}\n" \
               f"format version: {self.format_version}\n" \
               f"::cmap::\n" + \
               str(self.cmap)

    @classmethod
    def decode(cls, data: bytes, offset: int, debug: bool = False) -> CMap_2:
        cmap = CMap_2()

        name_len = utils.unpack_from('<B', data, offset, ("name length",), debug)[0]
        offset += 1

        cmap.name = data[offset:offset + name_len].decode("utf-8")
        if debug:
            utils.debug_print(data[offset:offset + name_len], "name", cmap.name, offset)
        offset += name_len

        utils.unpack_from('<?', data, offset, ("unused (gamemode)",), debug)
        offset += 1

        cmap.sun_rotation_hor = utils.unpack_from('<f', data, offset, ("sun rotation horizontal",), debug)[0]
        offset += 4

        cmap.sun_rotation_ver = utils.unpack_from('<f', data, offset, ("sun rotation vertical",), debug)[0]
        offset += 4

        cmap.camera_pos = utils.unpack_from('<ddd', data, offset, ("camera pos x", "camera pos y", "camera pos z"),
                                            debug)
        offset += 3 * 8

        cmap.camera_look = utils.unpack_from('<ddd', data, offset, ("camera look x", "camera look y", "camera look z"),
                                             debug)
        offset += 3 * 8

        # entities processing
        ent_count = utils.unpack_from('<I', data, offset, ("entity count",), debug)[0]
        offset += 4

        ent_done = 0
        while ent_done < ent_count:
            ent_type = utils.unpack_from('<B', data, offset, ("entity type",), debug)[0]
            offset += 1
            if ent_type == 0:
                cur_ent = Block_2.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 1:
                cur_ent = Sphere_2.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 2:
                cur_ent = PlayerStart_2.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 3:
                cur_ent = BarrierWall_2.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 4:
                cur_ent = BarrierFloor_2.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            elif ent_type == 128:
                cur_ent = Dummy_2.decode(data, offset, debug)
                cmap.entities.append(cur_ent)
                offset += cur_ent.byte_size
            else:
                raise ValueError(f"Unknown entity type: {ent_type} at {offset - 1}")
            ent_done += 1
        if debug:
            print(offset, " / ", len(data), " consumed")
        if offset != len(data):
            raise ValueError("Not all bytes were consumed")
        return cmap

    def encode(self) -> bytearray:
        data = bytearray()
        # file identifier
        data.extend(self.identifier.value.encode("utf-8"))
        # format version
        data.extend(struct.pack('<B', self.format_version))
        # length of name
        data.extend(struct.pack('<B', len(self.cmap.name)))
        # name
        data.extend(self.cmap.name.encode("utf-8"))
        # unused byte - gamemode
        data.extend(b'\x01')
        # sun rotation
        data.extend(struct.pack('<f', self.cmap.sun_rotation_hor))
        # sun angle
        data.extend(struct.pack('<f', self.cmap.sun_rotation_ver))
        # camera position
        data.extend(struct.pack('<ddd', *self.cmap.camera_pos))
        # camera look
        data.extend(struct.pack('<ddd', *self.cmap.camera_look))
        # entity count
        data.extend(struct.pack('<I', len(self.cmap.entities)))
        # entities
        for ent in self.cmap.entities:
            data.extend(ent.encode())
        return data
