"""Neural network model definition for the PARADOX assistant."""

from torch import nn


class NeuralNet(nn.Module):
    """Simple feed-forward neural network used to classify user intents."""

    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()

        # First hidden layer transforms the bag-of-words input.
        self.l1 = nn.Linear(input_size, hidden_size)

        # Second hidden layer adds depth to the classifier.
        self.l2 = nn.Linear(hidden_size, hidden_size)

        # Final layer maps the learned features to an intent class.
        self.l3 = nn.Linear(hidden_size, num_classes)

        # ReLU activation is used after the hidden layers.
        self.relu = nn.ReLU()

    def forward(self, x):
        """Run one forward pass through the network."""
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        return out
