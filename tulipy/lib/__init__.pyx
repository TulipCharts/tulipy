

# tulipy: Python bindings for Tulip Indicators
# https://github.com/cirla/tulipy
# Copyright (c) 2016 tulipy authors
# https://github.com/cirla/tulipy/blob/master/AUTHORS
#
# This file is part of tulipy: Python bindings for Tulip Indicators.
#
# tulipy is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# tulipy is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with tulipy.  If not, see <http://www.gnu.org/licenses/>.


# This file is generated. Do not modify directly.

# Alias builtins that are shadowed by indicators with the same name
try: # Python 3
    from builtins import min as builtin_min
except ImportError: # Python 2
    from __builtin__ import min as builtin_min

from libc.limits cimport INT_MAX

import numpy as np
cimport numpy as np

cimport ti

TI_VERSION = ti.TI_VERSION
TI_BUILD   = ti.TI_BUILD

class InvalidOptionError(ValueError):
    pass

class InvalidInputError(ValueError):
    pass

cdef dict _type_names = {
    ti.TI_TYPE_OVERLAY:     b'overlay',
    ti.TI_TYPE_INDICATOR:   b'indicator',
    ti.TI_TYPE_MATH:        b'math',
    ti.TI_TYPE_SIMPLE:      b'simple',
    ti.TI_TYPE_COMPARATIVE: b'comparative',
}

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

    def __call__(self, inputs, options):
        cdef int min_input_len = INT_MAX
        for i in range(self.info.inputs):
            min_input_len = builtin_min(min_input_len, inputs[i].shape[0])

        option_list = options if options else [0.0]
        cdef np.ndarray[np.float64_t, ndim=1, mode='c'] c_options = np.array(option_list, dtype=np.float64)

        delta = self.info.start(&c_options[0])
        if min_input_len - delta <= 0:
            # This would cause self.info.indicator to return ti.TI_INVALID_OPTION, but there would
            # be a problem before we got there in creating the `outputs` np.ndarray below with a
            # negative dimension
            raise InvalidOptionError()

        cdef ti.TI_REAL * c_inputs[ti.TI_MAXINDPARAMS]
        cdef np.ndarray[np.float64_t, ndim=1, mode='c'] input_ref

        for i in range(self.info.inputs):
            if inputs[i].dtype == np.float64:
                input_ref = inputs[i][-min_input_len:]
            elif np.issubdtype(inputs[i].dtype, np.number):
                input_ref = inputs[i][-min_input_len:].astype(np.float64)
            else:
                raise InvalidInputError("Input arrays must have a numeric dtype")
            input_ref = inputs[i][-min_input_len:]
            c_inputs[i] = &input_ref[0]

        cdef ti.TI_REAL * c_outputs[ti.TI_MAXINDPARAMS]
        cdef np.ndarray[np.float64_t, ndim=2, mode='c'] outputs = np.empty((self.info.outputs, min_input_len - delta))
        for i in range(self.info.outputs):
            c_outputs[i] = &outputs[i,0]

        ret = self.info.indicator(min_input_len, c_inputs, &c_options[0], c_outputs)
        if ret == ti.TI_INVALID_OPTION:
            raise InvalidOptionError()

        if self.info.outputs == 1:
            return outputs[0]

        return tuple(outputs)


abs = _Indicator(0)


acos = _Indicator(1)


ad = _Indicator(2)


add = _Indicator(3)


adosc = _Indicator(4)


adx = _Indicator(5)


adxr = _Indicator(6)


ao = _Indicator(7)


apo = _Indicator(8)


aroon = _Indicator(9)


aroonosc = _Indicator(10)


asin = _Indicator(11)


atan = _Indicator(12)


atr = _Indicator(13)


avgprice = _Indicator(14)


bbands = _Indicator(15)


bop = _Indicator(16)


cci = _Indicator(17)


ceil = _Indicator(18)


cmo = _Indicator(19)


cos = _Indicator(20)


cosh = _Indicator(21)


crossany = _Indicator(22)


crossover = _Indicator(23)


cvi = _Indicator(24)


decay = _Indicator(25)


dema = _Indicator(26)


di = _Indicator(27)


div = _Indicator(28)


dm = _Indicator(29)


dpo = _Indicator(30)


dx = _Indicator(31)


edecay = _Indicator(32)


ema = _Indicator(33)


emv = _Indicator(34)


exp = _Indicator(35)


fisher = _Indicator(36)


floor = _Indicator(37)


fosc = _Indicator(38)


hma = _Indicator(39)


kama = _Indicator(40)


kvo = _Indicator(41)


lag = _Indicator(42)


linreg = _Indicator(43)


linregintercept = _Indicator(44)


linregslope = _Indicator(45)


ln = _Indicator(46)


log10 = _Indicator(47)


macd = _Indicator(48)


marketfi = _Indicator(49)


mass = _Indicator(50)


max = _Indicator(51)


md = _Indicator(52)


medprice = _Indicator(53)


mfi = _Indicator(54)


min = _Indicator(55)


mom = _Indicator(56)


msw = _Indicator(57)


mul = _Indicator(58)


natr = _Indicator(59)


nvi = _Indicator(60)


obv = _Indicator(61)


ppo = _Indicator(62)


psar = _Indicator(63)


pvi = _Indicator(64)


qstick = _Indicator(65)


roc = _Indicator(66)


rocr = _Indicator(67)


round = _Indicator(68)


rsi = _Indicator(69)


sin = _Indicator(70)


sinh = _Indicator(71)


sma = _Indicator(72)


sqrt = _Indicator(73)


stddev = _Indicator(74)


stderr = _Indicator(75)


stoch = _Indicator(76)


stochrsi = _Indicator(77)


sub = _Indicator(78)


sum = _Indicator(79)


tan = _Indicator(80)


tanh = _Indicator(81)


tema = _Indicator(82)


todeg = _Indicator(83)


torad = _Indicator(84)


tr = _Indicator(85)


trima = _Indicator(86)


trix = _Indicator(87)


trunc = _Indicator(88)


tsf = _Indicator(89)


typprice = _Indicator(90)


ultosc = _Indicator(91)


var = _Indicator(92)


vhf = _Indicator(93)


vidya = _Indicator(94)


volatility = _Indicator(95)


vosc = _Indicator(96)


vwma = _Indicator(97)


wad = _Indicator(98)


wcprice = _Indicator(99)


wilders = _Indicator(100)


willr = _Indicator(101)


wma = _Indicator(102)


zlema = _Indicator(103)

