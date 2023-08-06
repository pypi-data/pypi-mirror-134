import tensorflow as tf
from .grad import Grad
from .utils import encode_dict_str


class VarContainer:
    def __init__(self, variables):
        self._var_types = []
        self._grads = dict()
        self._var_order = [variable.character for variable in variables]
        self._variables = {variable.character: variable for variable in variables}

    def _get_var(self, num, var_type):
        input_keys = var_type.keys()
        var = dict()

        if len(self._var_order) != len(input_keys):
            raise RuntimeError(f"You must implement input for all {self._var_order}")

        for input_key in input_keys:
            if input_key not in self._var_order:
                raise RuntimeError(f"The parameter \'{input_key}\' is invalid.")
            else:
                var_value = var_type[input_key]
                if isinstance(var_value, str):
                    var[input_key] = self._variables[input_key].random(num)
                elif isinstance(var_value, int) or isinstance(var_value, float):
                    data = tf.ones(shape=[num, 1], dtype=tf.float32)
                    data = tf.multiply(data, tf.constant(var_value, dtype=tf.float32))
                    var[input_key] = data
        return var 

    def add_var_type(self, num, var_type):
        self._var_types.append(var_type)

        var = self._get_var(num, var_type)

        key = encode_dict_str(var_type)
        self._grads[key] = Grad(var, self._var_order)
    
    def __call__(self, num=200, **char):
        key = encode_dict_str(char)

        if key not in self._grads.keys():
            self.add_var_type(num, char)
            return self._grads[key]

        return self._grads[key]

    def iterate_grads(self):
        return [grad for key, grad in self._grads.items()]
