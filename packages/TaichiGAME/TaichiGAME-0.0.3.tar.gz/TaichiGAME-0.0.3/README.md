<div align="center">
<!-- Title: -->
  <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/logo.png" />
  <br />
  <br />
  <a href="https://github.com/maksyuki/TaichiGAME/actions">
    <img src="https://img.shields.io/github/workflow/status/maksyuki/TaichiGAME/unit-test/main?label=unit-test&logo=github&style=flat-square">
  </a>
  <a href="https://app.codecov.io/gh/maksyuki/TaichiGAME/">
    <img src="https://img.shields.io/codecov/c/github/maksyuki/TaichiGAME/main?logo=codecov&style=flat-square">
  </a>
  <a href="https://github.com/maksyuki/TaichiGAME">
    <img src="https://img.shields.io/pypi/v/TaichiGAME?logo=pypi&style=flat-square">
  </a>
  <a href="https://github.com/maksyuki/TaichiGAME">
    <img src="https://img.shields.io/pypi/pyversions/TaichiGAME?logo=python&style=flat-square">
  </a>
  <!-- Second row: -->
  <br>

  <a href="https://github.com/maksyuki/TaichiGAME">
    <img src="https://img.shields.io/github/license/maksyuki/TaichiGAME?color=brightgreen&logo=github&style=flat-square">
  </a>
  <!-- <a href="https://github.com/maksyuki/TaichiGAME">
    <img src="https://img.shields.io/tokei/lines/github/maksyuki/TaichiGAME?style=flat-square">
  </a> -->
  <a href="https://github.com/maksyuki/TaichiGAME">
    <img src="https://img.shields.io/badge/total%20lines-12k-blue?style=flat-square">
  </a>
  <a href="https://github.com/google/yapf">
    <img src="https://img.shields.io/badge/code%20style-yapf%20mypy-red?style=flat-square">
  </a>
  <a href="https://github.com/PyCQA">
    <img src="https://img.shields.io/badge/static%20checker-pylint%20pycodestyle-red?style=flat-square">
  </a>
  <a href="https://github.com/maksyuki/TaichiGAME/blob/main/CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/contribution-welcome-brightgreen?style=flat-square">
  </a>
<!-- Short description: -->

  <h1></h1>
</div>


## Overview
TaichiGAME is aim to become a lightweight simulation engine in **motion planning and control research fields**. And it is written in python and [taichi](https://github.com/taichi-dev/taichi), which combines the traditional numerical methods for solving rigid dynamics equations, model parameters derivation, with parallel implementation capabilites in order to maximize scientists' productivity.

## Motivation
I am a postgraduate in school of astronautics and major in aerospace robot guidance, navigation and control. During my first year, I took a class on _advanced control theory_ and was taught many different control algorithms for estimating dynamic model, fitting state curves and so on.

When I carried out a research on asteroid rover motion planning supported by NFSC(**National Natural Science Foundation of China**), I spent lots of time on learning c++ for writing parallel program to solve complex rigid body dynamics equations. To be honest, achieving all of the details, especially some c++ advanced features, made me thoroughly exhausted. I could not just focus on the algorithms and built rapid prototype to verify it. I thought others feel the same way. After that, I searched online and found no open source, scientific-oriented, out-of-the-box tools or framework to execute such high performance rigid body motion computing. In that case, why not build one? The result of that desire is this project.

## Feature

> NOTE: Due to my research is still under review and revise, I could not release all results now. At present, I only release the initial physics engine component of TaichiGAME. So I only introduce physics engine component now. In the first half of 2022, I will release other components of TaichiGAME.

To implement the physics engine, I refer to the [Physics2D (c++, MIT License)](https://github.com/AngryAccelerated/Physics2D) project, and rewrite entire content of it into python with taichi and add more unit tests. The following architecture chart illustrates the basic features:

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/arch.drawio.svg"/>
 <p align="center">
  <em>The basic features of physics component in TaichiGAME</em>
  <br>
  <em>(open it in a new window to browse the larger picture)</em>
 </p>
</p>

## What is missing
First,  the physics engine component is under alpha phase, so it is lack of stability and reliability. Second, to narrow the development period, I use the easy-to-implement numberical methods, that makes the performance suffer a bit.

## Requirements
1. python>=3.7, <=3.9, because:
   - use `from __future__ import annotations` to postpone evaluation of annotations `(python3.7+ intro)`
   - taichi supports the highest version of python is `python3.9`

2. taichi>=0.8.0, because:
    - support taichi's new features
    - now TaichiGAME doesn't use the new GGUI `(taichi0.8+ intro)`, so maybe you can use lower version taichi(such as `taichi0.7+`).
    - **NOTE:** some TaichiGAME's API is based on specific taichi features. In views of the rapid development of taichi, I don't have much enery and time to maintain TaichiGAME to adapt or be compatiable to multiple different major version of taichi. It can make TaichiGAME too verbose. So I decide to **ONLY maintain TaichiGAME to adapt to current major verion plus one latest previous major verion of taichi**. For now, because a major version of taichi has not been released yet, I decide to **CHANGE** the 'major version' of previous policy into 'minor version'. Specifically, I develop and test all features of TaichiGAME in `taichi0.8+` , and **ONLY** maintain compatible version of TaichiGAME to `taichi0.7+`, the TaichiGAME based on `taichi<0.7+` will no longer be maintained.

## Install

Installation is simple, you can just type the following command in `shell` or `cmd` terminal(**_Recommend_**).

```shell
$ python3 -m pip install TaichiGAME
```

After installation, type following command to run the build-in example [`testbed.py`](./examples/testbed.py).

```shell
$ python3 -m TaichiGAME example testbed
```

You can type `python3 -m TaichiGAME -h` and `python3 -m TaichiGAME example -h` to get detail command line parameters usage. This cli module refers to [taichi main module](https://github.com/taichi-dev/taichi/blob/master/python/taichi/main.py).

> NOTE: Recommand use `venv` to isolate test environment from system directories, you can get more details from [Creation of virtual environments](https://docs.python.org/3/library/venv.html).

Another method is `git clone` this repo, `pip install` dependencies, and then run the [`testbed.py`](./examples/testbed.py) from package directly.
```shell
$ git clone https://github.com/maksyuki/TaichiGAME.git
$ cd TaichiGAME/
$ python3 -m pip install -r requirements.txt
$ cd TaichiGAME/ # necessary, run main.py in project root path can trigger module import error
$ python3 main.py example testbed
```

> NOTE: When running code, you maybe notice terminal print some informations like `[Taichi] version 0.8.7, llvm 10.0.0, commit 1c3c705a, osx, python 3.8.8`. I have tested TaichiGAME under `taichi>=0.7`. Your output maybe different from mine, but it doesn't matter.

### Testbed keyborad and mouse control
 - Press `esc` to exit the gui, `space` to pause simulation.
 - Press `left arrow` or `right arrow` key to switch different frames.
 - Press and hold `right mouse button` to move viewport position. Roll `mouse wheel` to zoom in or out the viewport.
 - Press and hold `left mouse button` to apply a mouse joint constraint to selected shape from the start point(mouse press position) to end point(current mouse hold position).
 - | keyboard button | function | keyboard button | function | keyboard button | function |
   | :-------------: | :------: | :-------------: | :------: | :-------------: | :------: |
   | `q` | toggle frame visibility | `w` | toggle AABB visibility | `e`|  toggle joint visibility|
   | `r` | toggle body visibility | `t` | toggle axis visibility | `a` | toggle dbvh visibility |
   | `s` | toggle dbvt visibility | `d` | toggle grid visibility | `f` | toggle rotation line visibility |
   | `g` | toggle center visibility | `z` | toggle contact visibility |

### Testbed simulation result
1. **dbvt query**: this frame is aim to show the dbvt's ability to accelerate the broad phase query of collision. The red rectangle represents the query region, yellow rectangles represent the query results(AABB of the shape).
<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/dbvt_query.gif"/>
 <p align="center">
  <em>The dbvt query with smooth viewport zoom in</em>
 </p>
</p>

2. **raycast**: this frame casts a ray in given direction. You can move the cast direction by mouse, and the cast shapes are rendered in cyan color.
<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/raycast.gif"/>
 <p align="center">
  <em>The raycast from the origin in given direction </em>
 </p>
</p>

3. **bitmask**: this frame shows two objects, a square and a ground, are with same bitmask property can contact with each other. In addition, the yellow rectangles represent the real time update result of dbvt.
<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/bitmask.gif"/>
 <p align="center">
  <em>Three squares contact with ground</em>
 </p>
</p>

4. **collision**: those frames show multiple collision examples. First one is a simple collision, second frame shows eight balls hit the ground with different restitution increased from left to right, the last one shows the three squares slide down from slopes with different friction coefficient.

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/collision_simple.gif"/>
 <p align="center">
  <em>A capsule hit the ground</em>
 </p>
</p>

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/collision_restit.gif"/>
 <p align="center">
  <em>Eight balls hit the ground with different restitution</em>
 </p>
</p>

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/collision_fric.gif"/>
 <p align="center">
  <em>Three squares slide down from slopes</em>
 </p>
</p>

5. **stack**: this frame shows a free fall square stack. You can apply mouse joint constraint to the shape.
<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/stack.gif"/>
 <p align="center">
  <em>The free fall stack</em>
 </p>
</p>

6. **domino**: this frame shows a pendulum strike a domino card and trigger a ripple collison. The surface of ground and slopes are both smooth, so the card can not stay static on it.
<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/domino.gif"/>
 <p align="center">
  <em>The domino simulation</em>
 </p>
</p>

### Quick Start
If you want to use `TaichiGAME` to implement your own simulation. You need to import `numpy`, `taichi` and `TaichiGAME` package first:
```python
import numpy as np
import taichi as ti
import TaichiGAME as tg

ti.init(arch=ti.gpu)
```
Then, you need to define a instance of `Scene` class. The `Scene` class is the base container holding all the resources, such as `Frame`, `Camera` and so on.

```python
# api: (class) tg.Scene(name: str, width: int = 1280, height: int = 720, option={})
scene = tg.Scene(name='Your Custom Name')
```
After that, you need to inherhit base class `Frame` and implement the `load()` and `render()` methods.  `load()` is called once when frame is initialized. If you want to custom extra render, you can implement `render()` optional. It is called in main render loop.
```python
class YourCustomFrameName(ng.Frame):
    def load():
      ...

    def render():
      ...
```
At last, you need to register the frame to the scene, initialize the frame and show the scene. Register mulitple frames to the scene is allowed as [`testbed.py`](./examples/testbed.py) do.
```python
custom_frame = YourCustomFrameName()
scene.register_frame(custom_frame)
scene.init_frame()
scene.show()
```
If you want to export the result as video or gif, you need to add `video` or `gif` config to the `scene`'s options list. Such as:
```python
scene = tg.Scene(name='Your Custom Name', option={'video': True, 'gif': True})
```
the video or gif is saved as `./export-res/video.mp4` and `./export-res/video.gif` by default.

> NOTE: TaichiGAME uses taichi's APIs to export video, so you need to install the `ffmpeg` first. How to install ffmpeg you can refer to [Install ffmpeg](https://docs.taichi.graphics/lang/articles/misc/export_results#export-videos) section of taichi doc.

If you want to know more details, you can refer to the official example [`testbed.py`](./examples/testbed.py). 

## Technical details
In general, the simulation is divided into two parts: **_physics calculation_** and **_frame render_**. This collision detection pipeline refers to the [Box2D](https://github.com/erincatto/box2d) and [Matter.js](https://github.com/liabru/matter-js).

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/flow.drawio.svg"/>
 <p align="center">
   <em>The simulation flow chart</em>
  <br>
  <em>(open it in a new window to browse the larger picture)</em>
 </p>
</p>

### Physics calculation
1. DBVT(**_Dynamics Bounding Volume Tree_**) is a tree data structure that is used to accelerate ray casts, overlap queries, and closest point queries for large worlds. Now the bounding box type of TaichiGAME use is AABB(**_Axis-Aligned Bounding Box_**). This data strucutre is a bit like AVL tree. If you want to know more details, you can refer to [[1]](#id_dbvt).

2. GJK(**_Gilbert–Johnson–Keerthi distance algorithm_**) is a method of determining the minimum distance between two convex sets. It does not require that the geometry data be stored in any specific format, but instead relies solely on a support function to iteratively generate closer simplices to the correct answer using the configuration space obstacle (CSO) of two convex shapes, more commonly known as the Minkowski difference(_[from wikipedia](https://en.wikipedia.org/wiki/Gilbert%E2%80%93Johnson%E2%80%93Keerthi_distance_algorithm)_). More informations can refer to [[2]](#id_fpbma)[[3]](#id_rtcd)[[4]](#id_gpg7).

3. Constraint solving is aim to restrict freedom of movement. TaichiGAME uses impulse-based constraint dynamics to calculate the equation. Based on moment-of-momentum equation and the method of lagrange multipliers, the impulse lambda can be deduced as：

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/lambda.png">
</p>

the impuse of a object is ![Image](https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/i_a.png), the impuse of b object is ![Image](https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/i_b.png).


To counter the fall of objects, previous equation need to introduce bias item. The penetration error is ![Image](https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/pen_error.png), and according to the **_Baumgarte Stabilization Method_**: ![Image](https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/bsm.png), the bias impuse can be deduced as ![Image](https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/bias_lambda.png).

### Render shape
All the shape's geometry data are provided in body coordinate system. For point/circle, TaichiGAME only uses `ti.GUI.circles` to draw inner shape with fill color. For polgyon, TaichiGAME uses `ti.GUI.triangles` to fill the shape by triangulation and uses `ti.GUI.lines` to draw the outline. Capsule is composed of two circles and one rectangle.

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/render.drawio.svg"/>
 <p align="center">
  <em>Base geometry shape and render method </em>
 </p>
</p>

Because the polygon is filled by triangulation, TaichiGAME renders one **N**-vertices polgon need to draw **N** lines and fill **N-2** triangles. Meanwhile, the `GUI` component of `taichi` not like `GGUI`, it cannot render on GPU. So if the frames have too many polygons to render, the workload becomes terrible large. In future, I will rewrite TaichiGAME renderer into `GGUI`.

## Performance optimization
First, I implement a cpu-based testbed([testbed.py](./examples/testbed.py)), which only use taichi to render the frames. Due to heavy calculation, that makes simulation slowly. After analysis and trade-off, I decide to rewrite some modules to make testbed into taichi-based([ti_testbed.py](./examples/ti_testbed.py)), the solutions are:
1. **Redesign the calculate structure** to fully utilize the taichi computing ability.
2. **Reuse some IO data structure** to provide unified external interface.
3. **Design a conversion method** to transfer data from 'python' scope into 'taichi' scope.

> NOTE: As the final exam is approaching, the optimization is still working in progress. That means the `ti_testbed.py` is not quite complete.

<p align="center">
 <img src="https://raw.githubusercontent.com/maksyuki/TaichiGAME-res/main/structure.drawio.svg"/>
 <p align="center">
  <em>The different between cpu-based and gpu-based structure</em>
 </p>
</p>


### Redesign the calculate structure
Use `ti.Vector.field` to hold all variables in [ti_phy_world.py](./TaichiGAME/dynamics/ti_phy_world.py). Every type of shape has own position and geometry features field.

### Reuse the IO data structure
Share common shape module , so you can define frame like cpu-based simulation do:
```python
def load(self) -> None:
    tri_data = [
        ng.Matrix([-1.0, 1.0], 'vec'),
        ng.Matrix([0.0, -2.0], 'vec'),
        ng.Matrix([1.0, -1.0], 'vec'),
        ng.Matrix([-1.0, 1.0], 'vec'),
    ]

    poly_data = [
        ng.Matrix([0.0, 4.0], 'vec'),
        ng.Matrix([-3.0, 3.0], 'vec'),
        ng.Matrix([-4.0, 0.0], 'vec'),
        ng.Matrix([-3.0, -3.0], 'vec'),
        ng.Matrix([0.0, -4.0], 'vec'),
        ng.Matrix([0.0, 4.0], 'vec')
    ]

    rect: ng.Rectangle = ng.Rectangle(0.5, 0.5)
    cir: ng.Circle = ng.Circle(0.5)
    cap: ng.Capsule = ng.Capsule(1.5, 0.5)
    tri: ng.Polygon = ng.Polygon()
    tri.vertices = tri_data
    poly: ng.Polygon = ng.Polygon()
    poly.vertices = poly_data
```
### Design a conversion method
In `init_data(self)` of [ti_phy_world.py](./TaichiGAME/dynamics/ti_phy_world.py), all numpy-based data is converted into taichi-based data.
```python
self._vel[i] = ti.Vector([self._body_list[i].vel.x, self._body_list[i].vel.y])
self._rot[i] = self._body_list[i].rot
self._ang_vel[i] = self._body_list[i].ang_vel
self._force[i] = ti.Vector([self._body_list[i].forces.x, self._body_list[i].forces.y])
```

## Contribution
If you want to contribute to TaichiGAME, be sure to review the [guidelines](CONTRIBUTING.md). This is an open project and contributions and collaborations are always welcome!! This project adheres to TaichiGAME's [code_of_conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

I use GitHub issues for tracking requests and bugs, so please direct specific questions to [issues panel](https://github.com/maksyuki/TaichiGAME/issues).

The TaichiGAME project strives to abide by generally accepted best practices in open-source software development, so feel free to raise a issues :smile:

## License
All of the TaichiGAME codes are release under the [MIT License](LICENSE).

## Acknowledgement
1. Thank [yuanming-hu](https://github.com/yuanming-hu) and [taichi-team](https://github.com/taichi-dev) for creating and maintaining [taichi](https://github.com/taichi-dev/taichi), such an excellent programming language. Meanwile, express thanks to [taichi-team](https://github.com/taichi-dev) to provide free and high-quality [taichi course](https://github.com/taichiCourse01). As well as course's tutor, [Tiantian Liu](https://tiantianliu.cn/) and responsible assistants.

2. Thanks to [ACRL](https://github.com/AngryAccelerated) and his engine project [Physics2D](https://github.com/AngryAccelerated/Physics2D). In addition, His [series posts](https://www.zhihu.com/people/acrl/posts) is full of detailed and understandable contents about graphcs and physics engine. Due to him, I learned a tons of konwledges from sratch.

3. Use [Inkscape 1.1.1 (3bf5ae0d25, 2021-09-20, window x64 version, GPL-3.0)](https://inkscape.org/) to draw the logo. Use [diagrams.net (online, Apache-2.0)](https://www.diagrams.net/) to draw flow and architecture charts. Use [Shotcut (21.12.24, GPL-3.0)](https://shotcut.org/) to cut and edit the videos and gifs. Use [GeoGebra (online, GPL-3.0)](https://www.geogebra.org/) to draw shapes to help debug computational geometry algorithms in TaichiGAME. You can get all resources from [TaichiGAME-res repo](https://github.com/maksyuki/TaichiGAME-res).

## Reference
[1] _Physically Based Rendering section 4.3 [BVH](https://www.pbr-book.org/3ed-2018/Primitives_and_Intersection_Acceleration/Bounding_Volume_Hierarchies) and [DBVH](https://box2d.org/files/ErinCatto_DynamicBVH_GDC2019.pdf)_, GDC2019, Erin Catto, Blizzard Entertainment <span id="id_dbvt"></span>

[2]  _Foundations of Physically Based Modeling and Animation_ By Donald H. House, John C. Keyser <span id="id_fpbma"></span>

[3] _Real-Time Collision Detection_ By Christer Ericson <span id="id_rtcd"></span>

[4] _Game Programming Gems 7_ By Scott Jacobs <span id="id_gpg7"></span>

[5] [Continuous Collision](https://box2d.org/files/ErinCatto_ContinuousCollision_GDC2013.pdf), GDC2013, Erin Catto, @erin_catto Principle Software Engineer, Blizzard

[6] [Constrained Dynamics](https://dyn4j.org/tags#constrained-dynamics), dyn4j, a java collision detection and phyics engine

[7] [Contact Manifolds](https://box2d.org/files/ErinCatto_ContactManifolds_GDC2007.pdf), GDC2007, Erin Catto Blizzard Entertainment
