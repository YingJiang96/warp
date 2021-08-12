import warp as wp

class Tape:

    def __init__(self):

        self.adjoints = {}
        self.launches = []

    def __enter__(self):      
        if (wp.context.runtime.tape != None):
            raise RuntimeError("Warp: Error, entering a tape while one is already active")

        wp.context.runtime.tape = self

    def __exit__(self, exc_type, exc_value, traceback):
        if (wp.context.runtime.tape == None):
            raise RuntimeError("Warp: Error, ended tape capture, but tape not present")            

        wp.context.runtime.tape = None

    # record a kernel launch on the tape
    def record(self, kernel, dim, inputs, outputs, device):   
        self.launches.append([kernel, dim, inputs, outputs, device])


    # adj_outputs is a mapping from output tensor -> adjoint of the output
    # after running backward the adjoints of tensors may be retrieved by:
    #
    #  adj_tensor = tape.adjoints[tensor]
    #
    def backward(self, adj_user: dict):

        # insert user specified adjoints (e.g.: from loss function inputs) into our lookup
        self.adjoints = {}
        self.adjoints.update(adj_user)

        # run launches backwards
        for launch in reversed(self.launches):

            kernel = launch[0]
            dim = launch[1]
            inputs = launch[2]
            outputs = launch[3]
            device = launch[4]

            adj_inputs = []
            adj_outputs = []

            # lookup adjoint inputs
            for a in inputs:
                adj_inputs.append(self.get_adjoint(a))

            # lookup adjoint outputs, todo: only allocate outputs if necessary
            for a in outputs:
                adj_outputs.append(self.get_adjoint(a))

            wp.launch(
                kernel=kernel, 
                dim=dim, 
                inputs=inputs, 
                outputs=outputs,
                adj_inputs=adj_inputs,
                adj_outputs=adj_outputs,
                device=device,
                adjoint=True)
            

    # returns the adjoint version of a tensor used in the computation
    def get_adjoint(self, a):
        
        if isinstance(a, wp.array) == False:
            # if input is a simple type (e.g.: float, vec3, etc) just return a value copy
            return a

        elif wp.type_is_int(a.dtype) or a.requires_grad == False:
            # otherwise if input is an array that is integer typed or doesn't require grad then return null array
            return None

        elif a in self.adjoints:
            # try and find adjoint array in map
            return self.adjoints[a]
        
        else:
            # otherwise allocate a zero array for the array adjoint
            adj = wp.zeros_like(a)
            self.adjoints[a] = adj
            return adj

    def zero(self):
        self.adjoints = {}

    def reset(self):

        self.adjoints = {}
        self.launches = []
        
   