#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



from google.net.proto import ProtocolBuffer
import array
import dummy_thread as thread

__pychecker__ = """maxreturns=0 maxbranches=0 no-callinit
                   unusednames=printElemNumber,debug_strs no-special"""

if hasattr(ProtocolBuffer, 'ExtendableProtocolMessage'):
  _extension_runtime = True
  _ExtendableProtocolMessage = ProtocolBuffer.ExtendableProtocolMessage
else:
  _extension_runtime = False
  _ExtendableProtocolMessage = ProtocolBuffer.ProtocolMessage

class Snapshot(ProtocolBuffer.ProtocolMessage):


  INACTIVE     =    0
  ACTIVE       =    1

  _Status_NAMES = {
    0: "INACTIVE",
    1: "ACTIVE",
  }

  def Status_Name(cls, x): return cls._Status_NAMES.get(x, "")
  Status_Name = classmethod(Status_Name)

  has_ts_ = 0
  ts_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def ts(self): return self.ts_

  def set_ts(self, x):
    self.has_ts_ = 1
    self.ts_ = x

  def clear_ts(self):
    if self.has_ts_:
      self.has_ts_ = 0
      self.ts_ = 0

  def has_ts(self): return self.has_ts_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_ts()): self.set_ts(x.ts())

  def Equals(self, x):
    if x is self: return 1
    if self.has_ts_ != x.has_ts_: return 0
    if self.has_ts_ and self.ts_ != x.ts_: return 0
    return 1

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_ts_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: ts not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.ts_)
    return n + 1

  def ByteSizePartial(self):
    n = 0
    if (self.has_ts_):
      n += 1
      n += self.lengthVarInt64(self.ts_)
    return n

  def Clear(self):
    self.clear_ts()

  def OutputUnchecked(self, out):
    out.putVarInt32(8)
    out.putVarInt64(self.ts_)

  def OutputPartial(self, out):
    if (self.has_ts_):
      out.putVarInt32(8)
      out.putVarInt64(self.ts_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_ts(d.getVarInt64())
        continue


      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_ts_: res+=prefix+("ts: %s\n" % self.DebugFormatInt64(self.ts_))
    return res


  def _BuildTagLookupTable(sparse, maxtag, default=None):
    return tuple([sparse.get(i, default) for i in xrange(0, 1+maxtag)])

  kts = 1

  _TEXT = _BuildTagLookupTable({
    0: "ErrorCode",
    1: "ts",
  }, 1)

  _TYPES = _BuildTagLookupTable({
    0: ProtocolBuffer.Encoder.NUMERIC,
    1: ProtocolBuffer.Encoder.NUMERIC,
  }, 1, ProtocolBuffer.Encoder.MAX_TYPE)


  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
  _PROTO_DESCRIPTOR_NAME = 'storage_onestore_v3.Snapshot'
if _extension_runtime:
  pass

__all__ = ['Snapshot']
