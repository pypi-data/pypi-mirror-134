"""An MPEG-4 elementary stream descriptor atom. This extension is required for MPEG-4 video"""
from .atom import FullBox, full_box_derived


class Descriptor:
    """A descriptor for MPEG-4 video, as defined in the MPEG-4 specification ISO/IEC 14496-1
       and subject to the restrictions for storage in MPEG-4 files specified in ISO/IEC 14496-14"""
    def __init__(self, tag, file):
        self._tag = tag
        self._indicator = file.read(1)
        if int.from_bytes(self.indicator, "big") == 0x80:
            self._indicator += file.read(2)
            self._length = file.read(1)[0]
        else:
            self._length = self.indicator[0]
            self._indicator = bytearray()

    def __str__(self):
        return 'tag {:x} len={}'.format(self._tag, self._length)

    def __repr__(self):
        return 'Descriptor({:x})'.format(self._tag)

    def __len__(self):
        return self._length

    def to_bytes(self):
        """Returns sample optional fields as bytestream, ready to be sent to socket"""
        ret = self._tag.to_bytes(1, byteorder='big')
        if self._indicator:
            ret += self._indicator
        ret += self._length.to_bytes(1, byteorder='big')
        return ret

    @property
    def tag(self):
        """Returns descriptor tag"""
        return self._tag

    @property
    def indicator(self):
        """Returns descriptor indicator"""
        return self._indicator


class ESDescriptor(Descriptor):
    """An elementary stream descriptor for MPEG-4 video"""
    def __init__(self, file):
        super().__init__(3, file)
        self.stream_id = int.from_bytes(file.read(2), 'big')
        self.stream_priority = file.read(1)[0]

    def __str__(self):
        return super().__str__() + ' ' + self.__repr__()

    def __repr__(self):
        return f'id:{self.stream_id} priority:{self.stream_priority}'

    def to_bytes(self):
        return super().to_bytes() + self.stream_id.to_bytes(2, byteorder='big') + \
                                    self.stream_priority.to_bytes(1, byteorder='big')


class ConfigDescriptor(Descriptor):
    """An elementary stream configuration descriptor for MPEG-4 video"""
    def __init__(self, file):
        super().__init__(4, file)
        _object_dict = {
            1: 'system v1',
            2: 'system v2',
            32: 'MPEG-4 video',
            33: 'MPEG-4 AVC SPS',
            34: 'MPEG-4 AVC PPS',
            64: 'MPEG-4 audio',
            96: 'MPEG-2 simple video',
            97: 'MPEG-2 main video',
            98: 'MPEG-2 SNR video',
            99: 'MPEG-2 spatial video',
            100: 'MPEG-2 high video',
            101: 'MPEG-2 4:2:2 video',
            102: 'MPEG-4 ADTS main',
            103: 'MPEG-4 ADTS Low Complexity',
            104: 'MPEG-4 ADTS Scalable Sampling Rate',
            105: 'MPEG-2 ADTS',
            106: 'MPEG-1 video',
            107: 'MPEG-1 ADTS',
            108: 'JPEG video',
            192: 'private audio',
            208: 'private video',
            224: '16-bit PCM LE audio',
            225: 'vorbis audio',
            226: 'dolby v3 (AC3) audio',
            227: 'alaw audio',
            228: 'mulaw audio',
            229: 'G723 ADPCM audio',
            230: '16-bit PCM Big Endian audio',
            240: 'YCbCr 4:2:0 (YV12) video',
            241: 'H264 video',
            242: 'H263 video',
            243: 'H261 video'
        }
        _stream_dict = {
            1: 'object descriptor.',
            2: 'clock ref.',
            3: 'scene descriptor.',
            4: 'visual',
            5: 'audio',
            6: 'MPEG-7',
            7: 'IPMP',
            8: 'OCI',
            9: 'MPEG Java',
            32: 'user private'
        }
        self.object_type_id = file.read(1)[0]
        try:
            self._object_type = _object_dict[self.object_type_id]
        except KeyError:
            self._object_type = str(self.object_type_id)
        self.stream_type = file.read(1)[0]
        try:
            self._stream_type = _stream_dict[self.stream_type >> 2]
        except KeyError:
            self._stream_type = str(self.stream_type)
        self.buffer_size = int.from_bytes(file.read(3), 'big')
        self.max_bit_rate = int.from_bytes(file.read(4), 'big')
        self.av_bit_rate = int.from_bytes(file.read(4), 'big')

    def __str__(self):
        return super().__str__() + ' ' + self.__repr__()

    def __repr__(self):
        return f" obj:'{self._object_type}' stream:'{self._stream_type}'" + \
               f" buf size:{self.buffer_size} max br:{self.max_bit_rate}" + \
               f" av br:{self.av_bit_rate}"

    def to_bytes(self):
        return super().to_bytes() + self.object_type_id.to_bytes(1, byteorder='big') + \
                                    self.stream_type.to_bytes(1, byteorder='big') + \
                                    self.buffer_size.to_bytes(3, byteorder='big') + \
                                    self.max_bit_rate.to_bytes(4, byteorder='big') + \
                                    self.av_bit_rate.to_bytes(4, byteorder='big')


class DecoderSpecificDescriptor(Descriptor):
    """An elementary stream decoder descriptor for MPEG-4 video"""
    def __init__(self, file):
        super().__init__(5, file)
        self._header_start_codes = file.read(len(self))

    def __str__(self):
        return super().__str__() + ' ' + self.__repr__()

    def __repr__(self):
        return " start_codes:[" + self.config + ']'

    @property
    def config(self):
        """Returns header as hex string"""
        return ''.join('{:02x}'.format(x) for x in self._header_start_codes)

    def to_bytes(self):
        return super().to_bytes() + self._header_start_codes


class SLConfigDescriptor(Descriptor):
    """An elementary stream synchronization properties descriptor for MPEG-4 video"""
    def __init__(self, file):
        super().__init__(6, file)
        self.value = file.read(1)[0]

    def __repr__(self):
        return f" sl:{self.value}"

    def to_bytes(self):
        return super().to_bytes() + self.value.to_bytes(1, byteorder='big')


@full_box_derived
class Box(FullBox):
    """An MPEG-4 elementary stream descriptor box"""
    descriptors = []

    def __repr__(self):
        return super().__repr__() + \
               ' descriptors: [' + ''.join('{'+str(d)+'}' for d in self.descriptors) + ']'

    def init_from_file(self, file):
        self.descriptors = []
        left = self.size - (file.tell() - self.position)
        while left > 0:
            tag = file.read(1)[0]
            if tag == 3:
                self.descriptors.append(ESDescriptor(file))
            elif tag == 4:
                self.descriptors.append(ConfigDescriptor(file))
            elif tag == 5:
                self.descriptors.append(DecoderSpecificDescriptor(file))
            elif tag == 6:
                self.descriptors.append(SLConfigDescriptor(file))
            else:
                break
            left = self.size - (file.tell() - self.position)

    @property
    def config(self):
        """Returns header from decoder specific descriptor"""
        return [desc for desc in self.descriptors if desc.tag == 5][0].config

    def to_bytes(self):
        ret = super().to_bytes()
        for descriptor in self.descriptors:
            ret += descriptor.to_bytes()
        return ret
