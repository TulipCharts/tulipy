from libc.limits cimport INT_MAX

import numpy as np
cimport numpy as np

cimport ti

TI_VERSION = ti.TI_VERSION
TI_BUILD   = ti.TI_BUILD

class InvalidOptionError(ValueError):
    pass

cdef dict _type_names = {
    ti.TI_TYPE_OVERLAY:     'overlay',
    ti.TI_TYPE_INDICATOR:   'indicator',
    ti.TI_TYPE_MATH:        'math',
    ti.TI_TYPE_SIMPLE:      'simple',
    ti.TI_TYPE_COMPARATIVE: 'comparative',
}

cdef class _Indicator:
    cdef const ti.ti_indicator_info * info

    cdef readonly const char * name
    cdef readonly const char * full_name
    cdef readonly const char * type

    def __cinit__(self, int index):
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
        return "{}:{}:{}".format(self.name, self.type, self.full_name)

    def __call__(self, inputs, options={}):
        cdef int min_input_len = INT_MAX
        for i in range(self.info.inputs):
            min_input_len = min(min_input_len, inputs[self.info.input_names[i]].shape[0])

        option_list = [options[self.info.option_names[i]] for i in range(self.info.options)] \
                      if options else [0.0]
        cdef np.ndarray[np.float64_t, ndim=1, mode='c'] c_options = np.array(option_list)

        delta = self.info.start(&c_options[0])

        cdef ti.TI_REAL * c_inputs[ti.TI_MAXINDPARAMS]
        cdef np.ndarray[np.float64_t, ndim=1, mode='c'] input_ref

        for i in range(self.info.inputs):
            input_ref = inputs[self.info.input_names[i]][-min_input_len:]
            c_inputs[i] = &input_ref[0]

        cdef ti.TI_REAL * c_outputs[ti.TI_MAXINDPARAMS]
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] outputs = np.empty((self.info.outputs, min_input_len - delta))
        for i in range(self.info.outputs):
            c_outputs[i] = &outputs[i,0]

        ret = self.info.indicator(min_input_len, c_inputs, &c_options[0], c_outputs)
        if ret == ti.TI_INVALID_OPTION:
            raise InvalidOptionError()

        return {
            self.info.output_names[i]: outputs[i]
            for i in range(self.info.outputs)
        }

cdef _init_module():
    for i in range(ti.TI_INDICATOR_COUNT):
        info = ti.ti_indicators[i]

        indicator = _Indicator(i)
        globals()[info.name] = indicator

_init_module()

