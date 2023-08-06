from .var_container import VarContainer
import tensorflow as tf


class Container:
    def __init__(self, variables, losses):
        self._var = VarContainer(variables)
        self._losses = losses
        self._first_run()

    def _first_run(self):
        for loss_func in self._losses:
            loss_func(self._var)

    def cal_grads(self, model):
        for grad in self._var.iterate_grads():
            grad.cal_grad(model)

    def cal_loss(self):
        result = 0
        for loss_func in self._losses:
            result += tf.reduce_mean(tf.square(loss_func(self._var)))

        return result
