import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.write('# Simulating logic gates with Neural Networks')
st.write('## Using CrysX-Neural Network library `crysx_nn`')

nInputs = 2
neurons_per_layer = [3, 1] # Neurons per layer (excluding the input layer)
activation_func_names = ['Tanh_offset', 'Tanh_offset']
nLayers = len(neurons_per_layer)
nEpochs=10**4
batchSize = 4 # No. of input samples to process at a time for optimization

inputs = []
outputs = []

def add_act_func(activation_func_names, name):
    activation_func_names.append(name)

def del_act_func(activation_func_names, name):
    activation_func_names.append(name)

from crysx_nn import network
model = network.nn_model(nInputs=nInputs, neurons_per_layer=neurons_per_layer, activation_func_names=activation_func_names, batch_size=batchSize, device='CPU', init_method='Xavier') 
model.visualize(filename='nnv_streamlit.png')

st.image('nnv_streamlit.png', caption='Neural Network Visualization')