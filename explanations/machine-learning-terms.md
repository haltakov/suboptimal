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
</tbody>
</table>

Machine Learning terms are one thing the math is another. Get some human language explanation of some confusing terms [here](math-terms.md).
