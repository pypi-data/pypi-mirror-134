#    @Author: Justin C Presley
#    @Author-Email: justincpresley@gmail.com
#    @Project: NDN State Vector Sync Protocol
#    @Source-Code: https://github.com/justincpresley/ndn-python-svs
#    @Pip-Library: https://pypi.org/project/ndn-svs
#    @Documentation: https://ndn-python-svs.readthedocs.io

from __future__ import annotations

from typing import Optional
from ndn.encoding import Name
from struct import unpack_from
from ndn.encoding import get_tl_num_size, write_tl_num, parse_tl_num, pack_uint_bytes
from .tlv import SVSyncTlvTypes

class Plot:
    def __init__(self, nid:str=None) -> None:
        self.plot, self.nid, self.wire = {}, nid, None
    def find(self, seqno:int) -> Optional[str]:
        try:
            return self.plot[seqno]
        except KeyError:
            return None
    def add(self, seqno:int, label:str) -> None:
        self.wire = None
        self.plot[seqno] = label
    def clear(self) -> None:
        self.plot.clear()
    def getDict(self) -> dict:
        return self.plot
    def getSeqnos(self) -> list:
        return self.plot.keys()
    def getEntries(self) -> List:
        return self.plot.values()
    def getNodeID(self) -> Optional[str]:
        return self.nid
    def incorporate(self, val:Plot) -> None:
        for seqno, label in val.getDict().items():
            self.add(seqno, label)
    def encode(self) -> bytes:
        if self.wire == None:
            wire_list, length = [], 0
            for seqno, label in self.plot.items():
                bseqno, blabel = pack_uint_bytes(seqno), label.encode()
                size = len(bseqno) + get_tl_num_size(len(bseqno)) + get_tl_num_size(SVSyncTlvTypes.SEQNO.value)
                temp1 = bytearray(size)
                pos = write_tl_num(SVSyncTlvTypes.SEQNO.value, temp1)
                pos += write_tl_num(len(bseqno), temp1, pos)
                temp1[pos:pos + len(bseqno)] = bseqno
                length += size
                size = len(blabel) + get_tl_num_size(len(blabel)) + get_tl_num_size(SVSyncTlvTypes.PLOT_ENTRY.value)
                temp2 = bytearray(size)
                pos = write_tl_num(SVSyncTlvTypes.PLOT_ENTRY.value, temp2)
                pos += write_tl_num(len(blabel), temp2, pos)
                temp2[pos:pos + len(blabel)] = blabel
                wire_list.append(temp1 + temp2)
                length += size
            buf_len = length + get_tl_num_size(length) + get_tl_num_size(SVSyncTlvTypes.PLOT.value)
            ret = bytearray(buf_len)
            pos = write_tl_num(SVSyncTlvTypes.PLOT.value, ret)
            pos += write_tl_num(length, ret, pos)
            for w in wire_list:
                ret[pos:pos + len(w)] = w
                pos += len(w)
            self.wire = bytes(ret)
        return self.wire
    @staticmethod
    def parse(buf:Component) -> Optional[Plot]:
        # Verify the Type
        typ, pos = parse_tl_num(buf)
        if typ != SVSyncTlvTypes.PLOT.value:
            return None
        # Check the length
        length, l = parse_tl_num(buf, pos)
        pos += l
        if pos + length != len(buf):
            return None
        # Decode components
        ret:Plot = Plot()
        while pos < len(buf):
            # Seqno
            typ, l = parse_tl_num(buf, pos)
            pos += l
            if typ != SVSyncTlvTypes.SEQNO.value:
                return None
            length, l = parse_tl_num(buf, pos)
            pos += l
            if length == 1:
                seqno = unpack_from('!B', buf, pos)[0]
            elif length == 2:
                seqno = unpack_from('!H', buf, pos)[0]
            elif length == 4:
                seqno = unpack_from('!I', buf, pos)[0]
            elif length == 8:
                seqno = unpack_from('!Q', buf, pos)[0]
            else:
                return None
            pos += length
            # Entry ID
            typ, l = parse_tl_num(buf, pos)
            pos += l
            if typ != SVSyncTlvTypes.PLOT_ENTRY.value:
                return None
            length, l = parse_tl_num(buf, pos)
            pos += l
            entry = buf[pos:pos + length]
            pos += length
            # Use the component
            ret.add(seqno, bytes(entry).decode())
        return ret