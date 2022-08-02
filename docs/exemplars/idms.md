---
title: Transmission
tags:
  - R
  - Stan
---
# Transmission Modelling

**Bayesian inference for SARS-CoV-2 transmission modelling, developed by Bethan Cracknell Daniels.**

## About

The aim of this exemplar is to demonstrate how to design and fit a mathematical model of disease transmission to real data, in order to estimate key epidemiological parameters and inform public health responses. Specifically, we will model the emergence of the SARS-CoV-2 variant of concern Omicron in Gauteng, South Africa. To fit the model, we use Stan, a free, accessible and efficient Bayesian inference software. Adopting a Bayesian approach to model fitting allows us to account for uncertainty, which is especially important when modelling a new pathogen or variant. The transmission model uses compartments to track the population’s movement between states, for instance from susceptible to infectious. By fitting a compartmental model to genomic and epidemiological surveillance data, we will recreate the transmission dynamics of Omicron and other circulating variants, and estimate key epidemiological parameters. Together these estimates are useful for guiding policy, especially in the early stages of an emerging variant or pathogen, when there are lots of unknowns. Developed by [Bethan Cracknell Daniels](https://github.com/bnc19/).

## Link to material

The full source code for this project is on [GitHub](https://github.com/bnc19/ReCoDE_IDMS).
Start working through the material using the [README](https://github.com/bnc19/ReCoDE_IDMS#bayesian-inference-for-sars-cov-2-transmission-modelling-using-stan)
