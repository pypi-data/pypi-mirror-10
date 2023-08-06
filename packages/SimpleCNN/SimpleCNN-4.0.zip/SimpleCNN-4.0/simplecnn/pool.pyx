import cython        
cimport cython
import numpy as np
cimport numpy as np
  
DTYPE = np.float
ctypedef np.float_t DTYPE_t
ctypedef Py_ssize_t uint
  
cdef inline DTYPE_t dtype_t_max(DTYPE_t a, DTYPE_t b): return a if a >= b else b
  
cdef inline int int_max(int a, int b): return a if a >= b else b
cdef inline int int_min(int a, int b): return a if a <= b else b
  
@cython.boundscheck(False)
@cython.wraparound(False)
def max_pool_ff_c(np.ndarray[DTYPE_t, ndim=4] prev_activation,
                    np.ndarray[DTYPE_t, ndim=4] ff_activation,
                    np.ndarray[DTYPE_t, ndim=4] ff_max_x_indices,
                    np.ndarray[DTYPE_t, ndim=4] ff_max_y_indices,
                    int pl_dim):
    '''
    Set max pooling result to ff_activation
    Set max pooling result indices to ff_max_indices
    
    prev_activation[img_num x prev_fltr_num x prev_output_dim x prev_output_dim]
    ff_activation[img_num x fltr_num x output_dim x output_dim]
    ff_max_x_indices[img_num x fltr_num x output_dim x output_dim]
    ff_max_y_indices[img_num x fltr_num x output_dim x output_dim]
    (The last two record x and y axis coordinates of units that 
    are maximal in each pooling area.)
    '''
    cdef uint img_num = prev_activation.shape[0]
    cdef uint fltr_num = prev_activation.shape[1]
    cdef uint input_dim = prev_activation.shape[2]
    
    for i in range(img_num):
        for f in range(fltr_num):
            for x in range(0, input_dim, pl_dim):
                for y in range(0, input_dim, pl_dim):
                    value = -9e99
                    for x_r in range(x, x + pl_dim):
                        for y_r in range(y, y + pl_dim):
                            new_value = prev_activation[i,f,x_r, y_r]
                            if new_value > value:
                                value = new_value
                                ff_activation[i,f,x/pl_dim,y/pl_dim] = value
                                ff_max_x_indices[i,f,x/pl_dim,y/pl_dim] = x_r
                                ff_max_y_indices[i,f,x/pl_dim,y/pl_dim] = y_r
                                
@cython.boundscheck(False)
@cython.wraparound(False)    
def max_pool_unsample_c(np.ndarray[DTYPE_t, ndim=4] sensitivity, 
                        np.ndarray[DTYPE_t, ndim=4] sensitivity_unsampled, 
                        np.ndarray[DTYPE_t, ndim=4] ff_max_x_indices, 
                        np.ndarray[DTYPE_t, ndim=4] ff_max_y_indices):
    '''        
    Unsample from sensitivity and set result to sensitivity_unsample
    
    Max pooling layer        unsampled layer
          A  B                 0 A 0 0
          C  D          =>     0 0 0 B
                               0 C 0 D
                               0 0 0 0
    (The locations of A, B, C and D depend on ff_max_x_indices and ff_max_y_indices. )
    
    sensitivity[img_num x fltr_num x output_dim x output_dim]
    sensitivity_unsampled[img_num x fltr_num x input_dim x input_dim]     
    ff_max_x_indices[img_num x fltr_num x output_dim x output_dim]   
    ff_max_y_indices[img_num x fltr_num x output_dim x output_dim]   
    '''
    cdef uint img_num = sensitivity.shape[0]
    cdef uint fltr_num = sensitivity.shape[1]
    cdef uint input_dim = sensitivity_unsampled.shape[2]
    cdef uint output_dim = ff_max_x_indices.shape[2]
     
    for i in range(img_num):
        for f in range(fltr_num):
            for x_o in range(output_dim):
                for y_o in range(output_dim):
                    x_i = ff_max_x_indices[i, f, x_o, y_o]
                    y_i = ff_max_y_indices[i, f, x_o, y_o]
                    sstvy = sensitivity[i, f, x_o, y_o]
                    sensitivity_unsampled[i,f, x_i, y_i] = sstvy
                    
                    
                    
@cython.boundscheck(False)
@cython.wraparound(False)
def mean_pool_ff_c(np.ndarray[DTYPE_t, ndim=4] prev_activation,
                   np.ndarray[DTYPE_t, ndim=4] ff_activation,
                   int pl_dim):
    '''
    Set mean pooling result to ff_activation
    
    prev_activation[img_num x prev_fltr_num x prev_output_dim x prev_output_dim]
    ff_activation[img_num x fltr_num x output_dim x output_dim]
    '''
    cdef uint img_num = prev_activation.shape[0]
    cdef uint fltr_num = prev_activation.shape[1]
    cdef uint input_dim = prev_activation.shape[2]
    
    for i in range(img_num):
        for f in range(fltr_num):
            for x in range(0, input_dim, pl_dim):
                for y in range(0, input_dim, pl_dim):
                    value = 0
                    for x_r in range(x, x + pl_dim):
                        for y_r in range(y, y + pl_dim):
                            value += prev_activation[i, f, x_r, y_r]
                    # Calculate mean
                    value = value * 1. / (pl_dim ** 2)
                    ff_activation[i,f,x/pl_dim,y/pl_dim] = value     
                    

@cython.boundscheck(False)
@cython.wraparound(False)    
def mean_pool_unsample_c(np.ndarray[DTYPE_t, ndim=4] sensitivity, 
                         np.ndarray[DTYPE_t, ndim=4] sensitivity_unsampled):
    '''        
    Unsample from sensitivity and set result to sensitivity_unsample
    
    Suppose pl_dim = 2
    Mean pooling layer        unsampled layer
          A  B                 A/4 A/4 B/4 B/4
          C  D          =>     A/4 A/4 B/4 B/4
                               C/4 C/4 D/4 D/4
                               C/4 C/4 D/4 D/4
    
    sensitivity[img_num x fltr_num x output_dim x output_dim]
    sensitivity_unsampled[img_num x fltr_num x input_dim x input_dim]     
    '''
    cdef uint img_num = sensitivity.shape[0]
    cdef uint fltr_num = sensitivity.shape[1]
    cdef uint input_dim = sensitivity_unsampled.shape[2]
    cdef uint output_dim = sensitivity.shape[2]
    
    pl_dim = input_dim / output_dim
     
    for i in range(img_num):
        for f in range(fltr_num):
            for x_o in range(output_dim):
                for y_o in range(output_dim):
                    sstvy = sensitivity[i, f, x_o, y_o]
                    unsampled_sstvy = sstvy / (pl_dim ** 2)
                    for x_i in range(x_o * pl_dim, x_o * pl_dim + pl_dim):
                        for y_i in range(y_o * pl_dim, y_o * pl_dim + pl_dim):
                            sensitivity_unsampled[i,f, x_i, y_i] = unsampled_sstvy    
    
                    
                    
                    
                    