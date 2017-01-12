from libc.stdint cimport uint64_t

cdef extern from "indicators.h":
    ctypedef double TI_REAL

    ctypedef TI_REAL*  options_t "TI_REAL const *"
    ctypedef TI_REAL** inputs_t  "TI_REAL const * const *"
    ctypedef TI_REAL** outputs_t "TI_REAL * const *"

    cdef const char *   TI_VERSION
    cdef const uint64_t TI_BUILD

    enum: TI_INDICATOR_COUNT # Total number of indicators

    enum: TI_OKAY
    enum: TI_INVALID_OPTION

    enum: TI_TYPE_OVERLAY     # These have roughly the same range as the input data.
    enum: TI_TYPE_INDICATOR   # Everything else (e.g. oscillators).
    enum: TI_TYPE_MATH        # These aren't so good for plotting, but are useful with formulas.
    enum: TI_TYPE_SIMPLE      # These apply a simple operator (e.g. addition, sin, sqrt).
    enum: TI_TYPE_COMPARATIVE # These are designed to take inputs from different securities. i.e. compare stock A to stock B.

    enum: TI_MAXINDPARAMS # No indicator will use more than this many inputs, options, or outputs.

    ctypedef int (*ti_indicator_start_function)(options_t options)
    ctypedef int (*ti_indicator_function)(int size,
                                          inputs_t inputs,
                                          options_t options,
                                          outputs_t outputs)

    ctypedef struct ti_indicator_info:
        const char * name
        const char * full_name;
        ti_indicator_start_function start
        ti_indicator_function indicator
        int type
        int inputs
        int options
        int outputs
        const char * input_names[TI_MAXINDPARAMS]
        const char * option_names[TI_MAXINDPARAMS]
        const char * output_names[TI_MAXINDPARAMS]

    ti_indicator_info ti_indicators[]

    const ti_indicator_info * ti_find_indicator(const char * name)

