[![Build Status](https://travis-ci.org/cirla/tulipy.svg?branch=master)](https://travis-ci.org/cirla/tulipy)
[![Build status](https://ci.appveyor.com/api/projects/status/g34af6ti605e2q4h?svg=true)](https://ci.appveyor.com/project/cirla/tulipy)

# tulipy

## Python bindings for [Tulip Indicators](https://tulipindicators.org/)

Tulipy requires [numpy](http://www.numpy.org/) as all inputs and outputs are numpy arrays (`dtype=np.float64`).

## Installation

You can install via `pip install tulipy`.
If a wheel is not available for your system, you will need to `pip install Cython numpy` to build from the source distribution.
When building from source on Windows, you will need the Microsoft Visual C++ Build Tools installed.

## Usage


```python
import numpy as np
import tulipy as ti
```


```python
ti.TI_VERSION
```




    '0.8.4'




```python
DATA = np.array([81.59, 81.06, 82.87, 83,    83.61,
                 83.15, 82.84, 83.99, 84.55, 84.36,
                 85.53, 86.54, 86.89, 87.77, 87.29])
```

Information about indicators are exposed as properties:


```python
def print_info(indicator):
    print("Type:", indicator.type)
    print("Full Name:", indicator.full_name)
    print("Inputs:", indicator.inputs)
    print("Options:", indicator.options)
    print("Outputs:", indicator.outputs)
```


```python
print_info(ti.sqrt)
```

    Type: simple
    Full Name: Vector Square Root
    Inputs: ['real']
    Options: []
    Outputs: ['sqrt']


Single outputs are returned directly. Indicators returning multiple outputs use
a tuple in the order indicated by the `outputs` property.


```python
ti.sqrt(DATA)
```




    array([ 9.03271831,  9.00333272,  9.10329611,  9.11043358,  9.14385039,
            9.11866218,  9.1016482 ,  9.16460583,  9.19510739,  9.18477   ,
            9.24824308,  9.30268778,  9.32148057,  9.36856446,  9.34291175])




```python
print_info(ti.sma)
```

    Type: overlay
    Full Name: Simple Moving Average
    Inputs: ['real']
    Options: ['period']
    Outputs: ['sma']



```python
ti.sma(DATA, period=5)
```




    array([ 82.426,  82.738,  83.094,  83.318,  83.628,  83.778,  84.254,
            84.994,  85.574,  86.218,  86.804])



Invalid options will throw an `InvalidOptionError`:


```python
try:
    ti.sma(DATA, period=-5)
except ti.InvalidOptionError:
    print("Invalid Option!")
```

    Invalid Option!



```python
print_info(ti.bbands)
```

    Type: overlay
    Full Name: Bollinger Bands
    Inputs: ['real']
    Options: ['period', 'stddev']
    Outputs: ['bbands_lower', 'bbands_middle', 'bbands_upper']



```python
ti.bbands(DATA, period=5, stddev=2)
```




    (array([ 80.53004219,  80.98714192,  82.53334324,  82.47198345,
             82.41775044,  82.43520292,  82.51133078,  83.14261781,
             83.53648779,  83.8703237 ,  85.28887096]),
     array([ 82.426,  82.738,  83.094,  83.318,  83.628,  83.778,  84.254,
             84.994,  85.574,  86.218,  86.804]),
     array([ 84.32195781,  84.48885808,  83.65465676,  84.16401655,
             84.83824956,  85.12079708,  85.99666922,  86.84538219,
             87.61151221,  88.5656763 ,  88.31912904]))



If inputs of differing sizes are provided, they are right-aligned and trimmed from the left:


```python
DATA2 = np.array([83.15, 82.84, 83.99, 84.55, 84.36])
```


```python
# 'high' trimmed to DATA[-5:] == array([ 85.53,  86.54,  86.89,  87.77,  87.29])
ti.aroonosc(high=DATA, low=DATA2, period=2)
```




    array([  50.,  100.,   50.])


