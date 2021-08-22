Title: Momentum
TitleShort: Momentum
Date: 2021-08-22
Author: Vladimir Haltakov
AuthorLink: https://twitter.com/haltakov
Category: Math Terms
Slug: momentum
Summary: A technique used when minimizing a function using gradeint descent that helps avoid local minima

A technique used when minimizing a function using gradient descent that helps avoid local minima.

One of the biggest problems when using [gradient descent](/explanation/gradient-descent) to minimize a function is that the optimization process may get stuck in a local minimum. Momentum is a technique that tries to mitigate that by allowing the optimization to "gather speed" and jump over small "hills" in the function.

## Detailed formula explanation

The formulat for momentum used in a [gradient descent](/explanation/gradient-descent) optimization can be written as:

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd_momentum.png" alt="Momentum formula">

The formula is based on a simple iterative optimization algorithm, that can be expressed as:

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd_1.jpg" alt="Momentum formula - iterative optimization">

In a simple [gradient descent](/explanation/gradient-descent) optimization, we define the update of the weights as:

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/gd_2.jpg" alt="Momentum formula - gradient descent update">

If we want to add momentum, we add an additional term - the weight update in the previous step times a decay factor. The decay factor `α` is just a number between 0 and 1 defining how much of the previous update will be taken into account. If we set `α` = 0 then no momentum is applied, while `α` = 1 means a lot of momentum.

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/momentum_1.jpg" alt="Momentum formula - momentum update update">

A useful analogy is a ball rolling down a hill. If the hill is steep, the ball will accelerate (we update the weights more). This will help the ball jump over small local minima and continue down the hill (to a smaller value of the function). More momentum means a heavier ball with higher inertia.

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/momentum_2.jpg" alt="Momentum formula - illustration">

The final formula of [gradient descent](/explanation/gradient-descent) optimization with momentum becomes:

<img class="w-full md:w-1/2 lg:w-3/5 mx-auto my-4" src="{{ SITEURL }}/images/momentum_3.jpg" alt="Momentum formula - annotated">
