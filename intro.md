# AI for Engineering: In-Browser Lab Demo

**A proof of concept** by Jim Ashe

This site shows how hands-on labs for an engineering-AI course can run entirely in the browser. The notebooks use JupyterLite, so Python runs locally through WebAssembly (Pyodide). There's no server to maintain and nothing for students to install.

Both activities use the same case: a liquid-cooled cold plate under a battery module, with simplified, illustrative physics.

| Activity | What it shows |
|---|---|
| **Lab: Evaluating a Physics-Constrained Model** | Load a pre-trained physics-informed neural network (PINN), complete one guided cell, and check whether the model actually respects energy conservation. |
| **Planning Simulations with Bayesian Optimization** | Plan a limited simulation campaign against a black-box simulator, and compare Bayesian optimization with random search under the same budget. |

## Technical notes

- **Kernel:** Python (Pyodide), running in the browser. No server required.
- **Packages:** numpy, pandas, matplotlib, scikit-learn.
- **Shared assets** (`content/`): the physics module, a small numpy MLP, pre-trained weights, and dataset partitions, bundled into the JupyterLite filesystem.
- Models are provided as pre-trained numpy artifacts, so no PyTorch or GPU is needed.
- All numbers are illustrative, not engineering specifications.
