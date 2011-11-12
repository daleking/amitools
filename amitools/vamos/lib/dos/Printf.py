"""Handle printf like Functions including VPrintf and RawDoFmt"""

import re

class printf_element:
  def __init__(self, txt, begin, end, etype, flags=None, width=None, limit=None, length=None):
    self.txt = txt
    self.begin = begin
    self.end = end
    self.etype = etype
    self.flags = flags
    self.width = width
    self.limit = limit
    self.length = length
    self.data = None
    
  def __str__(self):
    sf = self.gen_sys_printf_format()
    return "[%d:%d:'%s'=%s (%s)(type=%s,flags=%s,width=%s,limit=%s,length=%s)]" % (self.begin, self.end, self.txt, self.data, sf, self.etype,self.flags,self.width,self.limit,self.length)
  
  def gen_sys_printf_format(self):
    t = self.etype
    if t == 'b':
      t == 's'
    result = []
    result.append('%')
    result.append(self.flags)
    if self.width != None:
      result.append(self.width + '.')
    if self.limit != None:
      result.append(self.limit)
    result.append(t)
    return "".join(result)

class printf_state:
  def __init__(self, elements, fragments):
    self.elements = elements
    self.fragments = fragments

  def __str__(self):
    return "[elements:%s, fragments:%s]" % (map(str, self.elements), self.fragments)

printf_re_format = "%([-]?)([0-9]+\.)?([0-9]+)?([l])?([bduxsc])"

def printf_parse_string(string):
  # groups in pattern:
  # 1 flags (opt)
  # 2 width (opt)
  # 3 limit (opt)
  # 4 length (opt)
  # 5 type (req)
  matches = re.finditer(printf_re_format, string)
  pos = 0
  end = len(string)
  fragments = []
  elements = []
  for m in matches:
    m_s = m.start()
    m_e = m.end()
    if pos < m_s:
      # create new string fragment
      fs = string[pos:m_s]
      fragments.append(fs)
    
    # fetch options
    flags = m.group(1)
    width = m.group(2)
    if width != None:
      width = int(width[:-1])
    limit = m.group(3)
    if limit != None:
      limit = int(limit)
    length = m.group(4)
    etype = m.group(5)
    txt = string[m_s:m_e]
    # create element
    e = printf_element(txt,m_s,m_e,etype,flags,width,limit,length)
    elements.append(e)
    pos = m_e

  if pos < end:
    fs = string[pos:]
    fragments.append(fs)
  return printf_state(elements,fragments)

def printf_read_data(state, mem_access, data_ptr):
  elements = state.elements
  for e in elements:
    t = e.etype
    if t == 'b': # BSTR
      bptr = mem_access.r32(data_ptr)
      data_ptr += 4
      bptr *= 4
      data = mem_access.r_bstr(bptr)
    elif t in ('d','u','x'): # number
      l = e.length 
      if "l" in l:
        data = mem_access.r32(data_ptr)
        data_ptr += 4
      else:
        data = mem_access.r16(data_ptr)
        data_ptr += 2
    elif t == 's': # STR
      cptr = mem_access.r32(data_ptr)
      data_ptr += 4
      data = mem_access.r_cstr(cptr)
    elif t == 'c': # char
      data = mem_access.r16(data_ptr)
      data_ptr += 2
      data = chr(data)
    e.data = data

def printf_generate_output(state):
  result = []
  pos = 0
  f = state.fragments
  for e in state.elements:
    begin = e.begin
    if pos < begin:
      result.append(f.pop(0))
    fmt = e.gen_sys_printf_format()
    val = fmt % e.data
    result.append(val)
    pos = e.end
  if len(f) > 0:
    result.append(f[0])
  return "".join(result)

def printf(string, mem_access, data_ptr):
  ps = printf_parse_string(string)
  printf_read_data(ps, mem_access, data_ptr)
  return printf_generate_output(ps)

# test
if __name__ == '__main__':
  txt = "hello %s... %d what a number %2ld.. now align %-4.2s!"
  print txt
  elements, fragments = printf_parse_string(txt)
  for e in elements:
    print e
  print fragments
  
  txt = "%s begin and last %d"
  print txt
  elements, fragments = printf_parse_string(txt)
  for e in elements:
    print e
  print fragments
  