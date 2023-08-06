<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Documentation][docs-shield]][documentation-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/manassharma07/crysx_nn">
    <img src="logo_crysx_nn.png" alt="Logo" width="320" height="200">
  </a> -->

<h3 align="center">crysx_nn</h3>

  <p align="center">
    A simplistic and efficient pure-python neural network library from Phys Whiz with CPU and GPU support.
    <br />
    <a href="https://github.com/manassharma07/crysx_nn/blob/main/Documentation.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/manassharma07/crysx_nn/blob/main/examples/Simulating_Logic_Gates.ipynb">View Demo</a>
    ·
    <a href="https://github.com/manassharma07/crysx_nn/issues">Report Bug</a>
    ·
    <a href="https://github.com/manassharma07/crysx_nn/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#citation">Citation</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/manassharma07/crysx_nn)

Neural networks are an integral part of machine learning.
The project provides an easy-to-use, yet efficient implementation that can be used in your projects or for teaching/learning purposes.

The library is written in pure-python with some optimizations using numpy, opt_einsum, and numba when using CPU and cupy for CUDA support. 

The goal was to create a framework that is efficient yet easy to understand, so that everyone can see and learn about what goes inside a neural network. After all, the project did spawn from a semester project on [CP_IV: Machine Learning course](https://friedolin.uni-jena.de/qisserver/rds?state=verpublish&status=init&vmfile=no&moduleCall=webInfo&publishConfFile=webInfo&publishSubDir=veranstaltung&veranstaltung.veranstid=187951) at the [University of Jena, Germany](https://www.uni-jena.de/en/).


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Cupy](https://cupy.dev/) (Optional)
* [NumPy](https://numpy.org) (Required)
* [numba](https://numba.pydata.org) (Required)
* [opt_einsum](https://optimized-einsum.readthedocs.io/en/stable/) (Required)
* [matplotlib](https://matplotlib.org) (Required)
* [nnv](https://pypi.org/project/nnv/) (Required)
* [pillow](https://pillow.readthedocs.io/en/stable/index.html) (Optional)
* [zipfile](https://docs.python.org/3/library/zipfile.html) (Optional)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

You need to have `python3` installed along with `pip`.

### Installation

There are many ways to install `crysx_nn`

1. Install the release (stable) version from [PyPi](https://pypi.org/project/crysx-nn/)
    ```sh
    pip install crysx_nn
    ```
2. Install the latest development version, by cloning the git repo and installing it. 
   This requires you to have `git` installed.
   ```sh
   git clone https://github.com/manassharma07/crysx_nn.git
   cd crysx_nn
   pip install .
   ```
3. Install the latest development version without `git`.
   ```sh
   pip install --upgrade https://github.com/manassharma07/crysx_nn/tarball/main
   ```

Check if the installation was successful by running python shell and trying to import the package 
```sh
python3
```
```python
Python 3.7.11 (default, Jul 27 2021, 07:03:16) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import crysx_nn
>>> crysx_nn.__version__
'0.1.0'
>>> 
```

   Finally download the example script ([here](https://github.com/manassharma07/crysx_nn/blob/main/examples/Simulating_Logic_Gates.py)) for simulating logic gates like AND, XOR, NAND, and OR,
   and try running it
   ```sh
   python Simluating_logic_gates.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The most important thing for using this library properly is to use 2D NumPy/Cupy arrays for defining the inputs and expected outputs (targets) for a network. 1D arrays for inputs and targets are not supported and will result in an error.

For example, let us try to simulate the logic gate AND. The AND gate takes two input bits and returns a single input bit.
The bits can take a value of either 0 or 1. The AND gate returns 1 only if both the inputs are 1, otherwise it returns 0.

The truth table of the AND gate is as follows

x1 | x2 | output 
--- | --- | --- 
0 | 0 | 0 
0 | 1 | 0 
1 | 0 | 0 
1 | 1 | 1 

The four possible set of inputs are 
```python
import numpy as np
inputs = np.array([[0.,0.,1.,1.],[0.,1.,0.,1.]]).T.astype('float32')
print(inputs)
print(inputs.dtype) 
```
Output:
```sh
[[0. 0.]
 [0. 1.]
 [1. 0.]
 [1. 1.]]
float32
```
Similarly, set the corresponding four possible outputs as a 2D numpy array
```python
# AND outputs
outputAND = np.array([0.,0.,0.,1.]) # 1D array
outputAND = np.asarray([outputAND]).T # 2D array
print('AND outputs\n', outputAND)
```
Output:
```sh
AND outputs
 [[0.]
 [0.]
 [0.]
 [1.]]
```
Next, we need to set some parameters of our Neural network
```python
nInputs = 2 # No. of nodes in the input layer
neurons_per_layer = [3,1] # Neurons per layer (excluding the input layer)
activation_func_names = ['Sigmoid', 'Sigmoid']
nLayers = len(neurons_per_layer)
eta = 0.5 # Learning rate
nEpochs=10**4 # For stochastic gradient descent
batchSize = 4 # No. of input samples to process at a time for optimization
```
Let us now create the neural network model using the above parameters
```python
from crysx_nn import network
model = network.nn_model(nInputs=nInputs, neurons_per_layer=neurons_per_layer, activation_func_names=activation_func_names, batch_size=batchSize, device='CPU', init_method='Xavier') 
```
Note: ```device='CPU'``` indicates that the we are going to be running the computations on the CPU. If you have cupy installed and a compatible GPU, then you could also use ```device='GPU'```. However, in that case the inputs and ouputs should also be cupy arrays instead of numpy arrays.
To check if the model was initialized correctly, you can check the model details as
```python
model.details()
```
Output:
```
----------------------------------------------------------------------------------
****Neural Network Model Details****
----------------------------------------------------------------------------------
Number of input nodes:  2
Number of layers (hidden+output):  2
Number of nodes in each layer (hidden & output):  [3, 1]
Activation function for each layer (hidden & output):   ['Sigmoid', 'Sigmoid']
Method used for weights and biases initialization:   Xavier
Batch Size:  4
Device:  CPU
Optimization method:  SGD
Learning rate:  0.5
----------------------------------------------------------------------------------
```
For a better understanding of our network, let us visualize it. 
```python
model.visualize()
```
Output:
![](https://www.bragitoff.com/wp-content/uploads/2021/12/Screenshot-2021-12-25-at-17.31.01.png)

Weights and biases are already initialized when you create the model using the ```'Xavier'``` method. 
Weights and biases are lists of 2D and 1D NumPy arrays, respectively (1 Numpy array for each layer). In our case, we have 2 layers (1 hidden+ 1 output), therefore, the list of Weights and Biases will have 2 NumPy arrays each.
You can also initialize them again using some other method as follows:
<!--```python
# Initial guesses for weights
w1 = 0.30
w2 = 0.55
w3 = 0.20
w4 = 0.45
w5 = 0.50
w6 = 0.35
w7 = 0.15
w8 = 0.40
w9 = 0.25

# Initial guesses for biases
b1 = 0.60
b2 = 0.05

# need to use a list instead of a numpy array, since the 
#weight matrices at each layer are not of the same dimensions
weights = [] 
# Weights for layer 1 -> 2
weights.append(np.array([[w1,w4],[w2, w5], [w3, w6]]))
# Weights for layer 2 -> 3
weights.append(np.array([[w7, w8, w9]]))
# List of biases at each layer
biases = []
biases.append(np.array([b1,b1,b1]))
biases.append(np.array([b2]))

weightsOriginal = weights
biasesOriginal = biases

print('Weights matrices: ',weights)
print('Biases: ',biases)
``` -->

```python
model.init_params(method='NormXavier')
print('Initial Weights:\n',model.init_weights)
print('Initial Biases:\n',model.init_biases)
```
Output:
``` 
Initial Weights:
 [array([[-0.66735507,  1.89981375],
       [ 1.58135381,  0.30297808],
       [-1.02875636,  0.39637066]]), array([[ 1.14150595,  0.86579216, -1.50878406]])]
Initial Biases:
 [array([0., 0., 0.]), array([0.])]
```
Finally it is time to train our neural network. We will use mean squared error (MSE) loss function as the metric of performance. Currently, only stochastic gradient descent is supported.
```python
# Run optimization
model.optimize(inputs, outputAND, lr=0.5,nEpochs=nEpochs,loss_func_name='MSE', miniterEpoch=1, batchProgressBar=False, miniterBatch=100)
```
The optimization saves the optimized weights ```model.weights``` and biases ```model.biases``` as well as the error ```model.errors``` at each epoch in the attributes of the `nn_model` object.

We can then plot the training loss at each epoch
```python
import matplotlib.pyplot as plt
# Plot the error vs epochs
plt.plot(model.errors)
plt.yscale('log')
plt.show()
```
Output:
![](https://www.bragitoff.com/wp-content/uploads/2021/12/Screenshot-2021-12-25-at-18.56.01.png)

Finally, you can make predictions using the optimized network using the following code
```python
predictions, error = model.predict(inputs, outputAND, loss_func_name='MSE')
print('Input:\n',inputs)
print('Prediction:\n',predictions)
print('Expected Output:\n',outputAND)
print('New Average Error with optimized weights:\n', error)
```
OUTPUT:
```
Input:
 [[0. 0.]
 [0. 1.]
 [1. 0.]
 [1. 1.]]
Prediction:
 [[6.51744058e-05]
 [8.16272136e-03]
 [5.94678339e-03]
 [9.90297134e-01]]
Expected Output:
 [[0.]
 [0.]
 [0.]
 [1.]]
New Average Error with optimized weights:
 4.903602650103742e-05
```

_For more examples, please refer to the [Examples Section](https://github.com/manassharma07/crysx_nn/tree/main/examples)_

CrysX-NN (crysx_nn) also provides CUDA support by using cupy versions of all the features ike activation functions, loss functions, neural network calculations, etc.
Note: For small networks the Cupy versions may actually be slower than CPU versions. But the benefit becomes evident as you go beyond 1.5 Million parameters.
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Features -->
## Features

- [x] Efficient implementations of activation functions and their gradients
    - [x] Sigmoid, Sigmoid_grad
    - [x] ReLU, ReLU_grad
    - [x] Softmax, Softmax_grad  
    - [x] Softplus, Sofplus_grad  
    - [x] Tanh, Tanh_grad 
    - [x] Tanh_offset, Tanh_offset_grad  
    - [x] Identity, Identity_grad 
- [x] Efficient implementations of loss functions and their gradients
    - [x] Mean squared error 
    - [x] Mean absolute error
    - [x] Binary cross entropy  
    - [x] Categorical cross entropy  
- [x] Several methods for weights initialization
    - [x] ```'random1'```, ```'random2'```, ```'random3'```
    - [x] ```'Xavier'```
    - [x] ```'NormXavier'```
    - [x] ```'He'```
- [x] Neural network optimization using 
    - [x] Stochastic Gradient Descent
- [x] Support for batched inputs, i.e., supplying a matrix of inputs where the columns correspond to features and rows to the samples
- [x] Support for GPU through Cupy `pip install cupy-cuda102` (Tested with CUDA 10.2)
- [x] JIT compiled functions when possible for efficiency
- [x] Object oriented

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] More activation functions
    - [ ] LeakyReLU, Swish, Mish, etc.
- [ ] More loss functions
    - [ ] Hinge loss, and others
- [ ] Optimization algorithms apart from Stochastic Gradient Descent, like ADAM, RMSprop, etc.
- [ ] Implement regularizers
- [ ] Batch normalization and layer normalization
- [ ] Dropout
- [ ] Early stopping
- [ ] Some metric functions, although there is no harm in using `sklearn` for that 

See the [open issues](https://github.com/manassharma07/crysx_nn/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Manas Sharma - [@manassharma07](https://twitter.com/manassharma07) - feedback@bragitoff.com

Project Link: [https://github.com/manassharma07/crysx_nn](https://github.com/manassharma07/crysx_nn)

Project Documentation: [https://bragitoff.com](https://www.bragitoff.com/crysx-neural-network-crysx_nn/)

Blog: [https://bragitoff.com](https://bragitoff.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Lecture notes by [Prof. Dr. Bernd Brügmann](https://www.physik.uni-jena.de/en/bruegmann)
* [Ondřej  Zelenka](https://www.researchgate.net/profile/Ondrej-Zelenka) for useful discussions.
* [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com) by [Michael Nielsen](https://michaelnielsen.org)
* [A high-bias, low-variance introduction to Machine Learning for physicists](https://arxiv.org/abs/1803.08823) by Mehta et al., 2019
* [Deep Learning](https://www.deeplearningbook.org) by Goodfellow et al., 2016

<p align="right">(<a href="#top">back to top</a>)</p>

## Citation
If you use this library and would like to cite it, you can use:
```
 M. Sharma, "CrysX-NN: Neural Network libray", 2021. [Online]. Available: https://github.com/manassharma07/crysx_nn. [Accessed: DD- Month- 20YY].
```
or:
```
@Misc{,
  author = {Manas Sharma},
  title  = {CrysX-NN: Neural Network libray},
  month  = december,
  year   = {2021},
  note   = {Online; accessed <today>},
  url    = {https://github.com/manassharma07/crysx_nn},
}
```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/manassharma07/crysx_nn.svg?style=for-the-badge
[contributors-url]: https://github.com/manassharma07/crysx_nn/contributors
[forks-shield]: https://img.shields.io/github/forks/manassharma07/crysx_nn.svg?style=for-the-badge
[forks-url]: https://github.com/manassharma07/crysx_nn/network/members
[stars-shield]: https://img.shields.io/github/stars/manassharma07/crysx_nn.svg?style=for-the-badge
[stars-url]: https://github.com/manassharma07/crysx_nn/stargazers
[issues-shield]: https://img.shields.io/github/issues/manassharma07/crysx_nn.svg?style=for-the-badge
[issues-url]: https://github.com/manassharma07/cysx_nn/issues
[license-shield]: https://img.shields.io/github/license/manassharma07/crysx_nn.svg?style=for-the-badge
[license-url]: https://github.com/manassharma07/cysx_nn/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/manassharma07
[product-screenshot]: https://www.bragitoff.com/wp-content/uploads/2021/12/logo_crysx_nn.png
[documentation-url]: https://github.com/manassharma07/crysx_nn/blob/main/Documentation.md
[docs-shield]: https://img.shields.io/badge/-docs-blue.svg?style=for-the-badge&logo=documentation&colorB=389