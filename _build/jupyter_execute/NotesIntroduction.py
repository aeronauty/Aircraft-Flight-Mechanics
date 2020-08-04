
# Introduction to this website

This website comprises the course notes for MMAE 410 Aircraft Flight Mechanics at the Illinois Institute of Technology - this text originally started as a PDF file written using LaTeX, with links to code and other tidbits. These notes started as my means of ensuring my own competence with the material and, accordingly, they get updated regularly and requiring students to download an updated PDF file every few weeks proved to not be the ideal solution.

So now these notes are being transferred into Jupyter notebooks which are bundled together into this document - any changes made to the notes should be reflected in the website within minutes, and this format allows handy things like _interactive content,_ which simply isn't possible (easily) within a PDF.

It does mean that my pipedream of getting them published as a textbook is over - but in the spirit of open access and education for all, I'd simply rather that they just got used for their intended purpose. Hence; use these notes to supplement your own learning, and to further your knowledge of the discipline.

## Why use Python

The original PDF notes were written and contained examples using both MATLAB and Python. Over the past few months, I've made the personal decision to switch _all_ my code from MATLAB to Python. There are many reasons for this change, but the benefit for the reader is that you can view the source for any of the plots included in this book without purchasing a MATLAB license. 

### Interactive content

There is iteractive content that will help you to explore equations, and understand the relationship between different parameters.

The way this works is slightly convoluted, but very powerful - this whole book is hosted as a GitHub repository, as a mixture of ```.md``` and ```.ipynb``` files. This means that any Jupyter Notebooks can be run on the web thanks to the kind folks at DockerHub. The book is written using JupyterBook, which is a plugin called *thebe*, which enables the code sections to be run without having to actually go to DockerHub.

What this means is that you have a few different ways to access the interactive content:
- Download the whole ```.ipynb``` file and run natively in Juypter on your machine: {ref}`Github`
- Run the notebook in Docker: {ref}`Binder`
- Run the code in-place using thebe: {ref}`Thebe`

Both of the latter work well on the pages I have tested - but it can take time for the whole notebook to be initlialised. If you click on "run code" in the dropdown from the rocket icon at the top of the page, it needs to connect to Docker, which then connects to GitHub, and then send the content back to this site.

```{figure} Images/Binder.png
---
height: 30px
name: Binder
---
Connecting to Binder/Thebe
```

```{figure} Images/Github.png
---
height: 30px
name: Github
---
Downloading the source or a PDF
```

Give it a go, though - here's a trivial example of a plot that you can edit. Try the different ways of accessing this content.

The plot below plots $y=\sin(n\cdot x)$ in the interval 0 to $2\pi$. You can change whatever you want in the code below and make it run.




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
:caption: Getting Started

CourseIntroduction
Prerequisites/Prerequisites
```


```{toctree}
:hidden:
:titlesonly:
:caption: Aircraft Performance

AircraftPerformance/Introduction
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


```{toctree}
:hidden:
:titlesonly:
:caption: References and Resources

zreferences
```
