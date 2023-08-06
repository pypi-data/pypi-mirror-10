---
layout: post
title: PyDiagram Usage Tips
author: Yi-Xin Liu
image:
    feature: software-post.jpg
categories: [Software]
tags: [PyDiagram, Python, Documentation]
---

### Check Additional Phases

If one wants to check additional phases around some phase boundary points, one can simply add these phases into the `predictor.boundary` section in the project configuration file.

**Example**.

Suppose you initially have following configurations:

```yaml
predictor:
    boundary:  # list of phase pairs identifying a phase boundary
        - pairs:    [['DIS', 'HEX']]
          extra:    ['LAM']  # list of extra phases to be considered
```

Normally, you will have DIS, HEX, and LAM phases simulated. Then, suppose you want to know whether Gyroid can be more stable around those DIS-HEX boundary points, you can add it to the `extra` list such as

```yaml
predictor:
    boundary:  # list of phase pairs identifying a phase boundary
        - pairs:    [['DIS', 'HEX']]
          extra:    ['LAM', 'Gyroid']  # list of extra phases to be considered
```

Once you modify the configuration file, you need to restart PyDiagram.

### Run PyDiagram in Manual Mode

If one notices some failed simulations, one can manually delete these simulations and adds these simulations to the configuration file such as

```yaml
predictor:
    manual:
        - x:        [0.31, 0.32, 0.34, 0.36, 0.38]
          y:        [17.6]
          phases:   ['DIS']
          order:    False
          grid:     True
```

Then run PyDiagram as

```bash
pydiagram -m
```

to create new simulation jobs and submit them to the computational resources.

### Run DIS simulations for All Cases

- DIS simulations are very cheap.
- DIS simulations provide valuable information such as the free energy.
- Sometimes, we need DIS simulations results to determine the phase boundary points. For example, near LAM-HEX boundary where DIS-HEX boundary is also very close, if we create new simulations around LAM-HEX phase boundary points only for LAM and HEX, we may miss the DIS-HEX boundary points.
