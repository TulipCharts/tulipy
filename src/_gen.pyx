from collections import Counter

cimport ti

PYX_TEMPLATE = """
# This file is generated. Do not modify directly.

import __builtin__
from libc.limits cimport INT_MAX

import numpy as np
cimport numpy as np

cimport ti

TI_VERSION = ti.TI_VERSION
TI_BUILD   = ti.TI_BUILD

class InvalidOptionError(ValueError):
    pass

cdef dict _type_names = {{
    ti.TI_TYPE_OVERLAY:     'overlay',
    ti.TI_TYPE_INDICATOR:   'indicator',
    ti.TI_TYPE_MATH:        'math',
    ti.TI_TYPE_SIMPLE:      'simple',
    ti.TI_TYPE_COMPARATIVE: 'comparative',
}}

cdef class _Indicator:
    cdef const ti.ti_indicator_info * info

    cdef readonly const char * name
    cdef readonly const char * full_name
    cdef readonly const char * type

    def __init__(self, int index):
        assert 0 <= index < ti.TI_INDICATOR_COUNT

        self.info = ti.ti_indicators + index
        self.name = self.info.name
        self.full_name = self.info.full_name
        self.type = _type_names[self.info.type]

    @property
    def inputs(self):
        return [
            self.info.input_names[i]
            for i in range(self.info.inputs)
        ]

    @property
    def options(self):
        return [
            self.info.option_names[i]
            for i in range(self.info.options)
        ]

    @property
    def outputs(self):
        return [
            self.info.output_names[i]
            for i in range(self.info.outputs)
        ]

    def __repr__(self):
        return "{{}}:{{}}:{{}}".format(self.name, self.type, self.full_name)

    def _call(self, inputs, options):
        cdef int min_input_len = INT_MAX
        for i in range(self.info.inputs):
            min_input_len = __builtin__.min(min_input_len, inputs[i].shape[0])

        option_list = options if options else [0.0]
        cdef np.ndarray[np.float64_t, ndim=1, mode='c'] c_options = np.array(option_list)

        delta = self.info.start(&c_options[0])
        if min_input_len - delta < 0:
            # This would cause self.info.indicator to return ti.TI_INVALID_OPTION, but there would
            # be a problem before we got there in creating the `outputs` np.ndarray below with a
            # negative dimension
            raise InvalidOptionError()

        cdef ti.TI_REAL * c_inputs[ti.TI_MAXINDPARAMS]
        cdef np.ndarray[np.float64_t, ndim=1, mode='c'] input_ref

        for i in range(self.info.inputs):
            input_ref = inputs[i][-min_input_len:]
            c_inputs[i] = &input_ref[0]

        cdef ti.TI_REAL * c_outputs[ti.TI_MAXINDPARAMS]
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] outputs = np.empty((self.info.outputs, min_input_len - delta))
        for i in range(self.info.outputs):
            c_outputs[i] = &outputs[i,0]

        ret = self.info.indicator(min_input_len, c_inputs, &c_options[0], c_outputs)
        if ret == ti.TI_INVALID_OPTION:
            raise InvalidOptionError()

        return {{
            self.info.output_names[i]: outputs[i]
            for i in range(self.info.outputs)
        }}

{indicators}
"""


INDICATOR_TEMPLATE = """
class _Indicator_{name}(_Indicator):
    \"\"\"
    {full_name}
    \"\"\"
    def __init__(self):
        _Indicator.__init__(self, {index})

    def __call__(self, {inputs}{sep}{options}):
        return self._call([{inputs}], [{options}])

{name} = _Indicator_{name}()
"""


PARAMS_TEMPLATE = "{inputs}{sep}{options}"

def clean(names):
    c = Counter()

    for n in names:
        n = n.replace(' ', '_').replace('%', 'pct_')
        c[n] += 1
        if c[n] > 1:
            yield "{}{}".format(n, c[n])
        else:
            yield n


def gen(tulipy_pyx):
    indicators = []

    for i in range(ti.TI_INDICATOR_COUNT):
        info = ti.ti_indicators[i]

        indicators.append(INDICATOR_TEMPLATE.format(
            index=i,
            name=info.name,
            full_name=info.full_name,
            inputs=', '.join(clean([info.input_names[j] for j in range(info.inputs)])),
            sep=', ' if info.options else '',
            options=', '.join(clean([info.option_names[j] for j in range(info.options)])),
        ))

    tulipy_pyx.write(PYX_TEMPLATE.format(
        indicators='\n'.join(indicators)
    ))

