Title: Gradient Descent
TitleShort: Gradient Descent
Date: 2021-08-22
Author: Vladimir Haltakov
AuthorLink: https://twitter.com/haltakov
Category: Math Terms
Slug: gradient-descent
Featured: 1
Summary: A simple method for minimizing a function by changing its parameters in the direction the function decreases.

A simple method for minimizing a function by changing its parameters in the direction the function decreases.

Gradient descent is one of the most used optimization methods. The goal is to find the parameters of a function `w` that produces the lowest value of the function. This is done by changing the parameters in small steps in the direction the function decreases until a (local) minimum is reached. Simple gradient descent implementations are very likely to get stuck in a local minimum - there are several techniques to mitigate this, like for example using [momentum](/explanation/momentum).

Gradient descent and its variants are often used in machine learning to minimize a [loss function](/explanation/loss-function) during training.

## Detailed formula explanation

The gradient descent formula can be written like this:

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd.png" alt="Gradeint Descent formula">

The basis is this simple formula defines an iterative optimization method. We have some weights (parameters) `w` and we iteratively update them in some way to minimize the value of the function. Iterative methods are used when we cannot compute the solution directly.

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd_1.jpg" alt="Gradeint Descent formula - iterative optimization">

In machine learning, we define a loss function describing how good our model is. We want to find the weights that minimize the loss (make the model better). We compute the gradient of the function and update the weights by a small amount (learning rate) against the gradient.

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd_2.jpg" alt="Gradeint Descent formula - iterative optimization">

Here is an illustration of how it works. The gradient tells us if the function will decrease (negative gradient) or increase (positive gradient) if we increase the weight. The learning rate defines how far along the gradient we will jump in the current step of the optimization.

Large steps will lead us to the minimum more quickly, but we may jump over it and the optimization process may start to oscillate. Small steps may mean that we need many iterations to reach the minimum. Therefore, setting the learning rate correctly is very important for efficient optimization.

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd_3.jpg" alt="Gradeint Descent formula - illustration">

With this, we get the final formula:

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd_4.jpg" alt="Gradeint Descent formula - annotated">
