

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

from . import lib
from .lib import TI_BUILD, InvalidOptionError

TI_VERSION = lib.TI_VERSION.decode()


def abs(real):
    """
    Vector Absolute Value
    """

    return lib.abs([real], [])

abs.full_name = lib.abs.full_name.decode()
abs.type = lib.abs.type.decode()
abs.inputs = [x.decode() for x in lib.abs.inputs]
abs.options = [x.decode() for x in lib.abs.options]
abs.outputs = [x.decode() for x in lib.abs.outputs]


def acos(real):
    """
    Vector Arccosine
    """

    return lib.acos([real], [])

acos.full_name = lib.acos.full_name.decode()
acos.type = lib.acos.type.decode()
acos.inputs = [x.decode() for x in lib.acos.inputs]
acos.options = [x.decode() for x in lib.acos.options]
acos.outputs = [x.decode() for x in lib.acos.outputs]


def ad(high, low, close, volume):
    """
    Accumulation/Distribution Line
    """

    return lib.ad([high, low, close, volume], [])

ad.full_name = lib.ad.full_name.decode()
ad.type = lib.ad.type.decode()
ad.inputs = [x.decode() for x in lib.ad.inputs]
ad.options = [x.decode() for x in lib.ad.options]
ad.outputs = [x.decode() for x in lib.ad.outputs]


def add(real, real2):
    """
    Vector Addition
    """

    return lib.add([real, real2], [])

add.full_name = lib.add.full_name.decode()
add.type = lib.add.type.decode()
add.inputs = [x.decode() for x in lib.add.inputs]
add.options = [x.decode() for x in lib.add.options]
add.outputs = [x.decode() for x in lib.add.outputs]


def adosc(high, low, close, volume, short_period, long_period):
    """
    Accumulation/Distribution Oscillator
    """

    return lib.adosc([high, low, close, volume], [short_period, long_period])

adosc.full_name = lib.adosc.full_name.decode()
adosc.type = lib.adosc.type.decode()
adosc.inputs = [x.decode() for x in lib.adosc.inputs]
adosc.options = [x.decode() for x in lib.adosc.options]
adosc.outputs = [x.decode() for x in lib.adosc.outputs]


def adx(high, low, close, period):
    """
    Average Directional Movement Index
    """

    return lib.adx([high, low, close], [period])

adx.full_name = lib.adx.full_name.decode()
adx.type = lib.adx.type.decode()
adx.inputs = [x.decode() for x in lib.adx.inputs]
adx.options = [x.decode() for x in lib.adx.options]
adx.outputs = [x.decode() for x in lib.adx.outputs]


def adxr(high, low, close, period):
    """
    Average Directional Movement Rating
    """

    return lib.adxr([high, low, close], [period])

adxr.full_name = lib.adxr.full_name.decode()
adxr.type = lib.adxr.type.decode()
adxr.inputs = [x.decode() for x in lib.adxr.inputs]
adxr.options = [x.decode() for x in lib.adxr.options]
adxr.outputs = [x.decode() for x in lib.adxr.outputs]


def ao(high, low):
    """
    Awesome Oscillator
    """

    return lib.ao([high, low], [])

ao.full_name = lib.ao.full_name.decode()
ao.type = lib.ao.type.decode()
ao.inputs = [x.decode() for x in lib.ao.inputs]
ao.options = [x.decode() for x in lib.ao.options]
ao.outputs = [x.decode() for x in lib.ao.outputs]


def apo(real, short_period, long_period):
    """
    Absolute Price Oscillator
    """

    return lib.apo([real], [short_period, long_period])

apo.full_name = lib.apo.full_name.decode()
apo.type = lib.apo.type.decode()
apo.inputs = [x.decode() for x in lib.apo.inputs]
apo.options = [x.decode() for x in lib.apo.options]
apo.outputs = [x.decode() for x in lib.apo.outputs]


def aroon(high, low, period):
    """
    Aroon
    """

    return lib.aroon([high, low], [period])

aroon.full_name = lib.aroon.full_name.decode()
aroon.type = lib.aroon.type.decode()
aroon.inputs = [x.decode() for x in lib.aroon.inputs]
aroon.options = [x.decode() for x in lib.aroon.options]
aroon.outputs = [x.decode() for x in lib.aroon.outputs]


def aroonosc(high, low, period):
    """
    Aroon Oscillator
    """

    return lib.aroonosc([high, low], [period])

aroonosc.full_name = lib.aroonosc.full_name.decode()
aroonosc.type = lib.aroonosc.type.decode()
aroonosc.inputs = [x.decode() for x in lib.aroonosc.inputs]
aroonosc.options = [x.decode() for x in lib.aroonosc.options]
aroonosc.outputs = [x.decode() for x in lib.aroonosc.outputs]


def asin(real):
    """
    Vector Arcsine
    """

    return lib.asin([real], [])

asin.full_name = lib.asin.full_name.decode()
asin.type = lib.asin.type.decode()
asin.inputs = [x.decode() for x in lib.asin.inputs]
asin.options = [x.decode() for x in lib.asin.options]
asin.outputs = [x.decode() for x in lib.asin.outputs]


def atan(real):
    """
    Vector Arctangent
    """

    return lib.atan([real], [])

atan.full_name = lib.atan.full_name.decode()
atan.type = lib.atan.type.decode()
atan.inputs = [x.decode() for x in lib.atan.inputs]
atan.options = [x.decode() for x in lib.atan.options]
atan.outputs = [x.decode() for x in lib.atan.outputs]


def atr(high, low, close, period):
    """
    Average True Range
    """

    return lib.atr([high, low, close], [period])

atr.full_name = lib.atr.full_name.decode()
atr.type = lib.atr.type.decode()
atr.inputs = [x.decode() for x in lib.atr.inputs]
atr.options = [x.decode() for x in lib.atr.options]
atr.outputs = [x.decode() for x in lib.atr.outputs]


def avgprice(open, high, low, close):
    """
    Average Price
    """

    return lib.avgprice([open, high, low, close], [])

avgprice.full_name = lib.avgprice.full_name.decode()
avgprice.type = lib.avgprice.type.decode()
avgprice.inputs = [x.decode() for x in lib.avgprice.inputs]
avgprice.options = [x.decode() for x in lib.avgprice.options]
avgprice.outputs = [x.decode() for x in lib.avgprice.outputs]


def bbands(real, period, stddev):
    """
    Bollinger Bands
    """

    return lib.bbands([real], [period, stddev])

bbands.full_name = lib.bbands.full_name.decode()
bbands.type = lib.bbands.type.decode()
bbands.inputs = [x.decode() for x in lib.bbands.inputs]
bbands.options = [x.decode() for x in lib.bbands.options]
bbands.outputs = [x.decode() for x in lib.bbands.outputs]


def bop(open, high, low, close):
    """
    Balance of Power
    """

    return lib.bop([open, high, low, close], [])

bop.full_name = lib.bop.full_name.decode()
bop.type = lib.bop.type.decode()
bop.inputs = [x.decode() for x in lib.bop.inputs]
bop.options = [x.decode() for x in lib.bop.options]
bop.outputs = [x.decode() for x in lib.bop.outputs]


def cci(high, low, close, period):
    """
    Commodity Channel Index
    """

    return lib.cci([high, low, close], [period])

cci.full_name = lib.cci.full_name.decode()
cci.type = lib.cci.type.decode()
cci.inputs = [x.decode() for x in lib.cci.inputs]
cci.options = [x.decode() for x in lib.cci.options]
cci.outputs = [x.decode() for x in lib.cci.outputs]


def ceil(real):
    """
    Vector Ceiling
    """

    return lib.ceil([real], [])

ceil.full_name = lib.ceil.full_name.decode()
ceil.type = lib.ceil.type.decode()
ceil.inputs = [x.decode() for x in lib.ceil.inputs]
ceil.options = [x.decode() for x in lib.ceil.options]
ceil.outputs = [x.decode() for x in lib.ceil.outputs]


def cmo(real, period):
    """
    Chande Momentum Oscillator
    """

    return lib.cmo([real], [period])

cmo.full_name = lib.cmo.full_name.decode()
cmo.type = lib.cmo.type.decode()
cmo.inputs = [x.decode() for x in lib.cmo.inputs]
cmo.options = [x.decode() for x in lib.cmo.options]
cmo.outputs = [x.decode() for x in lib.cmo.outputs]


def cos(real):
    """
    Vector Cosine
    """

    return lib.cos([real], [])

cos.full_name = lib.cos.full_name.decode()
cos.type = lib.cos.type.decode()
cos.inputs = [x.decode() for x in lib.cos.inputs]
cos.options = [x.decode() for x in lib.cos.options]
cos.outputs = [x.decode() for x in lib.cos.outputs]


def cosh(real):
    """
    Vector Hyperbolic Cosine
    """

    return lib.cosh([real], [])

cosh.full_name = lib.cosh.full_name.decode()
cosh.type = lib.cosh.type.decode()
cosh.inputs = [x.decode() for x in lib.cosh.inputs]
cosh.options = [x.decode() for x in lib.cosh.options]
cosh.outputs = [x.decode() for x in lib.cosh.outputs]


def crossany(real, real2):
    """
    Crossany
    """

    return lib.crossany([real, real2], [])

crossany.full_name = lib.crossany.full_name.decode()
crossany.type = lib.crossany.type.decode()
crossany.inputs = [x.decode() for x in lib.crossany.inputs]
crossany.options = [x.decode() for x in lib.crossany.options]
crossany.outputs = [x.decode() for x in lib.crossany.outputs]


def crossover(real, real2):
    """
    Crossover
    """

    return lib.crossover([real, real2], [])

crossover.full_name = lib.crossover.full_name.decode()
crossover.type = lib.crossover.type.decode()
crossover.inputs = [x.decode() for x in lib.crossover.inputs]
crossover.options = [x.decode() for x in lib.crossover.options]
crossover.outputs = [x.decode() for x in lib.crossover.outputs]


def cvi(high, low, period):
    """
    Chaikins Volatility
    """

    return lib.cvi([high, low], [period])

cvi.full_name = lib.cvi.full_name.decode()
cvi.type = lib.cvi.type.decode()
cvi.inputs = [x.decode() for x in lib.cvi.inputs]
cvi.options = [x.decode() for x in lib.cvi.options]
cvi.outputs = [x.decode() for x in lib.cvi.outputs]


def decay(real, period):
    """
    Linear Decay
    """

    return lib.decay([real], [period])

decay.full_name = lib.decay.full_name.decode()
decay.type = lib.decay.type.decode()
decay.inputs = [x.decode() for x in lib.decay.inputs]
decay.options = [x.decode() for x in lib.decay.options]
decay.outputs = [x.decode() for x in lib.decay.outputs]


def dema(real, period):
    """
    Double Exponential Moving Average
    """

    return lib.dema([real], [period])

dema.full_name = lib.dema.full_name.decode()
dema.type = lib.dema.type.decode()
dema.inputs = [x.decode() for x in lib.dema.inputs]
dema.options = [x.decode() for x in lib.dema.options]
dema.outputs = [x.decode() for x in lib.dema.outputs]


def di(high, low, close, period):
    """
    Directional Indicator
    """

    return lib.di([high, low, close], [period])

di.full_name = lib.di.full_name.decode()
di.type = lib.di.type.decode()
di.inputs = [x.decode() for x in lib.di.inputs]
di.options = [x.decode() for x in lib.di.options]
di.outputs = [x.decode() for x in lib.di.outputs]


def div(real, real2):
    """
    Vector Division
    """

    return lib.div([real, real2], [])

div.full_name = lib.div.full_name.decode()
div.type = lib.div.type.decode()
div.inputs = [x.decode() for x in lib.div.inputs]
div.options = [x.decode() for x in lib.div.options]
div.outputs = [x.decode() for x in lib.div.outputs]


def dm(high, low, period):
    """
    Directional Movement
    """

    return lib.dm([high, low], [period])

dm.full_name = lib.dm.full_name.decode()
dm.type = lib.dm.type.decode()
dm.inputs = [x.decode() for x in lib.dm.inputs]
dm.options = [x.decode() for x in lib.dm.options]
dm.outputs = [x.decode() for x in lib.dm.outputs]


def dpo(real, period):
    """
    Detrended Price Oscillator
    """

    return lib.dpo([real], [period])

dpo.full_name = lib.dpo.full_name.decode()
dpo.type = lib.dpo.type.decode()
dpo.inputs = [x.decode() for x in lib.dpo.inputs]
dpo.options = [x.decode() for x in lib.dpo.options]
dpo.outputs = [x.decode() for x in lib.dpo.outputs]


def dx(high, low, close, period):
    """
    Directional Movement Index
    """

    return lib.dx([high, low, close], [period])

dx.full_name = lib.dx.full_name.decode()
dx.type = lib.dx.type.decode()
dx.inputs = [x.decode() for x in lib.dx.inputs]
dx.options = [x.decode() for x in lib.dx.options]
dx.outputs = [x.decode() for x in lib.dx.outputs]


def edecay(real, period):
    """
    Exponential Decay
    """

    return lib.edecay([real], [period])

edecay.full_name = lib.edecay.full_name.decode()
edecay.type = lib.edecay.type.decode()
edecay.inputs = [x.decode() for x in lib.edecay.inputs]
edecay.options = [x.decode() for x in lib.edecay.options]
edecay.outputs = [x.decode() for x in lib.edecay.outputs]


def ema(real, period):
    """
    Exponential Moving Average
    """

    return lib.ema([real], [period])

ema.full_name = lib.ema.full_name.decode()
ema.type = lib.ema.type.decode()
ema.inputs = [x.decode() for x in lib.ema.inputs]
ema.options = [x.decode() for x in lib.ema.options]
ema.outputs = [x.decode() for x in lib.ema.outputs]


def emv(high, low, volume):
    """
    Ease of Movement
    """

    return lib.emv([high, low, volume], [])

emv.full_name = lib.emv.full_name.decode()
emv.type = lib.emv.type.decode()
emv.inputs = [x.decode() for x in lib.emv.inputs]
emv.options = [x.decode() for x in lib.emv.options]
emv.outputs = [x.decode() for x in lib.emv.outputs]


def exp(real):
    """
    Vector Exponential
    """

    return lib.exp([real], [])

exp.full_name = lib.exp.full_name.decode()
exp.type = lib.exp.type.decode()
exp.inputs = [x.decode() for x in lib.exp.inputs]
exp.options = [x.decode() for x in lib.exp.options]
exp.outputs = [x.decode() for x in lib.exp.outputs]


def fisher(high, low, period):
    """
    Fisher Transform
    """

    return lib.fisher([high, low], [period])

fisher.full_name = lib.fisher.full_name.decode()
fisher.type = lib.fisher.type.decode()
fisher.inputs = [x.decode() for x in lib.fisher.inputs]
fisher.options = [x.decode() for x in lib.fisher.options]
fisher.outputs = [x.decode() for x in lib.fisher.outputs]


def floor(real):
    """
    Vector Floor
    """

    return lib.floor([real], [])

floor.full_name = lib.floor.full_name.decode()
floor.type = lib.floor.type.decode()
floor.inputs = [x.decode() for x in lib.floor.inputs]
floor.options = [x.decode() for x in lib.floor.options]
floor.outputs = [x.decode() for x in lib.floor.outputs]


def fosc(real, period):
    """
    Forecast Oscillator
    """

    return lib.fosc([real], [period])

fosc.full_name = lib.fosc.full_name.decode()
fosc.type = lib.fosc.type.decode()
fosc.inputs = [x.decode() for x in lib.fosc.inputs]
fosc.options = [x.decode() for x in lib.fosc.options]
fosc.outputs = [x.decode() for x in lib.fosc.outputs]


def hma(real, period):
    """
    Hull Moving Average
    """

    return lib.hma([real], [period])

hma.full_name = lib.hma.full_name.decode()
hma.type = lib.hma.type.decode()
hma.inputs = [x.decode() for x in lib.hma.inputs]
hma.options = [x.decode() for x in lib.hma.options]
hma.outputs = [x.decode() for x in lib.hma.outputs]


def kama(real, period):
    """
    Kaufman Adaptive Moving Average
    """

    return lib.kama([real], [period])

kama.full_name = lib.kama.full_name.decode()
kama.type = lib.kama.type.decode()
kama.inputs = [x.decode() for x in lib.kama.inputs]
kama.options = [x.decode() for x in lib.kama.options]
kama.outputs = [x.decode() for x in lib.kama.outputs]


def kvo(high, low, close, volume, short_period, long_period):
    """
    Klinger Volume Oscillator
    """

    return lib.kvo([high, low, close, volume], [short_period, long_period])

kvo.full_name = lib.kvo.full_name.decode()
kvo.type = lib.kvo.type.decode()
kvo.inputs = [x.decode() for x in lib.kvo.inputs]
kvo.options = [x.decode() for x in lib.kvo.options]
kvo.outputs = [x.decode() for x in lib.kvo.outputs]


def lag(real, period):
    """
    Lag
    """

    return lib.lag([real], [period])

lag.full_name = lib.lag.full_name.decode()
lag.type = lib.lag.type.decode()
lag.inputs = [x.decode() for x in lib.lag.inputs]
lag.options = [x.decode() for x in lib.lag.options]
lag.outputs = [x.decode() for x in lib.lag.outputs]


def linreg(real, period):
    """
    Linear Regression
    """

    return lib.linreg([real], [period])

linreg.full_name = lib.linreg.full_name.decode()
linreg.type = lib.linreg.type.decode()
linreg.inputs = [x.decode() for x in lib.linreg.inputs]
linreg.options = [x.decode() for x in lib.linreg.options]
linreg.outputs = [x.decode() for x in lib.linreg.outputs]


def linregintercept(real, period):
    """
    Linear Regression Intercept
    """

    return lib.linregintercept([real], [period])

linregintercept.full_name = lib.linregintercept.full_name.decode()
linregintercept.type = lib.linregintercept.type.decode()
linregintercept.inputs = [x.decode() for x in lib.linregintercept.inputs]
linregintercept.options = [x.decode() for x in lib.linregintercept.options]
linregintercept.outputs = [x.decode() for x in lib.linregintercept.outputs]


def linregslope(real, period):
    """
    Linear Regression Slope
    """

    return lib.linregslope([real], [period])

linregslope.full_name = lib.linregslope.full_name.decode()
linregslope.type = lib.linregslope.type.decode()
linregslope.inputs = [x.decode() for x in lib.linregslope.inputs]
linregslope.options = [x.decode() for x in lib.linregslope.options]
linregslope.outputs = [x.decode() for x in lib.linregslope.outputs]


def ln(real):
    """
    Vector Natural Log
    """

    return lib.ln([real], [])

ln.full_name = lib.ln.full_name.decode()
ln.type = lib.ln.type.decode()
ln.inputs = [x.decode() for x in lib.ln.inputs]
ln.options = [x.decode() for x in lib.ln.options]
ln.outputs = [x.decode() for x in lib.ln.outputs]


def log10(real):
    """
    Vector Base-10 Log
    """

    return lib.log10([real], [])

log10.full_name = lib.log10.full_name.decode()
log10.type = lib.log10.type.decode()
log10.inputs = [x.decode() for x in lib.log10.inputs]
log10.options = [x.decode() for x in lib.log10.options]
log10.outputs = [x.decode() for x in lib.log10.outputs]


def macd(real, short_period, long_period, signal_period):
    """
    Moving Average Convergence/Divergence
    """

    return lib.macd([real], [short_period, long_period, signal_period])

macd.full_name = lib.macd.full_name.decode()
macd.type = lib.macd.type.decode()
macd.inputs = [x.decode() for x in lib.macd.inputs]
macd.options = [x.decode() for x in lib.macd.options]
macd.outputs = [x.decode() for x in lib.macd.outputs]


def marketfi(high, low, volume):
    """
    Market Facilitation Index
    """

    return lib.marketfi([high, low, volume], [])

marketfi.full_name = lib.marketfi.full_name.decode()
marketfi.type = lib.marketfi.type.decode()
marketfi.inputs = [x.decode() for x in lib.marketfi.inputs]
marketfi.options = [x.decode() for x in lib.marketfi.options]
marketfi.outputs = [x.decode() for x in lib.marketfi.outputs]


def mass(high, low, period):
    """
    Mass Index
    """

    return lib.mass([high, low], [period])

mass.full_name = lib.mass.full_name.decode()
mass.type = lib.mass.type.decode()
mass.inputs = [x.decode() for x in lib.mass.inputs]
mass.options = [x.decode() for x in lib.mass.options]
mass.outputs = [x.decode() for x in lib.mass.outputs]


def max(real, period):
    """
    Maximum In Period
    """

    return lib.max([real], [period])

max.full_name = lib.max.full_name.decode()
max.type = lib.max.type.decode()
max.inputs = [x.decode() for x in lib.max.inputs]
max.options = [x.decode() for x in lib.max.options]
max.outputs = [x.decode() for x in lib.max.outputs]


def md(real, period):
    """
    Mean Deviation Over Period
    """

    return lib.md([real], [period])

md.full_name = lib.md.full_name.decode()
md.type = lib.md.type.decode()
md.inputs = [x.decode() for x in lib.md.inputs]
md.options = [x.decode() for x in lib.md.options]
md.outputs = [x.decode() for x in lib.md.outputs]


def medprice(high, low):
    """
    Median Price
    """

    return lib.medprice([high, low], [])

medprice.full_name = lib.medprice.full_name.decode()
medprice.type = lib.medprice.type.decode()
medprice.inputs = [x.decode() for x in lib.medprice.inputs]
medprice.options = [x.decode() for x in lib.medprice.options]
medprice.outputs = [x.decode() for x in lib.medprice.outputs]


def mfi(high, low, close, volume, period):
    """
    Money Flow Index
    """

    return lib.mfi([high, low, close, volume], [period])

mfi.full_name = lib.mfi.full_name.decode()
mfi.type = lib.mfi.type.decode()
mfi.inputs = [x.decode() for x in lib.mfi.inputs]
mfi.options = [x.decode() for x in lib.mfi.options]
mfi.outputs = [x.decode() for x in lib.mfi.outputs]


def min(real, period):
    """
    Minimum In Period
    """

    return lib.min([real], [period])

min.full_name = lib.min.full_name.decode()
min.type = lib.min.type.decode()
min.inputs = [x.decode() for x in lib.min.inputs]
min.options = [x.decode() for x in lib.min.options]
min.outputs = [x.decode() for x in lib.min.outputs]


def mom(real, period):
    """
    Momentum
    """

    return lib.mom([real], [period])

mom.full_name = lib.mom.full_name.decode()
mom.type = lib.mom.type.decode()
mom.inputs = [x.decode() for x in lib.mom.inputs]
mom.options = [x.decode() for x in lib.mom.options]
mom.outputs = [x.decode() for x in lib.mom.outputs]


def msw(real, period):
    """
    Mesa Sine Wave
    """

    return lib.msw([real], [period])

msw.full_name = lib.msw.full_name.decode()
msw.type = lib.msw.type.decode()
msw.inputs = [x.decode() for x in lib.msw.inputs]
msw.options = [x.decode() for x in lib.msw.options]
msw.outputs = [x.decode() for x in lib.msw.outputs]


def mul(real, real2):
    """
    Vector Multiplication
    """

    return lib.mul([real, real2], [])

mul.full_name = lib.mul.full_name.decode()
mul.type = lib.mul.type.decode()
mul.inputs = [x.decode() for x in lib.mul.inputs]
mul.options = [x.decode() for x in lib.mul.options]
mul.outputs = [x.decode() for x in lib.mul.outputs]


def natr(high, low, close, period):
    """
    Normalized Average True Range
    """

    return lib.natr([high, low, close], [period])

natr.full_name = lib.natr.full_name.decode()
natr.type = lib.natr.type.decode()
natr.inputs = [x.decode() for x in lib.natr.inputs]
natr.options = [x.decode() for x in lib.natr.options]
natr.outputs = [x.decode() for x in lib.natr.outputs]


def nvi(close, volume):
    """
    Negative Volume Index
    """

    return lib.nvi([close, volume], [])

nvi.full_name = lib.nvi.full_name.decode()
nvi.type = lib.nvi.type.decode()
nvi.inputs = [x.decode() for x in lib.nvi.inputs]
nvi.options = [x.decode() for x in lib.nvi.options]
nvi.outputs = [x.decode() for x in lib.nvi.outputs]


def obv(close, volume):
    """
    On Balance Volume
    """

    return lib.obv([close, volume], [])

obv.full_name = lib.obv.full_name.decode()
obv.type = lib.obv.type.decode()
obv.inputs = [x.decode() for x in lib.obv.inputs]
obv.options = [x.decode() for x in lib.obv.options]
obv.outputs = [x.decode() for x in lib.obv.outputs]


def ppo(real, short_period, long_period):
    """
    Percentage Price Oscillator
    """

    return lib.ppo([real], [short_period, long_period])

ppo.full_name = lib.ppo.full_name.decode()
ppo.type = lib.ppo.type.decode()
ppo.inputs = [x.decode() for x in lib.ppo.inputs]
ppo.options = [x.decode() for x in lib.ppo.options]
ppo.outputs = [x.decode() for x in lib.ppo.outputs]


def psar(high, low, acceleration_factor_step, acceleration_factor_maximum):
    """
    Parabolic SAR
    """

    return lib.psar([high, low], [acceleration_factor_step, acceleration_factor_maximum])

psar.full_name = lib.psar.full_name.decode()
psar.type = lib.psar.type.decode()
psar.inputs = [x.decode() for x in lib.psar.inputs]
psar.options = [x.decode() for x in lib.psar.options]
psar.outputs = [x.decode() for x in lib.psar.outputs]


def pvi(close, volume):
    """
    Positive Volume Index
    """

    return lib.pvi([close, volume], [])

pvi.full_name = lib.pvi.full_name.decode()
pvi.type = lib.pvi.type.decode()
pvi.inputs = [x.decode() for x in lib.pvi.inputs]
pvi.options = [x.decode() for x in lib.pvi.options]
pvi.outputs = [x.decode() for x in lib.pvi.outputs]


def qstick(open, close, period):
    """
    Qstick
    """

    return lib.qstick([open, close], [period])

qstick.full_name = lib.qstick.full_name.decode()
qstick.type = lib.qstick.type.decode()
qstick.inputs = [x.decode() for x in lib.qstick.inputs]
qstick.options = [x.decode() for x in lib.qstick.options]
qstick.outputs = [x.decode() for x in lib.qstick.outputs]


def roc(real, period):
    """
    Rate of Change
    """

    return lib.roc([real], [period])

roc.full_name = lib.roc.full_name.decode()
roc.type = lib.roc.type.decode()
roc.inputs = [x.decode() for x in lib.roc.inputs]
roc.options = [x.decode() for x in lib.roc.options]
roc.outputs = [x.decode() for x in lib.roc.outputs]


def rocr(real, period):
    """
    Rate of Change Ratio
    """

    return lib.rocr([real], [period])

rocr.full_name = lib.rocr.full_name.decode()
rocr.type = lib.rocr.type.decode()
rocr.inputs = [x.decode() for x in lib.rocr.inputs]
rocr.options = [x.decode() for x in lib.rocr.options]
rocr.outputs = [x.decode() for x in lib.rocr.outputs]


def round(real):
    """
    Vector Round
    """

    return lib.round([real], [])

round.full_name = lib.round.full_name.decode()
round.type = lib.round.type.decode()
round.inputs = [x.decode() for x in lib.round.inputs]
round.options = [x.decode() for x in lib.round.options]
round.outputs = [x.decode() for x in lib.round.outputs]


def rsi(real, period):
    """
    Relative Strength Index
    """

    return lib.rsi([real], [period])

rsi.full_name = lib.rsi.full_name.decode()
rsi.type = lib.rsi.type.decode()
rsi.inputs = [x.decode() for x in lib.rsi.inputs]
rsi.options = [x.decode() for x in lib.rsi.options]
rsi.outputs = [x.decode() for x in lib.rsi.outputs]


def sin(real):
    """
    Vector Sine
    """

    return lib.sin([real], [])

sin.full_name = lib.sin.full_name.decode()
sin.type = lib.sin.type.decode()
sin.inputs = [x.decode() for x in lib.sin.inputs]
sin.options = [x.decode() for x in lib.sin.options]
sin.outputs = [x.decode() for x in lib.sin.outputs]


def sinh(real):
    """
    Vector Hyperbolic Sine
    """

    return lib.sinh([real], [])

sinh.full_name = lib.sinh.full_name.decode()
sinh.type = lib.sinh.type.decode()
sinh.inputs = [x.decode() for x in lib.sinh.inputs]
sinh.options = [x.decode() for x in lib.sinh.options]
sinh.outputs = [x.decode() for x in lib.sinh.outputs]


def sma(real, period):
    """
    Simple Moving Average
    """

    return lib.sma([real], [period])

sma.full_name = lib.sma.full_name.decode()
sma.type = lib.sma.type.decode()
sma.inputs = [x.decode() for x in lib.sma.inputs]
sma.options = [x.decode() for x in lib.sma.options]
sma.outputs = [x.decode() for x in lib.sma.outputs]


def sqrt(real):
    """
    Vector Square Root
    """

    return lib.sqrt([real], [])

sqrt.full_name = lib.sqrt.full_name.decode()
sqrt.type = lib.sqrt.type.decode()
sqrt.inputs = [x.decode() for x in lib.sqrt.inputs]
sqrt.options = [x.decode() for x in lib.sqrt.options]
sqrt.outputs = [x.decode() for x in lib.sqrt.outputs]


def stddev(real, period):
    """
    Standard Deviation Over Period
    """

    return lib.stddev([real], [period])

stddev.full_name = lib.stddev.full_name.decode()
stddev.type = lib.stddev.type.decode()
stddev.inputs = [x.decode() for x in lib.stddev.inputs]
stddev.options = [x.decode() for x in lib.stddev.options]
stddev.outputs = [x.decode() for x in lib.stddev.outputs]


def stderr(real, period):
    """
    Standard Error Over Period
    """

    return lib.stderr([real], [period])

stderr.full_name = lib.stderr.full_name.decode()
stderr.type = lib.stderr.type.decode()
stderr.inputs = [x.decode() for x in lib.stderr.inputs]
stderr.options = [x.decode() for x in lib.stderr.options]
stderr.outputs = [x.decode() for x in lib.stderr.outputs]


def stoch(high, low, close, pct_k_period, pct_k_slowing_period, pct_d_period):
    """
    Stochastic Oscillator
    """

    return lib.stoch([high, low, close], [pct_k_period, pct_k_slowing_period, pct_d_period])

stoch.full_name = lib.stoch.full_name.decode()
stoch.type = lib.stoch.type.decode()
stoch.inputs = [x.decode() for x in lib.stoch.inputs]
stoch.options = [x.decode() for x in lib.stoch.options]
stoch.outputs = [x.decode() for x in lib.stoch.outputs]


def stochrsi(real, period):
    """
    Stochastic RSI
    """

    return lib.stochrsi([real], [period])

stochrsi.full_name = lib.stochrsi.full_name.decode()
stochrsi.type = lib.stochrsi.type.decode()
stochrsi.inputs = [x.decode() for x in lib.stochrsi.inputs]
stochrsi.options = [x.decode() for x in lib.stochrsi.options]
stochrsi.outputs = [x.decode() for x in lib.stochrsi.outputs]


def sub(real, real2):
    """
    Vector Subtraction
    """

    return lib.sub([real, real2], [])

sub.full_name = lib.sub.full_name.decode()
sub.type = lib.sub.type.decode()
sub.inputs = [x.decode() for x in lib.sub.inputs]
sub.options = [x.decode() for x in lib.sub.options]
sub.outputs = [x.decode() for x in lib.sub.outputs]


def sum(real, period):
    """
    Sum Over Period
    """

    return lib.sum([real], [period])

sum.full_name = lib.sum.full_name.decode()
sum.type = lib.sum.type.decode()
sum.inputs = [x.decode() for x in lib.sum.inputs]
sum.options = [x.decode() for x in lib.sum.options]
sum.outputs = [x.decode() for x in lib.sum.outputs]


def tan(real):
    """
    Vector Tangent
    """

    return lib.tan([real], [])

tan.full_name = lib.tan.full_name.decode()
tan.type = lib.tan.type.decode()
tan.inputs = [x.decode() for x in lib.tan.inputs]
tan.options = [x.decode() for x in lib.tan.options]
tan.outputs = [x.decode() for x in lib.tan.outputs]


def tanh(real):
    """
    Vector Hyperbolic Tangent
    """

    return lib.tanh([real], [])

tanh.full_name = lib.tanh.full_name.decode()
tanh.type = lib.tanh.type.decode()
tanh.inputs = [x.decode() for x in lib.tanh.inputs]
tanh.options = [x.decode() for x in lib.tanh.options]
tanh.outputs = [x.decode() for x in lib.tanh.outputs]


def tema(real, period):
    """
    Triple Exponential Moving Average
    """

    return lib.tema([real], [period])

tema.full_name = lib.tema.full_name.decode()
tema.type = lib.tema.type.decode()
tema.inputs = [x.decode() for x in lib.tema.inputs]
tema.options = [x.decode() for x in lib.tema.options]
tema.outputs = [x.decode() for x in lib.tema.outputs]


def todeg(real):
    """
    Vector Degree Conversion
    """

    return lib.todeg([real], [])

todeg.full_name = lib.todeg.full_name.decode()
todeg.type = lib.todeg.type.decode()
todeg.inputs = [x.decode() for x in lib.todeg.inputs]
todeg.options = [x.decode() for x in lib.todeg.options]
todeg.outputs = [x.decode() for x in lib.todeg.outputs]


def torad(real):
    """
    Vector Radian Conversion
    """

    return lib.torad([real], [])

torad.full_name = lib.torad.full_name.decode()
torad.type = lib.torad.type.decode()
torad.inputs = [x.decode() for x in lib.torad.inputs]
torad.options = [x.decode() for x in lib.torad.options]
torad.outputs = [x.decode() for x in lib.torad.outputs]


def tr(high, low, close):
    """
    True Range
    """

    return lib.tr([high, low, close], [])

tr.full_name = lib.tr.full_name.decode()
tr.type = lib.tr.type.decode()
tr.inputs = [x.decode() for x in lib.tr.inputs]
tr.options = [x.decode() for x in lib.tr.options]
tr.outputs = [x.decode() for x in lib.tr.outputs]


def trima(real, period):
    """
    Triangular Moving Average
    """

    return lib.trima([real], [period])

trima.full_name = lib.trima.full_name.decode()
trima.type = lib.trima.type.decode()
trima.inputs = [x.decode() for x in lib.trima.inputs]
trima.options = [x.decode() for x in lib.trima.options]
trima.outputs = [x.decode() for x in lib.trima.outputs]


def trix(real, period):
    """
    Trix
    """

    return lib.trix([real], [period])

trix.full_name = lib.trix.full_name.decode()
trix.type = lib.trix.type.decode()
trix.inputs = [x.decode() for x in lib.trix.inputs]
trix.options = [x.decode() for x in lib.trix.options]
trix.outputs = [x.decode() for x in lib.trix.outputs]


def trunc(real):
    """
    Vector Truncate
    """

    return lib.trunc([real], [])

trunc.full_name = lib.trunc.full_name.decode()
trunc.type = lib.trunc.type.decode()
trunc.inputs = [x.decode() for x in lib.trunc.inputs]
trunc.options = [x.decode() for x in lib.trunc.options]
trunc.outputs = [x.decode() for x in lib.trunc.outputs]


def tsf(real, period):
    """
    Time Series Forecast
    """

    return lib.tsf([real], [period])

tsf.full_name = lib.tsf.full_name.decode()
tsf.type = lib.tsf.type.decode()
tsf.inputs = [x.decode() for x in lib.tsf.inputs]
tsf.options = [x.decode() for x in lib.tsf.options]
tsf.outputs = [x.decode() for x in lib.tsf.outputs]


def typprice(high, low, close):
    """
    Typical Price
    """

    return lib.typprice([high, low, close], [])

typprice.full_name = lib.typprice.full_name.decode()
typprice.type = lib.typprice.type.decode()
typprice.inputs = [x.decode() for x in lib.typprice.inputs]
typprice.options = [x.decode() for x in lib.typprice.options]
typprice.outputs = [x.decode() for x in lib.typprice.outputs]


def ultosc(high, low, close, short_period, medium_period, long_period):
    """
    Ultimate Oscillator
    """

    return lib.ultosc([high, low, close], [short_period, medium_period, long_period])

ultosc.full_name = lib.ultosc.full_name.decode()
ultosc.type = lib.ultosc.type.decode()
ultosc.inputs = [x.decode() for x in lib.ultosc.inputs]
ultosc.options = [x.decode() for x in lib.ultosc.options]
ultosc.outputs = [x.decode() for x in lib.ultosc.outputs]


def var(real, period):
    """
    Variance Over Period
    """

    return lib.var([real], [period])

var.full_name = lib.var.full_name.decode()
var.type = lib.var.type.decode()
var.inputs = [x.decode() for x in lib.var.inputs]
var.options = [x.decode() for x in lib.var.options]
var.outputs = [x.decode() for x in lib.var.outputs]


def vhf(real, period):
    """
    Vertical Horizontal Filter
    """

    return lib.vhf([real], [period])

vhf.full_name = lib.vhf.full_name.decode()
vhf.type = lib.vhf.type.decode()
vhf.inputs = [x.decode() for x in lib.vhf.inputs]
vhf.options = [x.decode() for x in lib.vhf.options]
vhf.outputs = [x.decode() for x in lib.vhf.outputs]


def vidya(real, short_period, long_period, alpha):
    """
    Variable Index Dynamic Average
    """

    return lib.vidya([real], [short_period, long_period, alpha])

vidya.full_name = lib.vidya.full_name.decode()
vidya.type = lib.vidya.type.decode()
vidya.inputs = [x.decode() for x in lib.vidya.inputs]
vidya.options = [x.decode() for x in lib.vidya.options]
vidya.outputs = [x.decode() for x in lib.vidya.outputs]


def volatility(real, period):
    """
    Annualized Historical Volatility
    """

    return lib.volatility([real], [period])

volatility.full_name = lib.volatility.full_name.decode()
volatility.type = lib.volatility.type.decode()
volatility.inputs = [x.decode() for x in lib.volatility.inputs]
volatility.options = [x.decode() for x in lib.volatility.options]
volatility.outputs = [x.decode() for x in lib.volatility.outputs]


def vosc(volume, short_period, long_period):
    """
    Volume Oscillator
    """

    return lib.vosc([volume], [short_period, long_period])

vosc.full_name = lib.vosc.full_name.decode()
vosc.type = lib.vosc.type.decode()
vosc.inputs = [x.decode() for x in lib.vosc.inputs]
vosc.options = [x.decode() for x in lib.vosc.options]
vosc.outputs = [x.decode() for x in lib.vosc.outputs]


def vwma(close, volume, period):
    """
    Volume Weighted Moving Average
    """

    return lib.vwma([close, volume], [period])

vwma.full_name = lib.vwma.full_name.decode()
vwma.type = lib.vwma.type.decode()
vwma.inputs = [x.decode() for x in lib.vwma.inputs]
vwma.options = [x.decode() for x in lib.vwma.options]
vwma.outputs = [x.decode() for x in lib.vwma.outputs]


def wad(high, low, close):
    """
    Williams Accumulation/Distribution
    """

    return lib.wad([high, low, close], [])

wad.full_name = lib.wad.full_name.decode()
wad.type = lib.wad.type.decode()
wad.inputs = [x.decode() for x in lib.wad.inputs]
wad.options = [x.decode() for x in lib.wad.options]
wad.outputs = [x.decode() for x in lib.wad.outputs]


def wcprice(high, low, close):
    """
    Weighted Close Price
    """

    return lib.wcprice([high, low, close], [])

wcprice.full_name = lib.wcprice.full_name.decode()
wcprice.type = lib.wcprice.type.decode()
wcprice.inputs = [x.decode() for x in lib.wcprice.inputs]
wcprice.options = [x.decode() for x in lib.wcprice.options]
wcprice.outputs = [x.decode() for x in lib.wcprice.outputs]


def wilders(real, period):
    """
    Wilders Smoothing
    """

    return lib.wilders([real], [period])

wilders.full_name = lib.wilders.full_name.decode()
wilders.type = lib.wilders.type.decode()
wilders.inputs = [x.decode() for x in lib.wilders.inputs]
wilders.options = [x.decode() for x in lib.wilders.options]
wilders.outputs = [x.decode() for x in lib.wilders.outputs]


def willr(high, low, close, period):
    """
    Williams %R
    """

    return lib.willr([high, low, close], [period])

willr.full_name = lib.willr.full_name.decode()
willr.type = lib.willr.type.decode()
willr.inputs = [x.decode() for x in lib.willr.inputs]
willr.options = [x.decode() for x in lib.willr.options]
willr.outputs = [x.decode() for x in lib.willr.outputs]


def wma(real, period):
    """
    Weighted Moving Average
    """

    return lib.wma([real], [period])

wma.full_name = lib.wma.full_name.decode()
wma.type = lib.wma.type.decode()
wma.inputs = [x.decode() for x in lib.wma.inputs]
wma.options = [x.decode() for x in lib.wma.options]
wma.outputs = [x.decode() for x in lib.wma.outputs]


def zlema(real, period):
    """
    Zero-Lag Exponential Moving Average
    """

    return lib.zlema([real], [period])

zlema.full_name = lib.zlema.full_name.decode()
zlema.type = lib.zlema.type.decode()
zlema.inputs = [x.decode() for x in lib.zlema.inputs]
zlema.options = [x.decode() for x in lib.zlema.options]
zlema.outputs = [x.decode() for x in lib.zlema.outputs]

