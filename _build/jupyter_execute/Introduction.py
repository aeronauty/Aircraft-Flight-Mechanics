
# Introduction

This website comprises the course notes for MMAE 410 Aircraft Flight Mechanics - this text originally started as a PDF file written using LaTeX, with links to code and other tidbits. These notes started as my means of ensuring my own competence with the material and, accordingly, they get updated regularly and requiring students to download an updated PDF file every few weeks proved to not be the ideal solution.

So now these notes are being transferred into Jupyter notebooks which are bundled together into this document - any changes made to the notes should be reflected in the website within minutes, and this format allows handy things like _interactive content,_ which simply isn't possible (easily) within a PDF.

It does mean that my pipedream of getting them published as a textbook is over - but in the spirit of open access and education for all, I'd simply rather that they just got used for their intended purpose. Hence; use these notes to supplement your own learning, and to further your knowledge of the discipline.

## Interactive content - using Python

The original PDF notes were written and contained examples using both MATLAB and Python. Over the past few months, I've made the personal decision to switch _all_ my code from MATLAB to Python. There are many reasons for this change, but the benefit for the reader is that you can view the source for any of the plots included in this book. There should also be interactive content that will help you to explore equations, and understand the relationship between different parameters.

Here's a trivial example of a plot that you can edit


And see {eq}`my_label` below:
```{math}
:label: my_label
F = m\,a
v = u + a\,t
```



import numpy as np
import matplotlib.pyplot as plt

n = 3

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(n * x)

plt.figure()
plt.plot(x, y, '-b')
plt.xlabel('x')
plt.ylabel('y')






```{toctree}
:hidden:
:titlesonly:
:caption: Prerequisites

Prerequisites/AircraftAnatomy
Prerequisites/LiftandDrag
```


```{toctree}
:hidden:
:titlesonly:
:caption: Aircraft Performance

AircraftPerformance/Airspeed
AircraftPerformance/SteadyLevelFlight
AircraftPerformance/Propulsion
AircraftPerformance/RangeandEndurance
AircraftPerformance/ClimbandDescent
AircraftPerformance/SteadyTurns
```


```{toctree}
:hidden:
:titlesonly:
:caption: Aircraft Equations of Motion

EoM/Introduction
```
