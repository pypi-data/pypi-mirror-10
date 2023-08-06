cdef class Example:
    def __init__(self, int n_classes, int n_atoms, int n_features):
        self.mem = Pool()
        self.is_valid = <bint*>self.mem.alloc(n_classes, sizeof(bint))
        self.costs = <int*>self.mem.alloc(n_classes, sizeof(int))
        self.atoms = <atom_t*>self.mem.alloc(n_classes, sizeof(atom_t))
        self.scores = <weight_t*>self.mem.alloc(n_classes, sizeof(weight_t))


