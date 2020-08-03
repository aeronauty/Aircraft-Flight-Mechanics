# Course Introduction

## What is Flight Mechanics?

Without going back to basics too much, a definition of what Flight Mechanics is can be garnered from the definitions of each word:

```{epigraph}
**flight** - *the action or process of flying through the air*

-- Oxford English Dictionary
```

So Flight is relatively easy to understand. *Mechanics*, when not referring to people who fix machinery is defined as

```{epigraph}
**mechanics** - *the branch of mathematics dealing with **motion** and **forces producing motion***

-- Oxford English Dictionary
```

Flight Mechanics allows us to construct a mathematical *model* of an aircraft to analyse and predict flight characteristics. Generally, a model is a simpler representation of a system that has sufficient fidelity to represent the parameters of interest - so we are not concerned with, say, turbulence modelling in this course as this is a higher order parameter when understanding aircraft performance, stability, and control.

Within the field of mechanics, we define **kinematics** as the study of motion, without reference to the forces causing it - problems involving the kinematic equations ($s,u,v,a,t$ equations\...$v=u+a\cdot t$, ). This allows us to solve *some* problems in aircraft flight involving aircraft performance (given an aircraft's position, speed, and acceleration, we can determine basic distance parameters).

To gain further insight, we need to understand the forces that cause motion - this is the field of **kinetics**. The forces of interest for this course are, lift, drag, thrust, and weight - with which you should be familiar from MMAE 312, Aerodynamics of Aerospace Vehicles.

## Recommended Textbooks

These notes, and the materials presented in the class are sufficient to gain a full understanding of any examinable material. These notes are based on the previous course structure, which utilises "*Introduction to Aircraft Flight Mechanics*" by Tom Yechout {cite}`Yechout:2014vg`.

Other supplementary texts that may be useful are "*Aerodynamics for Engineering Students*" {cite}`Houghton:2012vl` and "*Aircraft Flight*" {cite}`Barnard:2010td`

## Course Structure

This is a *large* course, comprising five interrelated modules:

1.  **Aircraft Performance**: Defining relationships between basic forces and motion in steady, level flight, with aircraft represented by a point mass. Understanding take-off, landing, and steady turns. Range calculations.

2.  **Aircraft Equations of Motion**: Axis systems, reference frames, and relative motion. Newton's Second law as applied for aircraft forces and moments

3.  **Static Stability**: Defining trimmed conditions, utilising relationships between control surface deflections, and forces around the aircraft CG.

4.  **Linearisation of the Equations of Motion**: Using the small perturbation theory to linearise the aircraft nonlinear differential equations of motion.

5.  **Flight Dynamics**: Stability definitions for first order and second order systems. Laplace transforms, characteristic equation. Longitudinal EOM dynamics; short-period (pitch) mode, phugoid mode. Lateral/Directional EOM dynamics; spiral mode, roll mode, Dutch roll mode. Predicting the dynamic stability of fixed wing aircraft. Reduced order models.

Each of these could be an entire course on its own, so we will not be able to cover the entirety of each subject, but we will develop an understanding of sufficient detail to answer questions on a range of topics in each subject.


 