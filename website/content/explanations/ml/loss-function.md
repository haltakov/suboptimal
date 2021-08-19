Title: Loss Function
TitleShort: Loss Function
Date: 2021-06-10
Author: Nadirhan Şahin
AuthorLink: https://twitter.com/sahinadirhan
Category: Machine Learning Terms
Slug: loss-function
Summary: Function that is used to evaluate the performance of a model and guide the training process.

Function that is used to evaluate the performance of a model and guide the training process.

Loss Functions (aka Cost Functions) show the error between what value your model predicts and what the value actually is. Since these functions are generally differentiable (with some exceptions i.e. Hinge Loss), we can apply a Gradient Descent to find the least error. Some common ones are:

For Regression Models:

-   Mean Absolute Error (MAE)
-   Mean Squared Error (MSE)
-   Mean Squared Logarithmic Error (MSLE)

For Classification Models:

-   Binary Cross Entropy Loss
-   Categorical Cross Entropy Loss
