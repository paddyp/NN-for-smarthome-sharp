import os

import numpy as np
import shap
import torch
from numpy import genfromtxt
from ScenarioModel import ScenarioModel
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset

np.random.seed(17)
torch.manual_seed(17)


def read_data(filename: str, folder: str = "") -> torch.Tensor:
    os.getcwd()
    fullpath = os.getcwd() + "/"
    if folder:
        fullpath += folder + "/"
    fullpath += filename

    numpy_mat = genfromtxt(fullpath, delimiter=",")
    tensor = torch.from_numpy(numpy_mat).float()
    return tensor


def get_dataloader(type: str, folder: str) -> DataLoader:
    tensor_x = read_data(type + "_x.txt", folder=folder)
    tensor_y = read_data(type + "_y.txt", folder=folder)

    dataset = TensorDataset(tensor_x, tensor_y)
    return DataLoader(dataset=dataset, batch_size=16, shuffle=False)


def init_weights(m):
    if isinstance(m, nn.Linear):
        torch.nn.init.xavier_uniform_(m.weight)
        torch.nn.init.uniform_(m.bias)  # .data.fill_(0.01)


def main():
    device = "mps" if torch.backends.mps.is_available() else "cpu"

    train_loader = get_dataloader("train", folder="export")
    test_loader = get_dataloader("test", folder="export")

    print(len(train_loader))

    model = ScenarioModel()
    model.train()

    lr = 1e-1
    n_epochs = 20

    loss_fn = nn.CrossEntropyLoss()

    model.linear_relu_stack.apply(init_weights)
    # torch.nn.init.xavier_uniform_(model.weight)  # ToDO; check error

    # Defines a SGD optimizer to update the parameters
    optimizer = optim.SGD(model.linear_relu_stack.parameters(), lr=lr)
    scheduler = optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.99)

    for epoch in range(n_epochs):
        num_batches = len(train_loader)
        train_loss = 0
        for x_batch, y_batch in train_loader:
            # the dataset "lives" in the CPU, so do our mini-batches
            # therefore, we need to send those mini-batches to the
            # device where the model "lives"
            x_batch = x_batch.to(device)
            y_batch = y_batch.to(device)

            # Makes predictions
            yhat = model(x_batch)
            # Computes loss
            loss = loss_fn(y_batch, yhat)

            # print(epoch, " : ", loss)
            optimizer.zero_grad()
            # Computes gradients
            loss.backward()
            # Updates parameters and zeroes gradients
            optimizer.step()

            with torch.no_grad():
                train_loss += loss
        scheduler.step()

        train_loss /= num_batches
        print("Learning Rate", scheduler.get_last_lr())
        print("Train Loss", epoch, ":", train_loss)

        num_batches = len(test_loader)
        test_loss = 0
        with torch.no_grad():
            for x_batch, y_batch in test_loader:
                x_batch = x_batch.to(device)
                y_batch = y_batch.to(device)

                # Makes predictions
                yhat = model(x_batch)
                # Computes loss
                test_loss += loss_fn(y_batch, yhat)

            test_loss /= num_batches
            print("Test Loss", epoch, ":", test_loss)

    batch = next(iter(test_loader))
    data, _ = batch
    background = data[:100]
    test_data = data[:100]
    explainer = shap.DeepExplainer(model, background)

    shap_values = explainer.shap_values(test_data)
    for input, output in zip(test_data, shap_values):
        device_id = (input[:100] == min(input[:100])).nonzero(as_tuple=True)[0]
        max_inpact_id = list(output[0]).index(max(list(output[0])))
        print(
            "device : ", device_id, " | max inpact: ", inpact_to_string(max_inpact_id)
        )
    # shap.plots.waterfall(shap_values[0])


def inpact_to_string(value: int):
    if value in range(0, 6):
        return "device distance"
    if value in range(6, 12):
        return "device angle"
    if value == 12:
        return "weekday"
    if value == 13:
        return "hour"
    if value == 14:
        return "minute"


if __name__ == "__main__":
    main()

# max inpact
# 0-5 device distance
# 6-11 device angle
# 12 weekday
# 13 hour
# 14 minute
