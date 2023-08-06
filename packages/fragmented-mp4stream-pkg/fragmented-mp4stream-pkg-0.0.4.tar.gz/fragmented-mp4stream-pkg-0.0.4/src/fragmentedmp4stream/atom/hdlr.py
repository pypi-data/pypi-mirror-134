"""Declares the process by which the media-data in the track is presented,
   and thus, the nature of the media in a track.
"""
from .atom import FullBox, full_box_derived


def atom_type():
    """Returns this atom type"""
    return 'hdlr'


@full_box_derived
class Box(FullBox):
    """The media handler type box"""
    handler_type = ''
    name = ''

    def __repr__(self):
        return super().__repr__() + f" handler type:{self.handler_type} name:{self.name}"

    def init_from_file(self, file):
        self._read_some(file, 4)
        self.handler_type = self._read_some(file, 4).decode("utf-8")
        self._read_some(file, 12)
        left = (self.size - (file.tell() - self.position))
        if left > 0:
            self.name = self._read_some(file, left).decode("utf-8")

    def to_bytes(self):
        ret = super().to_bytes() +\
              (0).to_bytes(4, byteorder='big') + \
              str.encode(self.handler_type) + \
              (0).to_bytes(4, byteorder='big') + \
              (0).to_bytes(8, byteorder='big')
        if self.name:
            ret += str.encode(self.name)
        return ret
