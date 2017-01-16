

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
from .lib import TI_VERSION, TI_BUILD, InvalidOptionError


def abs(real):
    """
    Vector Absolute Value
    """

    return lib.abs([real], [])

abs.full_name = lib.abs.full_name
abs.type = lib.abs.type
abs.inputs = lib.abs.inputs
abs.options = lib.abs.options
abs.outputs = lib.abs.outputs


def acos(real):
    """
    Vector Arccosine
    """

    return lib.acos([real], [])

acos.full_name = lib.acos.full_name
acos.type = lib.acos.type
acos.inputs = lib.acos.inputs
acos.options = lib.acos.options
acos.outputs = lib.acos.outputs


def ad(high, low, close, volume):
    """
    Accumulation/Distribution Line
    """

    return lib.ad([high, low, close, volume], [])

ad.full_name = lib.ad.full_name
ad.type = lib.ad.type
ad.inputs = lib.ad.inputs
ad.options = lib.ad.options
ad.outputs = lib.ad.outputs


def add(real, real2):
    """
    Vector Addition
    """

    return lib.add([real, real2], [])

add.full_name = lib.add.full_name
add.type = lib.add.type
add.inputs = lib.add.inputs
add.options = lib.add.options
add.outputs = lib.add.outputs


def adosc(high, low, close, volume, short_period, long_period):
    """
    Accumulation/Distribution Oscillator
    """

    return lib.adosc([high, low, close, volume], [short_period, long_period])

adosc.full_name = lib.adosc.full_name
adosc.type = lib.adosc.type
adosc.inputs = lib.adosc.inputs
adosc.options = lib.adosc.options
adosc.outputs = lib.adosc.outputs


def adx(high, low, close, period):
    """
    Average Directional Movement Index
    """

    return lib.adx([high, low, close], [period])

adx.full_name = lib.adx.full_name
adx.type = lib.adx.type
adx.inputs = lib.adx.inputs
adx.options = lib.adx.options
adx.outputs = lib.adx.outputs


def adxr(high, low, close, period):
    """
    Average Directional Movement Rating
    """

    return lib.adxr([high, low, close], [period])

adxr.full_name = lib.adxr.full_name
adxr.type = lib.adxr.type
adxr.inputs = lib.adxr.inputs
adxr.options = lib.adxr.options
adxr.outputs = lib.adxr.outputs


def ao(high, low):
    """
    Awesome Oscillator
    """

    return lib.ao([high, low], [])

ao.full_name = lib.ao.full_name
ao.type = lib.ao.type
ao.inputs = lib.ao.inputs
ao.options = lib.ao.options
ao.outputs = lib.ao.outputs


def apo(real, short_period, long_period):
    """
    Absolute Price Oscillator
    """

    return lib.apo([real], [short_period, long_period])

apo.full_name = lib.apo.full_name
apo.type = lib.apo.type
apo.inputs = lib.apo.inputs
apo.options = lib.apo.options
apo.outputs = lib.apo.outputs


def aroon(high, low, period):
    """
    Aroon
    """

    return lib.aroon([high, low], [period])

aroon.full_name = lib.aroon.full_name
aroon.type = lib.aroon.type
aroon.inputs = lib.aroon.inputs
aroon.options = lib.aroon.options
aroon.outputs = lib.aroon.outputs


def aroonosc(high, low, period):
    """
    Aroon Oscillator
    """

    return lib.aroonosc([high, low], [period])

aroonosc.full_name = lib.aroonosc.full_name
aroonosc.type = lib.aroonosc.type
aroonosc.inputs = lib.aroonosc.inputs
aroonosc.options = lib.aroonosc.options
aroonosc.outputs = lib.aroonosc.outputs


def asin(real):
    """
    Vector Arcsine
    """

    return lib.asin([real], [])

asin.full_name = lib.asin.full_name
asin.type = lib.asin.type
asin.inputs = lib.asin.inputs
asin.options = lib.asin.options
asin.outputs = lib.asin.outputs


def atan(real):
    """
    Vector Arctangent
    """

    return lib.atan([real], [])

atan.full_name = lib.atan.full_name
atan.type = lib.atan.type
atan.inputs = lib.atan.inputs
atan.options = lib.atan.options
atan.outputs = lib.atan.outputs


def atr(high, low, close, period):
    """
    Average True Range
    """

    return lib.atr([high, low, close], [period])

atr.full_name = lib.atr.full_name
atr.type = lib.atr.type
atr.inputs = lib.atr.inputs
atr.options = lib.atr.options
atr.outputs = lib.atr.outputs


def avgprice(open, high, low, close):
    """
    Average Price
    """

    return lib.avgprice([open, high, low, close], [])

avgprice.full_name = lib.avgprice.full_name
avgprice.type = lib.avgprice.type
avgprice.inputs = lib.avgprice.inputs
avgprice.options = lib.avgprice.options
avgprice.outputs = lib.avgprice.outputs


def bbands(real, period, stddev):
    """
    Bollinger Bands
    """

    return lib.bbands([real], [period, stddev])

bbands.full_name = lib.bbands.full_name
bbands.type = lib.bbands.type
bbands.inputs = lib.bbands.inputs
bbands.options = lib.bbands.options
bbands.outputs = lib.bbands.outputs


def bop(open, high, low, close):
    """
    Balance of Power
    """

    return lib.bop([open, high, low, close], [])

bop.full_name = lib.bop.full_name
bop.type = lib.bop.type
bop.inputs = lib.bop.inputs
bop.options = lib.bop.options
bop.outputs = lib.bop.outputs


def cci(high, low, close, period):
    """
    Commodity Channel Index
    """

    return lib.cci([high, low, close], [period])

cci.full_name = lib.cci.full_name
cci.type = lib.cci.type
cci.inputs = lib.cci.inputs
cci.options = lib.cci.options
cci.outputs = lib.cci.outputs


def ceil(real):
    """
    Vector Ceiling
    """

    return lib.ceil([real], [])

ceil.full_name = lib.ceil.full_name
ceil.type = lib.ceil.type
ceil.inputs = lib.ceil.inputs
ceil.options = lib.ceil.options
ceil.outputs = lib.ceil.outputs


def cmo(real, period):
    """
    Chande Momentum Oscillator
    """

    return lib.cmo([real], [period])

cmo.full_name = lib.cmo.full_name
cmo.type = lib.cmo.type
cmo.inputs = lib.cmo.inputs
cmo.options = lib.cmo.options
cmo.outputs = lib.cmo.outputs


def cos(real):
    """
    Vector Cosine
    """

    return lib.cos([real], [])

cos.full_name = lib.cos.full_name
cos.type = lib.cos.type
cos.inputs = lib.cos.inputs
cos.options = lib.cos.options
cos.outputs = lib.cos.outputs


def cosh(real):
    """
    Vector Hyperbolic Cosine
    """

    return lib.cosh([real], [])

cosh.full_name = lib.cosh.full_name
cosh.type = lib.cosh.type
cosh.inputs = lib.cosh.inputs
cosh.options = lib.cosh.options
cosh.outputs = lib.cosh.outputs


def crossany(real, real2):
    """
    Crossany
    """

    return lib.crossany([real, real2], [])

crossany.full_name = lib.crossany.full_name
crossany.type = lib.crossany.type
crossany.inputs = lib.crossany.inputs
crossany.options = lib.crossany.options
crossany.outputs = lib.crossany.outputs


def crossover(real, real2):
    """
    Crossover
    """

    return lib.crossover([real, real2], [])

crossover.full_name = lib.crossover.full_name
crossover.type = lib.crossover.type
crossover.inputs = lib.crossover.inputs
crossover.options = lib.crossover.options
crossover.outputs = lib.crossover.outputs


def cvi(high, low, period):
    """
    Chaikins Volatility
    """

    return lib.cvi([high, low], [period])

cvi.full_name = lib.cvi.full_name
cvi.type = lib.cvi.type
cvi.inputs = lib.cvi.inputs
cvi.options = lib.cvi.options
cvi.outputs = lib.cvi.outputs


def decay(real, period):
    """
    Linear Decay
    """

    return lib.decay([real], [period])

decay.full_name = lib.decay.full_name
decay.type = lib.decay.type
decay.inputs = lib.decay.inputs
decay.options = lib.decay.options
decay.outputs = lib.decay.outputs


def dema(real, period):
    """
    Double Exponential Moving Average
    """

    return lib.dema([real], [period])

dema.full_name = lib.dema.full_name
dema.type = lib.dema.type
dema.inputs = lib.dema.inputs
dema.options = lib.dema.options
dema.outputs = lib.dema.outputs


def di(high, low, close, period):
    """
    Directional Indicator
    """

    return lib.di([high, low, close], [period])

di.full_name = lib.di.full_name
di.type = lib.di.type
di.inputs = lib.di.inputs
di.options = lib.di.options
di.outputs = lib.di.outputs


def div(real, real2):
    """
    Vector Division
    """

    return lib.div([real, real2], [])

div.full_name = lib.div.full_name
div.type = lib.div.type
div.inputs = lib.div.inputs
div.options = lib.div.options
div.outputs = lib.div.outputs


def dm(high, low, period):
    """
    Directional Movement
    """

    return lib.dm([high, low], [period])

dm.full_name = lib.dm.full_name
dm.type = lib.dm.type
dm.inputs = lib.dm.inputs
dm.options = lib.dm.options
dm.outputs = lib.dm.outputs


def dpo(real, period):
    """
    Detrended Price Oscillator
    """

    return lib.dpo([real], [period])

dpo.full_name = lib.dpo.full_name
dpo.type = lib.dpo.type
dpo.inputs = lib.dpo.inputs
dpo.options = lib.dpo.options
dpo.outputs = lib.dpo.outputs


def dx(high, low, close, period):
    """
    Directional Movement Index
    """

    return lib.dx([high, low, close], [period])

dx.full_name = lib.dx.full_name
dx.type = lib.dx.type
dx.inputs = lib.dx.inputs
dx.options = lib.dx.options
dx.outputs = lib.dx.outputs


def edecay(real, period):
    """
    Exponential Decay
    """

    return lib.edecay([real], [period])

edecay.full_name = lib.edecay.full_name
edecay.type = lib.edecay.type
edecay.inputs = lib.edecay.inputs
edecay.options = lib.edecay.options
edecay.outputs = lib.edecay.outputs


def ema(real, period):
    """
    Exponential Moving Average
    """

    return lib.ema([real], [period])

ema.full_name = lib.ema.full_name
ema.type = lib.ema.type
ema.inputs = lib.ema.inputs
ema.options = lib.ema.options
ema.outputs = lib.ema.outputs


def emv(high, low, volume):
    """
    Ease of Movement
    """

    return lib.emv([high, low, volume], [])

emv.full_name = lib.emv.full_name
emv.type = lib.emv.type
emv.inputs = lib.emv.inputs
emv.options = lib.emv.options
emv.outputs = lib.emv.outputs


def exp(real):
    """
    Vector Exponential
    """

    return lib.exp([real], [])

exp.full_name = lib.exp.full_name
exp.type = lib.exp.type
exp.inputs = lib.exp.inputs
exp.options = lib.exp.options
exp.outputs = lib.exp.outputs


def fisher(high, low, period):
    """
    Fisher Transform
    """

    return lib.fisher([high, low], [period])

fisher.full_name = lib.fisher.full_name
fisher.type = lib.fisher.type
fisher.inputs = lib.fisher.inputs
fisher.options = lib.fisher.options
fisher.outputs = lib.fisher.outputs


def floor(real):
    """
    Vector Floor
    """

    return lib.floor([real], [])

floor.full_name = lib.floor.full_name
floor.type = lib.floor.type
floor.inputs = lib.floor.inputs
floor.options = lib.floor.options
floor.outputs = lib.floor.outputs


def fosc(real, period):
    """
    Forecast Oscillator
    """

    return lib.fosc([real], [period])

fosc.full_name = lib.fosc.full_name
fosc.type = lib.fosc.type
fosc.inputs = lib.fosc.inputs
fosc.options = lib.fosc.options
fosc.outputs = lib.fosc.outputs


def hma(real, period):
    """
    Hull Moving Average
    """

    return lib.hma([real], [period])

hma.full_name = lib.hma.full_name
hma.type = lib.hma.type
hma.inputs = lib.hma.inputs
hma.options = lib.hma.options
hma.outputs = lib.hma.outputs


def kama(real, period):
    """
    Kaufman Adaptive Moving Average
    """

    return lib.kama([real], [period])

kama.full_name = lib.kama.full_name
kama.type = lib.kama.type
kama.inputs = lib.kama.inputs
kama.options = lib.kama.options
kama.outputs = lib.kama.outputs


def kvo(high, low, close, volume, short_period, long_period):
    """
    Klinger Volume Oscillator
    """

    return lib.kvo([high, low, close, volume], [short_period, long_period])

kvo.full_name = lib.kvo.full_name
kvo.type = lib.kvo.type
kvo.inputs = lib.kvo.inputs
kvo.options = lib.kvo.options
kvo.outputs = lib.kvo.outputs


def lag(real, period):
    """
    Lag
    """

    return lib.lag([real], [period])

lag.full_name = lib.lag.full_name
lag.type = lib.lag.type
lag.inputs = lib.lag.inputs
lag.options = lib.lag.options
lag.outputs = lib.lag.outputs


def linreg(real, period):
    """
    Linear Regression
    """

    return lib.linreg([real], [period])

linreg.full_name = lib.linreg.full_name
linreg.type = lib.linreg.type
linreg.inputs = lib.linreg.inputs
linreg.options = lib.linreg.options
linreg.outputs = lib.linreg.outputs


def linregintercept(real, period):
    """
    Linear Regression Intercept
    """

    return lib.linregintercept([real], [period])

linregintercept.full_name = lib.linregintercept.full_name
linregintercept.type = lib.linregintercept.type
linregintercept.inputs = lib.linregintercept.inputs
linregintercept.options = lib.linregintercept.options
linregintercept.outputs = lib.linregintercept.outputs


def linregslope(real, period):
    """
    Linear Regression Slope
    """

    return lib.linregslope([real], [period])

linregslope.full_name = lib.linregslope.full_name
linregslope.type = lib.linregslope.type
linregslope.inputs = lib.linregslope.inputs
linregslope.options = lib.linregslope.options
linregslope.outputs = lib.linregslope.outputs


def ln(real):
    """
    Vector Natural Log
    """

    return lib.ln([real], [])

ln.full_name = lib.ln.full_name
ln.type = lib.ln.type
ln.inputs = lib.ln.inputs
ln.options = lib.ln.options
ln.outputs = lib.ln.outputs


def log10(real):
    """
    Vector Base-10 Log
    """

    return lib.log10([real], [])

log10.full_name = lib.log10.full_name
log10.type = lib.log10.type
log10.inputs = lib.log10.inputs
log10.options = lib.log10.options
log10.outputs = lib.log10.outputs


def macd(real, short_period, long_period, signal_period):
    """
    Moving Average Convergence/Divergence
    """

    return lib.macd([real], [short_period, long_period, signal_period])

macd.full_name = lib.macd.full_name
macd.type = lib.macd.type
macd.inputs = lib.macd.inputs
macd.options = lib.macd.options
macd.outputs = lib.macd.outputs


def marketfi(high, low, volume):
    """
    Market Facilitation Index
    """

    return lib.marketfi([high, low, volume], [])

marketfi.full_name = lib.marketfi.full_name
marketfi.type = lib.marketfi.type
marketfi.inputs = lib.marketfi.inputs
marketfi.options = lib.marketfi.options
marketfi.outputs = lib.marketfi.outputs


def mass(high, low, period):
    """
    Mass Index
    """

    return lib.mass([high, low], [period])

mass.full_name = lib.mass.full_name
mass.type = lib.mass.type
mass.inputs = lib.mass.inputs
mass.options = lib.mass.options
mass.outputs = lib.mass.outputs


def max(real, period):
    """
    Maximum In Period
    """

    return lib.max([real], [period])

max.full_name = lib.max.full_name
max.type = lib.max.type
max.inputs = lib.max.inputs
max.options = lib.max.options
max.outputs = lib.max.outputs


def md(real, period):
    """
    Mean Deviation Over Period
    """

    return lib.md([real], [period])

md.full_name = lib.md.full_name
md.type = lib.md.type
md.inputs = lib.md.inputs
md.options = lib.md.options
md.outputs = lib.md.outputs


def medprice(high, low):
    """
    Median Price
    """

    return lib.medprice([high, low], [])

medprice.full_name = lib.medprice.full_name
medprice.type = lib.medprice.type
medprice.inputs = lib.medprice.inputs
medprice.options = lib.medprice.options
medprice.outputs = lib.medprice.outputs


def mfi(high, low, close, volume, period):
    """
    Money Flow Index
    """

    return lib.mfi([high, low, close, volume], [period])

mfi.full_name = lib.mfi.full_name
mfi.type = lib.mfi.type
mfi.inputs = lib.mfi.inputs
mfi.options = lib.mfi.options
mfi.outputs = lib.mfi.outputs


def min(real, period):
    """
    Minimum In Period
    """

    return lib.min([real], [period])

min.full_name = lib.min.full_name
min.type = lib.min.type
min.inputs = lib.min.inputs
min.options = lib.min.options
min.outputs = lib.min.outputs


def mom(real, period):
    """
    Momentum
    """

    return lib.mom([real], [period])

mom.full_name = lib.mom.full_name
mom.type = lib.mom.type
mom.inputs = lib.mom.inputs
mom.options = lib.mom.options
mom.outputs = lib.mom.outputs


def msw(real, period):
    """
    Mesa Sine Wave
    """

    return lib.msw([real], [period])

msw.full_name = lib.msw.full_name
msw.type = lib.msw.type
msw.inputs = lib.msw.inputs
msw.options = lib.msw.options
msw.outputs = lib.msw.outputs


def mul(real, real2):
    """
    Vector Multiplication
    """

    return lib.mul([real, real2], [])

mul.full_name = lib.mul.full_name
mul.type = lib.mul.type
mul.inputs = lib.mul.inputs
mul.options = lib.mul.options
mul.outputs = lib.mul.outputs


def natr(high, low, close, period):
    """
    Normalized Average True Range
    """

    return lib.natr([high, low, close], [period])

natr.full_name = lib.natr.full_name
natr.type = lib.natr.type
natr.inputs = lib.natr.inputs
natr.options = lib.natr.options
natr.outputs = lib.natr.outputs


def nvi(close, volume):
    """
    Negative Volume Index
    """

    return lib.nvi([close, volume], [])

nvi.full_name = lib.nvi.full_name
nvi.type = lib.nvi.type
nvi.inputs = lib.nvi.inputs
nvi.options = lib.nvi.options
nvi.outputs = lib.nvi.outputs


def obv(close, volume):
    """
    On Balance Volume
    """

    return lib.obv([close, volume], [])

obv.full_name = lib.obv.full_name
obv.type = lib.obv.type
obv.inputs = lib.obv.inputs
obv.options = lib.obv.options
obv.outputs = lib.obv.outputs


def ppo(real, short_period, long_period):
    """
    Percentage Price Oscillator
    """

    return lib.ppo([real], [short_period, long_period])

ppo.full_name = lib.ppo.full_name
ppo.type = lib.ppo.type
ppo.inputs = lib.ppo.inputs
ppo.options = lib.ppo.options
ppo.outputs = lib.ppo.outputs


def psar(high, low, acceleration_factor_step, acceleration_factor_maximum):
    """
    Parabolic SAR
    """

    return lib.psar([high, low], [acceleration_factor_step, acceleration_factor_maximum])

psar.full_name = lib.psar.full_name
psar.type = lib.psar.type
psar.inputs = lib.psar.inputs
psar.options = lib.psar.options
psar.outputs = lib.psar.outputs


def pvi(close, volume):
    """
    Positive Volume Index
    """

    return lib.pvi([close, volume], [])

pvi.full_name = lib.pvi.full_name
pvi.type = lib.pvi.type
pvi.inputs = lib.pvi.inputs
pvi.options = lib.pvi.options
pvi.outputs = lib.pvi.outputs


def qstick(open, close, period):
    """
    Qstick
    """

    return lib.qstick([open, close], [period])

qstick.full_name = lib.qstick.full_name
qstick.type = lib.qstick.type
qstick.inputs = lib.qstick.inputs
qstick.options = lib.qstick.options
qstick.outputs = lib.qstick.outputs


def roc(real, period):
    """
    Rate of Change
    """

    return lib.roc([real], [period])

roc.full_name = lib.roc.full_name
roc.type = lib.roc.type
roc.inputs = lib.roc.inputs
roc.options = lib.roc.options
roc.outputs = lib.roc.outputs


def rocr(real, period):
    """
    Rate of Change Ratio
    """

    return lib.rocr([real], [period])

rocr.full_name = lib.rocr.full_name
rocr.type = lib.rocr.type
rocr.inputs = lib.rocr.inputs
rocr.options = lib.rocr.options
rocr.outputs = lib.rocr.outputs


def round(real):
    """
    Vector Round
    """

    return lib.round([real], [])

round.full_name = lib.round.full_name
round.type = lib.round.type
round.inputs = lib.round.inputs
round.options = lib.round.options
round.outputs = lib.round.outputs


def rsi(real, period):
    """
    Relative Strength Index
    """

    return lib.rsi([real], [period])

rsi.full_name = lib.rsi.full_name
rsi.type = lib.rsi.type
rsi.inputs = lib.rsi.inputs
rsi.options = lib.rsi.options
rsi.outputs = lib.rsi.outputs


def sin(real):
    """
    Vector Sine
    """

    return lib.sin([real], [])

sin.full_name = lib.sin.full_name
sin.type = lib.sin.type
sin.inputs = lib.sin.inputs
sin.options = lib.sin.options
sin.outputs = lib.sin.outputs


def sinh(real):
    """
    Vector Hyperbolic Sine
    """

    return lib.sinh([real], [])

sinh.full_name = lib.sinh.full_name
sinh.type = lib.sinh.type
sinh.inputs = lib.sinh.inputs
sinh.options = lib.sinh.options
sinh.outputs = lib.sinh.outputs


def sma(real, period):
    """
    Simple Moving Average
    """

    return lib.sma([real], [period])

sma.full_name = lib.sma.full_name
sma.type = lib.sma.type
sma.inputs = lib.sma.inputs
sma.options = lib.sma.options
sma.outputs = lib.sma.outputs


def sqrt(real):
    """
    Vector Square Root
    """

    return lib.sqrt([real], [])

sqrt.full_name = lib.sqrt.full_name
sqrt.type = lib.sqrt.type
sqrt.inputs = lib.sqrt.inputs
sqrt.options = lib.sqrt.options
sqrt.outputs = lib.sqrt.outputs


def stddev(real, period):
    """
    Standard Deviation Over Period
    """

    return lib.stddev([real], [period])

stddev.full_name = lib.stddev.full_name
stddev.type = lib.stddev.type
stddev.inputs = lib.stddev.inputs
stddev.options = lib.stddev.options
stddev.outputs = lib.stddev.outputs


def stderr(real, period):
    """
    Standard Error Over Period
    """

    return lib.stderr([real], [period])

stderr.full_name = lib.stderr.full_name
stderr.type = lib.stderr.type
stderr.inputs = lib.stderr.inputs
stderr.options = lib.stderr.options
stderr.outputs = lib.stderr.outputs


def stoch(high, low, close, pct_k_period, pct_k_slowing_period, pct_d_period):
    """
    Stochastic Oscillator
    """

    return lib.stoch([high, low, close], [pct_k_period, pct_k_slowing_period, pct_d_period])

stoch.full_name = lib.stoch.full_name
stoch.type = lib.stoch.type
stoch.inputs = lib.stoch.inputs
stoch.options = lib.stoch.options
stoch.outputs = lib.stoch.outputs


def sub(real, real2):
    """
    Vector Subtraction
    """

    return lib.sub([real, real2], [])

sub.full_name = lib.sub.full_name
sub.type = lib.sub.type
sub.inputs = lib.sub.inputs
sub.options = lib.sub.options
sub.outputs = lib.sub.outputs


def sum(real, period):
    """
    Sum Over Period
    """

    return lib.sum([real], [period])

sum.full_name = lib.sum.full_name
sum.type = lib.sum.type
sum.inputs = lib.sum.inputs
sum.options = lib.sum.options
sum.outputs = lib.sum.outputs


def tan(real):
    """
    Vector Tangent
    """

    return lib.tan([real], [])

tan.full_name = lib.tan.full_name
tan.type = lib.tan.type
tan.inputs = lib.tan.inputs
tan.options = lib.tan.options
tan.outputs = lib.tan.outputs


def tanh(real):
    """
    Vector Hyperbolic Tangent
    """

    return lib.tanh([real], [])

tanh.full_name = lib.tanh.full_name
tanh.type = lib.tanh.type
tanh.inputs = lib.tanh.inputs
tanh.options = lib.tanh.options
tanh.outputs = lib.tanh.outputs


def tema(real, period):
    """
    Triple Exponential Moving Average
    """

    return lib.tema([real], [period])

tema.full_name = lib.tema.full_name
tema.type = lib.tema.type
tema.inputs = lib.tema.inputs
tema.options = lib.tema.options
tema.outputs = lib.tema.outputs


def todeg(real):
    """
    Vector Degree Conversion
    """

    return lib.todeg([real], [])

todeg.full_name = lib.todeg.full_name
todeg.type = lib.todeg.type
todeg.inputs = lib.todeg.inputs
todeg.options = lib.todeg.options
todeg.outputs = lib.todeg.outputs


def torad(real):
    """
    Vector Radian Conversion
    """

    return lib.torad([real], [])

torad.full_name = lib.torad.full_name
torad.type = lib.torad.type
torad.inputs = lib.torad.inputs
torad.options = lib.torad.options
torad.outputs = lib.torad.outputs


def tr(high, low, close):
    """
    True Range
    """

    return lib.tr([high, low, close], [])

tr.full_name = lib.tr.full_name
tr.type = lib.tr.type
tr.inputs = lib.tr.inputs
tr.options = lib.tr.options
tr.outputs = lib.tr.outputs


def trima(real, period):
    """
    Triangular Moving Average
    """

    return lib.trima([real], [period])

trima.full_name = lib.trima.full_name
trima.type = lib.trima.type
trima.inputs = lib.trima.inputs
trima.options = lib.trima.options
trima.outputs = lib.trima.outputs


def trix(real, period):
    """
    Trix
    """

    return lib.trix([real], [period])

trix.full_name = lib.trix.full_name
trix.type = lib.trix.type
trix.inputs = lib.trix.inputs
trix.options = lib.trix.options
trix.outputs = lib.trix.outputs


def trunc(real):
    """
    Vector Truncate
    """

    return lib.trunc([real], [])

trunc.full_name = lib.trunc.full_name
trunc.type = lib.trunc.type
trunc.inputs = lib.trunc.inputs
trunc.options = lib.trunc.options
trunc.outputs = lib.trunc.outputs


def tsf(real, period):
    """
    Time Series Forecast
    """

    return lib.tsf([real], [period])

tsf.full_name = lib.tsf.full_name
tsf.type = lib.tsf.type
tsf.inputs = lib.tsf.inputs
tsf.options = lib.tsf.options
tsf.outputs = lib.tsf.outputs


def typprice(high, low, close):
    """
    Typical Price
    """

    return lib.typprice([high, low, close], [])

typprice.full_name = lib.typprice.full_name
typprice.type = lib.typprice.type
typprice.inputs = lib.typprice.inputs
typprice.options = lib.typprice.options
typprice.outputs = lib.typprice.outputs


def ultosc(high, low, close, short_period, medium_period, long_period):
    """
    Ultimate Oscillator
    """

    return lib.ultosc([high, low, close], [short_period, medium_period, long_period])

ultosc.full_name = lib.ultosc.full_name
ultosc.type = lib.ultosc.type
ultosc.inputs = lib.ultosc.inputs
ultosc.options = lib.ultosc.options
ultosc.outputs = lib.ultosc.outputs


def var(real, period):
    """
    Variance Over Period
    """

    return lib.var([real], [period])

var.full_name = lib.var.full_name
var.type = lib.var.type
var.inputs = lib.var.inputs
var.options = lib.var.options
var.outputs = lib.var.outputs


def vhf(real, period):
    """
    Vertical Horizontal Filter
    """

    return lib.vhf([real], [period])

vhf.full_name = lib.vhf.full_name
vhf.type = lib.vhf.type
vhf.inputs = lib.vhf.inputs
vhf.options = lib.vhf.options
vhf.outputs = lib.vhf.outputs


def vidya(real, short_period, long_period, alpha):
    """
    Variable Index Dynamic Average
    """

    return lib.vidya([real], [short_period, long_period, alpha])

vidya.full_name = lib.vidya.full_name
vidya.type = lib.vidya.type
vidya.inputs = lib.vidya.inputs
vidya.options = lib.vidya.options
vidya.outputs = lib.vidya.outputs


def volatility(real, period):
    """
    Annualized Historical Volatility
    """

    return lib.volatility([real], [period])

volatility.full_name = lib.volatility.full_name
volatility.type = lib.volatility.type
volatility.inputs = lib.volatility.inputs
volatility.options = lib.volatility.options
volatility.outputs = lib.volatility.outputs


def vosc(volume, short_period, long_period):
    """
    Volume Oscillator
    """

    return lib.vosc([volume], [short_period, long_period])

vosc.full_name = lib.vosc.full_name
vosc.type = lib.vosc.type
vosc.inputs = lib.vosc.inputs
vosc.options = lib.vosc.options
vosc.outputs = lib.vosc.outputs


def vwma(close, volume, period):
    """
    Volume Weighted Moving Average
    """

    return lib.vwma([close, volume], [period])

vwma.full_name = lib.vwma.full_name
vwma.type = lib.vwma.type
vwma.inputs = lib.vwma.inputs
vwma.options = lib.vwma.options
vwma.outputs = lib.vwma.outputs


def wad(high, low, close):
    """
    Williams Accumulation/Distribution
    """

    return lib.wad([high, low, close], [])

wad.full_name = lib.wad.full_name
wad.type = lib.wad.type
wad.inputs = lib.wad.inputs
wad.options = lib.wad.options
wad.outputs = lib.wad.outputs


def wcprice(high, low, close):
    """
    Weighted Close Price
    """

    return lib.wcprice([high, low, close], [])

wcprice.full_name = lib.wcprice.full_name
wcprice.type = lib.wcprice.type
wcprice.inputs = lib.wcprice.inputs
wcprice.options = lib.wcprice.options
wcprice.outputs = lib.wcprice.outputs


def wilders(real, period):
    """
    Wilders Smoothing
    """

    return lib.wilders([real], [period])

wilders.full_name = lib.wilders.full_name
wilders.type = lib.wilders.type
wilders.inputs = lib.wilders.inputs
wilders.options = lib.wilders.options
wilders.outputs = lib.wilders.outputs


def willr(high, low, close, period):
    """
    Williams %R
    """

    return lib.willr([high, low, close], [period])

willr.full_name = lib.willr.full_name
willr.type = lib.willr.type
willr.inputs = lib.willr.inputs
willr.options = lib.willr.options
willr.outputs = lib.willr.outputs


def wma(real, period):
    """
    Weighted Moving Average
    """

    return lib.wma([real], [period])

wma.full_name = lib.wma.full_name
wma.type = lib.wma.type
wma.inputs = lib.wma.inputs
wma.options = lib.wma.options
wma.outputs = lib.wma.outputs


def zlema(real, period):
    """
    Zero-Lag Exponential Moving Average
    """

    return lib.zlema([real], [period])

zlema.full_name = lib.zlema.full_name
zlema.type = lib.zlema.type
zlema.inputs = lib.zlema.inputs
zlema.options = lib.zlema.options
zlema.outputs = lib.zlema.outputs

