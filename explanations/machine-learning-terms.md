# Machine Learning Terms

Researchers often invent complicated names for simple things. This page will help you uncover the real meaning of those perplexing terms.

<table>
<thead>
<tr>
<th>Term</th>
<th>Human Language Translation</th>
</tr>
</thead>
<tbody>
<tr>
<td valign="top">Rectified Linear Unit (ReLU)</td>
<td>
    <p>A simple function of <tt>x</tt> returning 0 if <tt>x < 0</tt> or <tt>x</tt> otherwise</p>
    <p><img width="400px" src="images/relu.png"></p>
</td>
</tr>
<tr>
<td valign="top">Embedding</td>
<td>
    <p>A representation of an object as a list of numbers.</p>
    <p>Embeddings are commonly used to create representations of objects or features that are suitable for particular machine learning algorithms.</p>
    <p>One example is working with words in Natural Language Processing. Words are usually transformed to a list of numbers (embedded) before given as input to a neural network. The exact mapping between word and the list of numbers will be automatically learned.</p>
</td>
</tr>
<tr>
<td valign="top">Tensor (as in TensorFlow or PyTorch)</td>
<td>
    <p>A multidimensional array similar to <tt>numpy.array</tt></p>
    <p>Tensor is a term that is used in TensorFlow and PyTorch to indicate a multidimensional array. This may be a bit confusing, because the mathematical term tensor, actually has a different meaning - more like a function.</p>
    <p>Tensors are data structures that are used to store data. For example, a 1D tensor could store prices of houses, a 2D tensor could store an image, a 3D tensor could store multiple images etc.</p>
</td>
</tr>
<tr>
<td valign="top">Principal Component Analysis (PCA)</td>
<td>
    <p>An algorithm that removes less important data from a dataset.</p>
    <p>PCA (as any 'dimensionality reduction' algorithms) helps to reduce the storage space, to improve the performance of the models, and, to ease the data visualization.</p>
    <p>Technically, it's a statistical procedure that identifies and sorts a small number of uncorrelated variables, called principal components, in such a way that the first one has the most scattered data. So if we want to reduce from <tt>n</tt> to <tt>k</tt> dimensions, we keep the <tt>k</tt>'s first principal components. But the lower is <tt>k</tt> the greater is the information loss.</p>
</td>
</tr>
<tr>
<td valign="top">Kernel (function)</td>
<td>
    <p>A function that helps to separate datasets that can't be separated with a classic linear approach.</p>
    <p>A kernel function implicitly finds a higher dimensional space in which a non linearly separable dataset can be easily separated, then project the separation back to the original dataset space.</p>
    <p>Technically, a kernel function allows making complex non-linear classifiers using any learning algorithm that can be expressed solely in terms of dot products between two vectors.</p>
</td>
</tr>
<tr>
<td valign="top">Parameters</td>
<td>
    <p>The model parameters are the internal variables of the model that will be updated during the training phase, for example, in the case of neural networks, the weights or biases of the network.</p>
    <p>In some contexts, it is usual to describe a model by its number of parameters.</p>
</td>
</tr>
<tr>
<td valign="top">Hyperparameters</td>
<td>
    <p>Hyperparameters specify the model's architecture and how it will be trained. Therefore, these hyperparameters are not learned during training phase. In the case of neural networks, some common hyperparameters are:</p>
    <ul>
        <li>Learning rate</li>
        <li>Batch size</li>
        <li>Number of epochs to train the model</li>
        <li>Number of hidden layers</li>
        <li>Number of neurons in each layer</li>
        <li>Activations functions</li>
    </ul>
</td>
</tr>
<tr>
<td valign="top">Loss Functions</td>
<td>
    <p>Functions that are used to evaluate the performance of a model and guide the training process.</p>
    <p>Loss Functions (aka Cost Functions) show the error between what value your model predicts and what the value actually is. Since these functions are generally differentiable (with some exceptions i.e. Hinge Loss), we can apply a Gradient Descent to find the least error. Some common ones are:</p>
    <p>For Regression Models:</p>
    <ul>
        <li>Mean Absolute Error (MAE)</li>
        <li>Mean Squared Error (MSE)</li>
        <li>Mean Squared Logarithmic Error (MSLE)</li>
    </ul>
    <p>For Classification Models:</p>
    <ul>
        <li>Binary Cross Entropy Loss</li>
        <li>Categorical Cross Entropy Loss</li>
    </ul>
</td>
</tr>
</tbody>
</table>

Machine Learning terms are one thing the math is another. Get some human language explanation of some confusing terms [here](math-terms.md).
