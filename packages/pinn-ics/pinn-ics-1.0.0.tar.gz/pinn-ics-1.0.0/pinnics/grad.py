import tensorflow as tf


class Grad:
    output_key = 'u_'

    def __init__(self, var, var_order):
        self._fir_grad = set()
        self._sec_grad = set()
        self._result_dict = dict()
        self._var = var
        self._var_order = var_order

    @property 
    def var(self):
        return self._var
    
    def get_input(self):
        data = []
        for key in self._var_order:
            data.append(self.var[key]) 

        return tf.concat(data, axis=1)

    def _get_result_key(self, char):
        return f"{self.output_key}{'_'.join(char)}"

    def __call__(self):
        try:
            return self._result_dict[f"{self.output_key}"]
        except:
            return tf.constant(0., dtype=tf.float32)

    def diff(self, *char):
        len_char = len(char)
        key = self._get_result_key(char)

        if key in self._result_dict.keys():
            return self._result_dict[key]
        elif len_char == 1:
            self._fir_grad.add(char)
            return tf.constant(0., dtype=tf.float32)
        elif len_char == 2:
            self._fir_grad.add(char[:1])
            self._sec_grad.add(char)
            return tf.constant(0., dtype=tf.float32)

    def _get_result_keys(self, key_set):
        return [[self._get_result_key(char), char] for char in key_set]

    def get_fir_result_keys(self):
        return self._get_result_keys(self._fir_grad)    

    def get_sec_result_keys(self):
        return self._get_result_keys(self._sec_grad)

    def cal_grad(self, model):
        self.reset() 

        with tf.GradientTape(persistent=True) as tape_sec:
            tape_sec.watch([self.var[char] for char in self._var_order])
            with tf.GradientTape(persistent=True) as tape_fir:
                tape_fir.watch([self.var[char] for char in self._var_order])
                input = self.get_input()
                output = model(input)
                self._result_dict[self.output_key] = output

            for char in self._fir_grad:
                key = self._get_result_key(char)
                grad = tape_fir.gradient(output, self.var[char[0]])
                self._result_dict[key] = grad
            
        for char in self._sec_grad:
            source_key = self._get_result_key(char[:1])
            key = self._get_result_key(char)
            source = self._result_dict[source_key] 
            grad = tape_sec.gradient(source, self.var[char[1]])
            self._result_dict[key] = grad

        del tape_fir
        del tape_sec

    def reset(self):
        self._result_dict = dict()
