---
title: ReCoDE Exemplars
hide:
  - toc
  - navigation
search:
  exclude: true
---

<style>
  /* Full-page background setup */
  body {
    margin: 0;
    font-family: Arial, sans-serif;
  }

  /* Background overlay for the image */
  .background-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-image: url('./assets/img/group_computing.png');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
    opacity: 1;
    transition: opacity 0.2s ease-out;
    z-index: -1; /* Ensure it stays behind all content */
  }

  /* Main page content to overlay on top */
  .content {
    position: relative; /* Ensures it overlays above the background */
    z-index: 1; /* Stack above background overlay */
    padding: 20px;
  }

  .grid.cards {
    background-color: rgba(255, 255, 255, 0.4); /* Match opacity with content div */
    padding: 20px;
    margin: 20px;
    border-radius: 10px;

  }
</style>

<div class="background-overlay" id="backgroundOverlay"></div>

<div class="content">
    <div style="background-color: rgba(250, 250, 250, 0.80); padding: 20px; margin: 20px; border-radius: 10px;">
    <h1 style="text-align: center;"><strong>Welcome to ReCoDE</strong></h1>
    <h2 style="text-align: center;">Research Computing and Data Science Exemplars for Learning and Teaching</h2>

    <p><strong>A set of research computing exemplars with rich learning annotation for doctoral students and researchers who are working on projects with significant computational aspects.</strong></p>

    <p>Keep scrolling to see all of our exemplars...</p>
    </div>
</div>

<script>
  window.addEventListener("scroll", function() {
    const scrollPosition = window.scrollY;
    const fadeStart = 0; // Starting point for fade effect
    const fadeEnd = 400;   // End point for fade effect
    const fadeDistance = fadeEnd - fadeStart;

    // Calculate opacity based on scroll position
    let opacity = 1 - Math.min(Math.max((scrollPosition - fadeStart) / fadeDistance, 0), 1);

    // Update overlay opacity
    document.getElementById("backgroundOverlay").style.opacity = opacity;
  });
</script>









<div class="grid cards" markdown>

-  <big>__Mathematics of the Mandlebrot Set__</big>
    <br>Juan Carlos Bilbao-Ludena

    ---
    
    ![Mandlebrot](./assets/img/exemplars/mandelbrot.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/mandelbrot)</big>

    [:octicons-tag-24: C++, Parallel Computing, Visualisation](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-Exploration-Mandelbrot-Set)</small>

-  <big>__Neural Ordinary Differential Equations__</big>
    <br>Ekin Ozturk

    ---
    
    ![Neural ODEs](./assets/img/exemplars/neuralodes.gif)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/neuralodes)</big>

    [:octicons-tag-24: Python, Machine Learning, PyTorch, Ordinary Differential Equations](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-NeuralODEs)</small>

-  <big>__Predicting Colitis<br>with Penalised Regression__</big>
    <br>Fabio Feser

    ---
    
    ![Neural ODEs](./assets/img/exemplars/penalisedreg.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/penalisedreg)</big>

    [:octicons-tag-24: R, Statistics, Logistic Regression](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-penalised-reg/)</small>

-  <big>__Environmental Literature Analysis<br>with BERTopic & RoBERTa__</big>
    <br>Yurong Yu

    ---
    
    ![Environmental lit](./assets/img/exemplars/environmentlit.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/environmentlit)</big>

    [:octicons-tag-24: Topic Modelling, BERTopic, RoBERTa](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-Analysis-of-environmental-literature-with-BERTopic-and-RoBERTa)</small>

-  <big>__Cracking Time's Code:<br>Survival Analysis of Large Datasets__</big>
    <br>Valentina Quintero Santofimio

    ---
    
    ![Cracking Time](./assets/img/exemplars/crackingtime.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/crackingtime)</big>

    [:octicons-tag-24: R, Epidemiology, Statistics](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-SurvivalAnalysis/)</small>

-  <big>__Hand-eye Calibration of Medical Robots__</big>
    <br>Zejian Cui

    ---
    
    ![Hand-eye Calibration](./assets/img/exemplars/handeyecalib.jpeg)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/handeyecalib)</big>

    [:octicons-tag-24: C++, Robotics, Computer Vision](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-HandEyeCalibration)</small>

-  <big>__Turing Patterns & Partial Differential Equations__</big>
    <br>Elliot James Badcock

    ---
    
    ![Turing Patterns](./assets/img/exemplars/turingpatterns.gif)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/turingpatterns)</big>

    [:octicons-tag-24: Fortran, Fortran Package Manager, Partial Differential Equations](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-Turing-Patterns-and-Partial-Differential-Equations)</small>

-  <big>__Deep Learning Best Practices__</big>
    <br>Antoni Bigata Casademunt

    ---
    
    ![Deep Learning](./assets/img/exemplars/deeplearning.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/deeplearning)</big>

    [:octicons-tag-24: Python, PyTorch, Machine Learning](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-DeepLearning-Best-Practices)</small>

-  <big>__SPH Solver for 2D Navier-Stokes__</big>
    <br>Georgios Efstathiou

    ---
    
    ![SPH Navier-Stokes](./assets/img/exemplars/sphnavierstokes.gif)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/sphnavierstokes)</big>

    [:octicons-tag-24: Python, C++, Boost](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-SPH-solver-2D-NS/)</small>

-  <big>__Hidden Markov Models for the discovery of behavioural states__</big>
    <br>Laurence Blackhurst

    ---
    
    ![Hidden Markov](./assets/img/exemplars/hiddenmarkov.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/hiddenmarkov)</big>

    [:octicons-tag-24: Python, Pandas, Machine Learning](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-HMMs-for-the-discovery-of-behavioural-states)</small>

-  <big>__Decoding Market Signals__</big>
    <br>Benjamin Scharpf

    ---
    
    ![Decoding Market Signals](./assets/img/exemplars/decodingmarketsignals.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/decodingmarketsignals)</big>

    [:octicons-tag-24: Finance, Pandas, Logistic Regression](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-DecodingMarketSignals)</small>

-  <big>__Binary Classification of Patent Texts__</big>
    <br>Egheosa Ogbomo

    ---
    
    ![AI for Patents](./assets/img/exemplars/aiforpatents.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/aiforpatents)</big>

    [:octicons-tag-24: Python, Tensorflow, Sci-kit Learn](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-AIForPatents)</small>

-  <big>__CNNs for the Cosmic Dawn__</big>
    <br>Kimeel Sooknunan

    ---
    
    ![Cosmic Dawn](./assets/img/exemplars/cosmicdawn.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/cosmicdawn)</big>

    [:octicons-tag-24: Python, Tensorflow, Sci-kit Learn](./tags)
    

    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-FirstDawn)</small>

-  <big>__Solving SDEs with Euler-Maruyama__</big>
    <br>Antonio Malpica-Morales

    ---
    
    ![Euler-Maruyama](./assets/img/exemplars/eulermaruyama.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/eulermaruyama)</big>

    [:octicons-tag-24: Python, NumPy, Matplotlib](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDe-Euler-Maruyama)</small>

-  <big>__Multi-channel Python GUI__</big>
    <br>Shuaixun Wang

    ---
    
    ![Python GUI](./assets/img/exemplars/pythongui.jpg)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/pythongui)</big>

    [:octicons-tag-24: Python, NumPy, GUI](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE-PythonGUI)</small>

-  <big>__RNA Sequencing Analysis__</big>
    <br>Jack Gisby

    ---
    
    ![RNA Sequencing](./assets/img/exemplars/rnaseq.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/rnaseq)</big>

    [:octicons-tag-24: R, bash, Conda, Nextflow](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE_rnaseq_pipeline)</small>

-  <big>__Bayesian Inference for SARS-CoV-2 Transmission Modelling__</big>
    <br>Bethan C Daniels

    ---
    
    ![IDMS](./assets/img/exemplars/idms.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/idms)</big>

    [:octicons-tag-24: R, Stan](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE_IDMS)</small>

-  <big>__1-Dimensional Neutron Diffusion Solver__</big>
    <br>Jack Trainor

    ---
    
    ![Neutron Diffusion](./assets/img/exemplars/diffusion.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/diffusion)</big>

    [:octicons-tag-24: Fortran, OOP](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE_Diffusion_Code)</small>


-  <big>__Markov Chain Monte Carlo for fun and profit__</big>
    <br>Tom Hodson

    ---
    
    ![MCMC](./assets/img/exemplars/mcmc.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/mcmc)</big>

    [:octicons-tag-24: Python, TDD, Optimisation](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/ReCoDE_MCMCFF)</small>

-  <big>__PyTorch for end-to-end training of a deep learning model__</big>
    <br>Emily Muller

    ---
    
    ![Perceptions](./assets/img/exemplars/perceptions.png)

    <big>[__:octicons-arrow-right-24: Get Started__](./exemplars/perceptions)</big>

    [:octicons-tag-24: Python, pyTorch, Machine Learning](./tags)
    
    <small>:fontawesome-brands-github: [See it on GitHub](https://github.com/ImperialCollegeLondon/recode-perceptions)</small>

</div>
