from amitools.vamos.cfgcore import *


class TraceParser(Parser):
  def __init__(self, ini_prefix=None):
    def_cfg = {
        "trace": {
            "instr": False,
            "memory": False,
            "internal_memory": False,
            "reg_dump": False,
            "labels": False
        }
    }
    arg_cfg = {
        "trace": {
            "instr": Argument('-I', '--instr-trace', action='store_true',
                              help="enable instruction trace"),
            "memory": Argument('-t', '--memory-trace', action='store_true',
                               help="enable memory tracing (slower)"),
            "internal_memory": Argument('-T', '--internal-memory-trace', action='store_true',
                                        help="enable internal memory tracing (slow)"),
            "reg_dump": Argument('-r', '--reg-dump', action='store_true',
                                 help="add register dump to instruction trace"),
            "labels": Argument('-B', '--labels', action='store_true',
                               help="add memory labels for detailed infos")
        }
    }
    ini_trafo = {
        "trace": {
            "instr": "instr_trace",
            "memory": "memory_trace",
            "internal_memory": "internal_memory_trace",
            "reg_dump": "reg_dump",
            "labels": "labels"
        }
    }
    Parser.__init__(self, def_cfg, arg_cfg,
                    "trace", "control low-level machine tracing",
                    ini_trafo, ini_prefix)
