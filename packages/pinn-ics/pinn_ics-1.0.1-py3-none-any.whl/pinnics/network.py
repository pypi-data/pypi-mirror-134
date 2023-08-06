import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.activations import tanh
from tensorflow.keras.initializers import glorot_normal
from tensorflow.keras.optimizers import Adam
from .problem_container import Container
from tensorflow.keras.layers import Dense


class NetWork(Model):
    def __init__(self, variables, losses, 
                layers=[2, 1], 
                activation_func=tanh, 
                initializer_func=glorot_normal,
                optimizer=Adam(), 
                **kwargs):
        Model.__init__(self, **kwargs)
        self.dense_layers = []
        self.optim = optimizer
        self.container = Container(variables, losses)
        self.history_loss = []
        len_layers = len(layers)
        for index, layer in enumerate(layers):
            self.dense_layers.append(Dense(layer, kernel_initializer=initializer_func))
            if index != len_layers - 1:
                self.dense_layers.append(activation_func)

    @tf.function
    def call(self, input_tensor):
        output = tf.identity(input_tensor)
        for layer in self.dense_layers:
            output = layer(output)
        return output

    @tf.function
    def _train_step(self):
        with tf.GradientTape() as tape: 
            self.container.cal_grads(self)
            loss = self.container.cal_loss()

        gradients = tape.gradient(loss, self.trainable_variables)
        self.optim.apply_gradients(zip(gradients, self.trainable_variables))
        return loss

    def solve(self, epochs=1000, show_every=100):
        for epoch in range(1, epochs + 1): 
            loss = self._train_step()
            self.history_loss.append(loss)

            if epoch % show_every == 0:
                print(f"Epoch {epoch} \n\tLoss: {loss}")
            
        return self.history_loss
