# UmbrellaRL

## Generic solution for reinforcement learning problems ☂️

Version 1.0.0 will be a full tabular solution method release. See below for currently implemented & planned features.

UmbrellaRL is intended to ease some of the requirements for working with reinforcement learning problems. By providing logic & mathematics, the UmbrellaRL agent only requires an environment to interact with.
This allows for faster solution methods to reinforcement learning problems.

## Implementations

- [ ] Tabular Solution Methods
  - [ ] Dynamic programming
    - [x] Policy Evaluation
    - [ ] Policy Improvement
    - [ ] Policy Iteration
    - [ ] Value Iteration
    - [ ] Asynchronous methods
    - [ ] Generalised Policy Iteration
  - [ ] Monte Carlo Methods
  - [ ] Temporal Difference Learning
  - [ ] n-step Bootstrapping

- [ ] Approximate Solution Methods

## Usage

UmbrellaRL comes with abstract Agent, Environment & Policy generic classes. These abstract generic classes are intended to be inherited from to define the solution to your problem.
UmbrellaRL also comes with various types to make implementation easier.
A 'Solutions' directory is included in the package. The modules within the 'Solutions' directory are commonly found reinforcement learning problems that implement UmbrellaRL's classes & types.
The modules within the 'Solutions' directory could also function as tutorials.
