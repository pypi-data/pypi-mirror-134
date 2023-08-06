import numpy as np
import logging
from tqdm import tqdm
class Perceptron:   
    def __init__(self, eta, epochs):
        self.weights = np.random.randn(3)*1e-4
        logging.info(f"Initial weights before training :{self.weights}")
        self.eta = eta
        self.epochs = epochs

    def activationFunction(self, inputs, weights):
        z = np.dot(inputs, weights) # z = w * x 
        return np.where(z>0,1,0)

    def fit(self, x, y):
        self.x = x
        self.y = y

        x_with_bias = np.c_[self.x, -np.ones((len(self.x),1))]
        logging.info(f"x_with_bias is :{x_with_bias} ")

        for epoch in tqdm(range(self.epochs), total=self.epochs,desc="Training the model"):
            logging.info("--"*10)
            logging.info(f"for epoch :{epoch}")
            logging.info("--"*10)

            y_hat = self.activationFunction(x_with_bias, self.weights) # forward propogation
            logging.info(f"predicted value after forward pass :\n{y_hat}")

            self.error = self.y-y_hat
            logging.info(f"error :\n{self.error}")
            self.weights = self.weights + self.eta*np.dot(x_with_bias.T, self.error) #backwords propogation
            logging.info(f"updated weights after epochs :{epoch}/{self.epochs} : \n{self.weights}")
            logging.info("#####"*10)


    def predict(self,x):
        x_with_bias = np.c_[x, -np.ones((len(x),1))]
        return self.activationFunction(x_with_bias,self.weights)

    def total_loss(self):
        total_loss = np.sum(self.error)
        logging.info(f"total_loss :{total_loss}")
        return total_loss