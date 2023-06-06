from torch import nn


class ScenarioModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.linear_relu_stack = nn.Sequential(
            nn.Linear(15, 15),
            nn.ReLU(),
            nn.Linear(15, 15),
            nn.ReLU(),
            nn.Linear(15, 15),
            nn.ReLU(),
            nn.Linear(15, 10),
            # nn.Sigmoid(),
            nn.Softmax(dim=1),
        )

    def forward(self, x):
        return self.linear_relu_stack(x)
