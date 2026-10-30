"""Zero the bytes after the NUL terminator of every Texts6 font-name field.

Altium writes each text's TrueType font name into a fixed 64-byte UTF-16LE
field and leaves whatever was in memory after the terminator. KiCad 9.0.9's
importer converts all 64 bytes and keeps the part before the first NUL; when
the leftover bytes contain an unpaired surrogate the whole conversion fails,
the name comes back empty and the text silently drops to the KiCad stroke font
(with stroke-font size conversion). Zeroing the padding changes nothing Altium
or KiCad reads as data. The stream keeps its exact size.

usage: sanitize_fonts.py <in.PcbDoc> <out.PcbDoc>"""
import shutil
import struct
import sys

import olefile

src, dst = sys.argv[1], sys.argv[2]
shutil.copyfile(src, dst)
ole = olefile.OleFileIO(dst, write_mode=True)
data = bytearray(ole.openstream("Texts6/Data").read())
i = fixed = 0
while i < len(data):
    i += 1                                   # record type
    n = struct.unpack_from("<I", data, i)[0]
    i += 4
    props = i
    if n >= 46 + 64:
        f = props + 46
        end = next((k for k in range(0, 64, 2) if data[f + k:f + k + 2] == b"\0\0"), 64)
        if any(data[f + end:f + 64]):
            data[f + end:f + 64] = bytes(64 - end)
            fixed += 1
    i += n
    n2 = struct.unpack_from("<I", data, i)[0]
    i += 4 + n2
assert i == len(data), "Texts6 walk did not end on the stream boundary"
ole.write_stream("Texts6/Data", bytes(data))
ole.close()
print(f"{dst}: sanitized {fixed} font-name fields")
