---
title: Introduction
subtitle: Introduction to `oxphys_numerics`
description: Introduction to the `oxphys_numerics` python package
status: new
---

`oxphys_numerics` is a python package that provides general purpose tools for numerical work in python.
The focuses of the package are:

<div class="annotate" markdown>
-  :rocket: **Performance**: On your machine, the `oxphys_numerics` package should be able to do everything that packages like [`numpy`](https://numpy.org/) can do, but with superior performance.(1)
-  :cloud: **Scalability**: `oxphys_numerics` applications are *cloud-native*, and can be scaled to handle enormous calculations.(2)
-  :battery: **Batteries included**: `oxphys_numerics` should be as easy to use as is reasonably possible. This isn't a package for high performance computing experts, but for scientists and engineers who have stuff to get done.(3)
</div>

1.  All `oxphys_numerics` expressions are jit-compiled when you evaluate them, so you get the performance of a compiled language and can leverage the full power any special instructions specific to your CPU. We won't accept anything but the best performance from our code, so we have written our own just-in-time compiler to maintain full control over the emitted machine code.
2.  Efficient cloud computing has been one of the core goals of the `oxphys_numerics` project since its inception. We're *performance obsessed*; we want `oxphys_numerics` to power the most demanding scientific workloads in the world.
3.  `oxphys_numerics` ships with a wide range of algorithms for doing things like analysing PDEs, integrating expressions and solving optimization problems. We believe in sensible defaults and a simple API.

So, we want it to be easy to use on your local machine, while being blazingly fast.
Once you have finished your preliminary investigations, scaling up to the cloud should be as simple as setting an environment variable, and passing an extra argument to the `oxphys_numerics` function you're calling.
