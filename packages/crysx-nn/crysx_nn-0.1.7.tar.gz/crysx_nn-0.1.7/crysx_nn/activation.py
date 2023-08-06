'''
Activation functions and their gradients
crysx_nn 
Manas Sharma
feedback@bragitoff.com
https://www.bragitoff.com
'''

'''DEVELOPER NOTES:
1. Whenever adding a new activation function, use Numba for CPU version and cupy for CUDA version.
2. After adding a function here, also update the lists in utils.py
3. Don't forget to add the gradient of activation functions as well with the suffix '_grad'.
4. Use the suffix '_cupy' for CUDA versions of activation functions.
5. Use the suffix '_grad_cupy' for CUDA versions of gradient of activation functions.
'''

### ------- USEFUL REFERENCES -------------###
# https://www.analyticsvidhya.com/blog/2021/04/activation-functions-and-their-derivatives-a-quick-complete-guide/
# https://dustinstansbury.github.io/theclevermachine/derivation-common-neural-network-activation-functions
# https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6

# List of PyTorch Activation functions https://pytorch.org/docs/stable/nn.html#non-linear-activations-weighted-sum-nonlinearity
# List of TensorFlow Activation Functions https://www.tensorflow.org/api_docs/python/tf/keras/activations

from numba import vectorize,jit,njit,prange,set_num_threads,get_num_threads 
import numpy as np
try:
    import cupy as cp                     
except ImportError:
    print('Warning: CuPy could not be imported! You can only use CPU for computations.')



@njit(cache=True,fastmath=True)  # Best implementation (VERY FAST)
def Softmax(x):
    '''
    Performs the Softmax activation on a given set of inputs
    Note: Works for 2D arrays only(rows for samples, columns for nodes/outputs)

    Parameters:
    x:  (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns:
    Softmax activated (N,k) ndarray (N: no. of samples, k: no. of nodes)
    '''
    # The following is wrong! We should be taking hte maximum of each row of data and then subtracting that
    # e_x = np.exp(x - np.max(x)) # For stability as it is prone to overflow and underflow
    # Alternative 1 (Doesn't work with NUMBA)
    # max_x = np.amax(x, 1).reshape(x.shape[0],1)
    # e_x = np.exp(x - max_x)
    # return e_x / e_x.sum(axis=1, keepdims=True) # only difference
    # Alternative 2
    max_x = np.zeros((x.shape[0],1),dtype=x.dtype)
    for i in range(x.shape[0]):
        max_x[i,0] = np.max(x[i,:])
    e_x = np.exp(x - max_x)
    return e_x / e_x.sum(axis=1).reshape((-1, 1)) # Alternative of keepdims=True for Numba compatibility

@njit(cache=True,fastmath=True)
def Softmax_grad(x): # Best implementation (VERY FAST)
    '''
    Returns the jacobian of the Softmax function wrt the given set of inputs.
    
    Parameters:
    x: should be a 2d array where the rows correspond to the samples
        and the columns correspond to the nodes. [(N,k) ndarray (N: no. of samples, k: no. of nodes)]
    
    Returns: 
    jacobian of the Softmax activated values wrt to the input parameter x
    '''
    s = Softmax(x)
    a = np.eye(s.shape[-1])
    temp1 = np.zeros((s.shape[0], s.shape[1], s.shape[1]),dtype=x.dtype)
    temp2 = np.zeros((s.shape[0], s.shape[1], s.shape[1]),dtype=x.dtype)
    # Einsum is unsupported with Numba (nopython mode)
    # temp1 = np.einsum('ij,jk->ijk',s,a)
    # temp2 = np.einsum('ij,ik->ijk',s,s)
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            for k in range(s.shape[1]):
                temp1[i,j,k] = s[i,j]*a[j,k]
                temp2[i,j,k] = s[i,j]*s[i,k]
    
    return temp1-temp2

@njit(cache=True,fastmath=True, parallel=True)
def Sigmoid(x): # Also known as logistic/soft step or even expit in scipy.special
    '''
    Performs the Sigmoid activation on a given set of inputs
    Note: Works for 2D arrays only(rows for samples, columns for nodes/outputs)
    
    Parameters:
    x:  (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns:
    Sigmoid activated (N,k) ndarray (N: no. of samples, k: no. of nodes)
    '''
    # The following is susceptible to overflow/underflow issues.
    # return 1/(1+np.exp(-x))
    # The following are some stable alternatives
    # Alternative 1 (Doesn't work with Numba as boolean masking (fancy indexing) is not supported for 2D arrays -https://stackoverflow.com/questions/57915632/numba-nopython-mode-cannot-accept-2-d-boolean-indexing )
    # Hao Peng's answer from here https://stackoverflow.com/questions/51976461/optimal-way-of-defining-a-numerically-stable-sigmoid-function-for-a-list-in-pyth
    # pos_mask = (x >= 0)
    # Boolean array inversion is faster than another comparison
    # neg_mask = ~pos_mask
    # z = np.zeros_like(x)
    # z[pos_mask] = np.exp(-x[pos_mask])
    # z[neg_mask] = np.exp(x[neg_mask])
    # top = np.ones_like(x)
    # top[neg_mask] = z[neg_mask]
    # return top / (1. + z)
    # Alternative 2 (Excruciatingly slow)
    # Neil G's answer from here https://stackoverflow.com/questions/3985619/how-to-calculate-a-logistic-sigmoid-function-in-python
    # return np.exp(-np.logaddexp(0., -x))
    # Alternative 3 (fastest implementation)
    # Works only for 2D arrays
    output = np.zeros((x.shape[0],x.shape[1]),dtype=x.dtype)
    for i in prange(x.shape[0]):
        for j in prange(x.shape[1]):
            x_val = x[i,j]
            if x_val>=0:
                output[i,j] = 1. / ( 1. + np.exp(-x_val) )
            else:
                e_x = np.exp(x_val)
                output[i,j] = e_x / ( 1. + e_x )
    return output


@njit(cache=True,fastmath=True)
def Sigmoid_grad(x):
    '''
    Returns the gradient (derivative) of the Sigmoid function wrt the given set of inputs.
    
    Parameters:
    x: (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns: 
    gradient of the Sigmoid activated values wrt to the input parameter x
    '''
    e_x = np.exp(-x)
    return e_x/(e_x+1)**2

@njit(cache=True,fastmath=True)
def ReLU(x):
    '''
    Performs the ReLU (Rectified Linear Unit) activation on a given set of inputs
    Note: Works for 2D arrays only(rows for samples, columns for nodes/outputs)
    
    Parameters:
    x:  (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns:
    ReLU activated (N,k) ndarray (N: no. of samples, k: no. of nodes)
    '''
    # Broadcasting seems expensive compared to TF and PyTorch
    # return np.maximum(0.,x)
    # a = np.zeros(x.shape,dtype=np.float32)
    # return np.maximum(a,x)
    return x * (x > 0) # This has been the fastest till date

@njit(cache=True,fastmath=True)
def ReLU_grad(x):
    '''
    Returns the gradient (derivative) of the ReLU function wrt the given set of inputs.
    
    Parameters:
    x: (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns: 
    gradient of the ReLU activated values wrt to the input parameter x
    '''
    return np.greater(x, 0.).astype(x.dtype)

@njit(cache=True,fastmath=True)
def Tanh_offset(x):
    '''
    Performs the Tanh_offset activation on a given set of inputs
    Note: Works for 2D arrays only(rows for samples, columns for nodes/outputs)
    
    Parameters:
    x:  (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns:
    Tanh_offset activated (N,k) ndarray (N: no. of samples, k: no. of nodes)
    '''
    return 0.5*(1.+np.tanh(x))

@njit(cache=True,fastmath=True)
def Tanh_offset_grad(x):
    '''
    Returns the gradient (derivative) of the Tanh_offset function wrt the given set of inputs.
    
    Parameters:
    x: (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns: 
    gradient of the Tanh_offset activated values wrt to the input parameter x
    '''
    return 1./(np.cosh(2.*x)+1.)

@njit(cache=True,fastmath=True)
def Tanh(x):
    '''
    Performs the Tanh activation on a given set of inputs
    Note: Works for 2D arrays only(rows for samples, columns for nodes/outputs)
    
    Parameters:
    x:  (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns:
    Tanh activated (N,k) ndarray (N: no. of samples, k: no. of nodes)
    '''
    return np.tanh(x)

@njit(cache=True,fastmath=True)
def Tanh_grad(x):
    '''
    Returns the gradient (derivative) of the Tanh function wrt the given set of inputs.
    
    Parameters:
    x: (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns: 
    gradient of the Tanh activated values wrt to the input parameter x
    '''
    return 1.-np.tanh(x)**2 # sech^2{x}

@njit(cache=True,fastmath=True)
def Identity(x):
    '''
    Performs the Identity activation on a given set of inputs
    
    Parameters:
    x:  input ndarray
    
    Returns:
    Identity activated ndarray 
    '''
    return x

@njit(cache=True,fastmath=True)
def Identity_grad(x):
    '''
    Returns the gradient (derivative) of the Identity function wrt the given set of inputs.
    
    Parameters:
    x: (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns: 
    gradient of the Idnentity activated values wrt to the input parameter x
    '''
    return np.ones(x.shape, dtype=x.dtype)

@njit(cache=True,fastmath=True)
def Softplus(x): 
    '''
    Performs the Softplus activation on a given set of inputs
    
    Parameters:
    x: (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns:
    Softplus activated ndarray 
    '''
    # Reference: https://stackoverflow.com/questions/44230635/avoid-overflow-with-softplus-function-in-python
    return np.log1p(np.exp(-np.abs(x))) + np.maximum(x, 0)
    # np.log(1 + np.exp(-np.abs(x))) + np.maximum(x,0)

@njit(cache=True,fastmath=True)
def Softplus_grad(x): # This is simply the sigmoid function
    '''
    Returns the gradient (derivative) of the Softplus function wrt the given set of inputs.
    
    Parameters:
    x: (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns: 
    gradient of the Softplus activated values wrt to the input parameter x
    '''
    # The following would be susceptible to over/underflow just like th Sigmoid function
    # return np.divide(1.,1.+np.exp(-x))
    # Use this instead
    return Sigmoid(x)
    


###-----------CUPY----------------
def Softmax_cupy(x):
    '''
    Performs the Softmax activation on a given set of inputs
    Note: Works for 2D arrays only(rows for samples, columns for nodes/outputs)
    
    Parameters:
    x:  (N,k) ndarray (N: no. of samples, k: no. of nodes)
    
    Returns:
    Softmax activated (N,k) ndarray (N: no. of samples, k: no. of nodes)
    '''
    max_x = cp.amax(x, 1).reshape(x.shape[0],1)
    e_x = cp.exp(x - max_x) # For stability as it is prone to overflow and underflow
#     return e_x / e_x.sum(axis=1, keepdims=True) # only difference
    return e_x / e_x.sum(axis=1).reshape((-1, 1)) # Alternative of keepdims=True for Numba compatibility

def Softmax_grad_cupy(x): # Best implementation (VERY FAST)
    
    s = Softmax_cupy(x)
    a = cp.eye(s.shape[-1])
    temp1 = cp.zeros((s.shape[0], s.shape[1], s.shape[1]),dtype=cp.float32)
    temp2 = cp.zeros((s.shape[0], s.shape[1], s.shape[1]),dtype=cp.float32)
    # for i in range(s.shape[0]):
    #     for j in range(s.shape[1]):
    #         for k in range(s.shape[1]):
    #             temp1[i,j,k] = s[i,j]*a[j,k]
    #             temp2[i,j,k] = s[i,j]*s[i,k]
    temp1 = cp.einsum('ij,jk->ijk',s,a)
    temp2 = cp.einsum('ij,ik->ijk',s,s)
    return temp1-temp2

def Sigmoid_cupy(x): # Also known as logistic/soft step or even expit in scipy.special
    # The following is susceptible to overflow/underflow issues.
    # return 1/(1+np.exp(-x))
    # The following are some stable alternatives
    # Alternative 1 (Slower than logaddexp, when using cupy but with numpy this was faster)
    # Hao Peng's answer from here https://stackoverflow.com/questions/51976461/optimal-way-of-defining-a-numerically-stable-sigmoid-function-for-a-list-in-pyth
    # pos_mask = (x >= 0)
    # # Boolean array inversion is faster than another comparison
    # neg_mask = ~pos_mask
    # z = cp.zeros_like(x)
    # z[pos_mask] = cp.exp(-x[pos_mask])
    # z[neg_mask] = cp.exp(x[neg_mask])
    # top = cp.ones_like(x)
    # top[neg_mask] = z[neg_mask]
    # return top / (1. + z)
    # Alternative 2 
    # Neil G's answer from here https://stackoverflow.com/questions/3985619/how-to-calculate-a-logistic-sigmoid-function-in-python
    return cp.exp(-cp.logaddexp(0., -x)) 

def Sigmoid_grad_cupy(x):
    e_x = cp.exp(-x)
    return e_x/(e_x+1.)**2


def ReLU_cupy(x):
    # Broadcasting seems expensive compared to TF and PyTorch
    # return np.maximum(0.,x)
    # a = cp.zeros(x.shape,dtype=cp.float32)
    # return cp.maximum(a,x)
    return x * (x > 0) # This has been the fastest till date

def ReLU_grad_cupy(x):
    return cp.greater(x, 0.).astype(cp.float32)


def Tanh_offset_cupy(x):
    return 0.5*(1.+cp.tanh(x))

def Tanh_offset_grad_cupy(x):
    return 1./(cp.cosh(2.*x)+1.)

def Tanh_cupy(x):
    return cp.tanh(x)

def Tanh_grad_cupy(x):
    return 1.-cp.tanh(x)**2 # sech^2{x}

def Identity_cupy(x):
    return x

def Identity_grad_cupy(x):
    return cp.ones(x.shape, dtype=cp.float32)

def Softplus_cupy(x): 
    # Reference: https://stackoverflow.com/questions/44230635/avoid-overflow-with-softplus-function-in-python
    return cp.log1p(cp.exp(-cp.abs(x))) + cp.maximum(x, 0)
    # np.log(1 + np.exp(-np.abs(x))) + np.maximum(x,0)

def Softplus_grad_cupy(x): # This is simply the sigmoid function
    # The following would be susceptible to over/underflow just like th Sigmoid function
    # return cp.divide(1.,1.+cp.exp(-x))
    # Use this instead
    return Sigmoid_cupy(x)