# policyengine-core

This repository contains the core infrastructure for PolicyEngine sites in order to reduce code duplication. Namely, `policyengine`, a Python package which contains the server-side implementations, and `policyengine-core`, a React library containing high-level components to build the client-side interface.

## Development

First, install using `make install`. Then, to debug the client, run `make debug-client`, or to debug the server, run `make debug-server`.

If your changes involve the server, change `useLocalServer = false;` to `useLocalServer = true;` in `src/countries/country.jsx`.

If you don't have access to the UK Family Resources Survey, you can still run the UK population-wide calculator on an anonymised version. To do that, instead of running `make debug-server`, run `POLICYENGINE_SYNTH_UK=1 make debug-server`