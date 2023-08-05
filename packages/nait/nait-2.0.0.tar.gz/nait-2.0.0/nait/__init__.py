# Nait
# Neural Artificial Intelligence Tool
# nait v2.0.0

import random
import math
import copy
import time
import json

class Network:
    def __init__(self):

        # Generating layers
        self.weights = []
        for _ in range(2):
            layer = []

            for _ in range(4):
                layer.append([0]*4)
            self.weights.append(layer)

        self.biases = []
        for _ in range(2):
            self.biases.append([0]*4)

    def train(self, x, y, layer_size=4, layers=1, activation_function="linear", learning_rate=0.01, epochs=100, backup=None):

        # Verifying training data
        if len(x) != len(y):
            raise ValueError("length of x should equal the length of y")
        if layer_size < 1 or layer_size > 128:
            raise ValueError("layer size can not be below 1 or above 128")
        if layers < 1 or layers > 9:
            raise ValueError("can not have less hidden layers than 1 or more than 9")

        start_time = time.time()

        # Generating layers
        self.activation_function = activation_function
        self.weights = []
        for _ in range(layers+1):
            layer = []

            for _ in range(layer_size):
                layer.append([0]*layer_size)
            self.weights.append(layer)
        
        self.biases = []
        for _ in range(layers+1):
            self.biases.append([0]*layer_size)

        # Adapting layers to training data
        first_layer = []
        for _ in self.weights[0]:
            first_layer.append([0]*len(x[0]))
        self.weights[0] = first_layer

        last_layer = []
        for _ in y[0]:
            last_layer.append(self.weights[-1][0][:])
        self.weights[-1] = copy.deepcopy(last_layer)

        last_layer = []
        for _ in y[0]:
            last_layer.append(0)
        self.biases[-1] = copy.deepcopy(last_layer)

        # Layer foward function
        def layer_forward(layer_input, layer_weights, layer_biases):
            layer_output = []

            for neuron_index in range(len(layer_weights)):
                neuron_output = []

                for weight_index in range(len(layer_weights[neuron_index])):
                    neuron_output.append(layer_input[weight_index] * layer_weights[neuron_index][weight_index])

                neuron_output = sum(neuron_output) + layer_biases[neuron_index]
                
                if self.activation_function == 'relu':
                    if neuron_output < 0:
                        neuron_output = 0

                if self.activation_function == 'step':
                    if neuron_output >= 1:
                        neuron_output = 1
                    else:
                        neuron_output = 0

                if self.activation_function == 'sigmoid':
                    sig = 1 / (1 + math.exp(-neuron_output))
                    neuron_output = sig

                if self.activation_function == 'leaky_relu':
                    if neuron_output < 0:
                        neuron_output = neuron_output * 0.1

                layer_output.append(neuron_output)

            return layer_output

        # Forward function
        def network_forward(network_input, weights, biases):
            activation_list = [network_input]
            network_output = network_input
            for weight_index in range(len(weights)):
                activation_list.append(layer_forward(network_output, weights[weight_index], biases[weight_index]))
                network_output = layer_forward(network_output, weights[weight_index], biases[weight_index])
            return (network_output, activation_list)

        # Training
        epoch = 0

        while epoch < epochs:

            epoch += 1

            # Generating batch
            batch_weights = [self.weights]
            batch_biases = [self.biases]

            for _ in range(10):
                batch_weights.append(copy.deepcopy(self.weights))
                batch_biases.append(copy.deepcopy(self.biases))

                for layerindex in range(len(batch_weights[0])):
                    for neuronindex in range(len(batch_weights[0][layerindex])):
                        batch_biases[0][layerindex][neuronindex] = round(
                            random.uniform(learning_rate, learning_rate*-1) + batch_biases[0][layerindex][neuronindex], 8)

                        for weightindex in range(len(batch_weights[0][layerindex][neuronindex])):
                            batch_weights[0][layerindex][neuronindex][weightindex] = round(
                                random.uniform(learning_rate, learning_rate*-1) + batch_weights[0][layerindex][neuronindex][weightindex], 8)

                for layerindex in range(len(batch_weights[0])):
                    for neuronindex in range(len(batch_weights[0][layerindex])):
                        batch_biases[0][layerindex][neuronindex] = round(
                            random.uniform(learning_rate*0.1, learning_rate*-0.1) + batch_biases[0][layerindex][neuronindex], 8)

                        for weightindex in range(len(batch_weights[0][layerindex][neuronindex])):
                            batch_weights[0][layerindex][neuronindex][weightindex] = round(
                                random.uniform(learning_rate*0.1, learning_rate*-0.1) + batch_weights[0][layerindex][neuronindex][weightindex], 8)

                # Selection
                losses = []
                for index in range(len(batch_weights)):
                    current_loss = 0
                    for x_index in range(len(x)):
                        network_output = network_forward(x[x_index], batch_weights[index], batch_biases[index])[0]
                        neuron_loss = 0
                        for output_index in range(len(y[x_index])):
                            neuron_loss += abs(network_output[output_index] - y[x_index][output_index])
                        current_loss += neuron_loss
                    losses.append(current_loss)
                self.weights = batch_weights[losses.index(min(losses))]
                self.biases = batch_biases[losses.index(min(losses))]

            if epoch == 1:
                if (time.time() - start_time) * epochs >= 60:
                    print(f"TRAINING (estimated time: {math.floor(((time.time() - start_time) * epochs) / 60)}m)")
                else:
                    print(f"TRAINING (estimated time: {math.floor((time.time() - start_time) * epochs)}s)")

            filled_loadingbar = "█"
            unfilled_loadingbar = " "

            bar_filled = round(epoch / epochs * 20)

            if round(epoch % (epochs / 50), 0) == 0 or epoch == epochs:
                if ((time.time() - start_time) / (epoch / epochs)) * (1 - (epoch / epochs)) >= 60:
                    print(f"TRAINING (loss: {round(min(losses), 8)} average loss: {round(min(losses)/len(x), 8)} epoch {epoch}/{epochs} estimated remaining time: {math.floor((((time.time() - start_time) / (epoch / epochs)) * (1 - (epoch / epochs))) / 60)}m)                                        ")
                else:
                    print(f"TRAINING (loss: {round(min(losses), 8)} average loss: {round(min(losses)/len(x), 8)} epoch {epoch}/{epochs} estimated remaining time: {math.floor(((time.time() - start_time) / (epoch / epochs)) * (1 - (epoch / epochs)))}s)                                        ")

                if backup != None and epoch != epochs:
                    data = {}
                    data['weights'] = self.weights
                    data['biases'] = self.biases
                    data['activation'] = self.activation_function

                    with open(backup, 'w') as backup_file:
                        json.dump(data, backup_file)

            else:
                print(f"TRAINING |{filled_loadingbar * bar_filled}{unfilled_loadingbar * (20 - bar_filled)}| {round((epoch / epochs) * 100, 1)}% (loss: {round(min(losses), 8)} average loss: {round(min(losses)/len(x), 8)} epoch {epoch}/{epochs})          ", end="\r")

        # Post training
        if (time.time() - start_time) * (epoch / epochs) >= 60:
            print(f"FINAL (loss: {round(min(losses), 8)} average loss: {round(min(losses)/len(x), 8)} time: {math.floor(((time.time() - start_time) / (epoch / epochs)) / 60)}m)")
        else:
            print(f"FINAL (loss: {round(min(losses), 8)} average loss: {round(min(losses)/len(x), 8)} time: {math.floor((time.time() - start_time) / (epoch / epochs))}s)")

    def predict(self, inputs):

        # Layer foward function
        def layer_forward(layer_input, layer_weights, layer_biases):
            layer_output = []

            for neuron_index in range(len(layer_weights)):
                neuron_output = []

                for weight_index in range(len(layer_weights[neuron_index])):
                    neuron_output.append(layer_input[weight_index] * layer_weights[neuron_index][weight_index])

                neuron_output = sum(neuron_output) + layer_biases[neuron_index]
                
                if self.activation_function == 'relu':
                    if neuron_output < 0:
                        neuron_output = 0

                if self.activation_function == 'step':
                    if neuron_output >= 1:
                        neuron_output = 1
                    else:
                        neuron_output = 0

                if self.activation_function == 'sigmoid':
                    sig = 1 / (1 + math.exp(-neuron_output))
                    neuron_output = sig

                if self.activation_function == 'leaky_relu':
                    if neuron_output < 0:
                        neuron_output = neuron_output * 0.1

                layer_output.append(neuron_output)

            return layer_output

        # Forward function
        def network_forward(network_input, weights, biases):
            activation_list = []
            network_output = network_input
            for weight_index in range(len(weights)):
                activation_list.append(layer_forward(network_output, weights[weight_index], biases[weight_index]))
                network_output = layer_forward(network_output, weights[weight_index], biases[weight_index])
            return (network_output, activation_list)

        return network_forward(inputs, self.weights, self.biases)[0]
    
    def save(self, file):
        
        data = {}

        data['weights'] = self.weights
        data['biases'] = self.biases
        data['activation'] = self.activation_function

        with open(file, 'w') as file:
            json.dump(data, file)
    
    def load(self, file):

        with open(file, 'r') as file:
            data = json.load(file)

        self.weights = data['weights']
        self.biases = data['biases']
        self.activation_function = data['activation']
    
    def evaluate(self, x, y):

        # Layer foward function
        def layer_forward(layer_input, layer_weights, layer_biases):
            layer_output = []

            for neuron_index in range(len(layer_weights)):
                neuron_output = []

                for weight_index in range(len(layer_weights[neuron_index])):
                    neuron_output.append(layer_input[weight_index] * layer_weights[neuron_index][weight_index])

                layer_output.append(sum(neuron_output) + layer_biases[neuron_index])

            return layer_output

        # Forward function
        def network_forward(network_input, weights, biases):
            network_output = network_input

            for weight_index in range(len(weights)):
                network_output = layer_forward(network_output, weights[weight_index], biases[weight_index])
            return network_output

        # Evaluation
        loss = 0
        for x_index in range(len(x)):
            network_output = network_forward(x[x_index], self.weights, self.biases)
            neuron_loss = 0
            for output_index in range(len(y[x_index])):
                neuron_loss += abs(network_output[output_index] - y[x_index][output_index])
            loss += neuron_loss
        print(f"EVALUATION (loss: {round(loss, 8)} average loss: {round(loss/len(x), 8)})")