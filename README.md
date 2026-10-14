# AI for Engineering: In-Browser Lab Demo

A proof of concept: interactive engineering-AI labs that run entirely in the browser, published as a Jupyter Book with JupyterLite (Python via Pyodide/WebAssembly). No server and no student installs.

**Live site:** https://ashejim.github.io/engineering-ai-lab-demo/

## Contents

- `lab/` — guided lab: evaluate whether a pre-trained physics-informed neural network (PINN) respects energy conservation.
- `bo/` — plan a simulation campaign with Bayesian optimization and compare it with random search under a fixed budget.
- `content/` — shared physics module, numpy MLP, pre-trained weights, and data.

All physics and numbers are simplified and illustrative.

## Build locally

```bash
pip install -r requirements.txt
jupyter-book build .
cd _build/html && python -m http.server 8080
```

Deployment to GitHub Pages runs from `.github/workflows/deploy.yml` (Settings → Pages → Source: GitHub Actions).
