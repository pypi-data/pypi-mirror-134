# Random-brain

Random brain is the neural network implementation of a random forest.

## Background on random forests
A random forest is a machine learning model that is composed of multiple decision trees. These trees in the forest all predict an outcome and the majority rules.

## Similarities
Just as the random forest is a vote based ML algorithm, the random brain is a vote based algorithm as well, but uses neural networks specified by the user rather than decision forests.

## Setting up Random brain
```
pip install random-brain
```

## API
init the brain
```
brain = random_brain()
```

**import models()**
```
brain.import_models(model_path = 'path to model.h5)
```
Import models will take in a directory or a single .h5 file. Sub directories will be ignored.

**show_brain()**
```
brain.show_brain()
```
Shows the keys used in the brain. This should just be the name of each imported model


**clear_brain()**
```
brain.clear_brain(item_list = ['model to remove'])
```
Clear a single model or more by entering in the model name as a list. Leave blank to clear all models.

**Vote**
```
brain.vote(yTest = [1, 2, 3, 4, ...])
```
Add in yTest to cast votes. Vote() will only return the votes as a numpy array and not actual predictions. This is useful if you want to run statistics on the votes

**predict**
```
brain.predict(yTest = [1, 2, 3, 4, ...])
```
Add in your yTest to make predictions. This will attempt to make a prediction based off of the networks and will return a numpy array of answers

In the future prediction and threading options will be added and improved.

## Disclaimer
The random brain module is in no way a production ready module. This is intended as a research experiment to easily implement random forest style forecasting for neural networks. 
