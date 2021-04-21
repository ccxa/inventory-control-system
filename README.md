# Inventory control system (fixed size order)

Simulate and estimate your profit and loss at different intervals, then
it helps you to choose best reorder point for your inventory.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)

### Introduction

when you have to manage an inventory you should Observe balance between <br>
current supply and daily usage of that specific product.<br>
running out of that product will opset your costumers, <br>
and over storing of that product will have a lot of costs for you.<br>

so by this app you can set essential parameters likes reorder point, lead time, <br>
daily usage probabilities and ... to estimate how much profit or loss will have at future!

Some parameters are received from the user when launching the program, you can hard-code it in parameters.py<br>
other parameter such as probabilities for distributions are hard-coded, you can modify them too.


### Installation

Clone and fork the repository to make the changes in your local system.

```git-bash
git clone https://github.com/ccxa/inventory-control-system.git
cd inventory-control-system
```

The following command creates a directory named inventory-control-system<br>
then you can execute this app by:

```bash
python3 main.py
```
