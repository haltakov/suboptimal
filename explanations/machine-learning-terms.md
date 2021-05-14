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
    <p>A simple function of <tt>x</tt> returning 0 if <tt>x < 0<tt> or <tt>x</tt> otherwise</p>
    <p><img width="400px" src="images/relu.png"></p>
</td>
</tr>
<tr>
<td valign="top">Embedding</td>
<td>
    <p>A representation of an object as a list of numbers.</p>
    <p>Embeddings are commonly used to create representations of objects or features that are suitable for particular machine learning algorithms.</p>
    <p>One example is working with words in Natural Language Processing. Words are usually transformed to a list of numbers  (embedded) before given as input to a neural network. The exact mapping between word and the list of numbers will be automatically learned.</p>
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
</tbody>
</table>

Machine Learning terms are one thing the math is another. Get some human language explanation of some confusing terms [here](math-terms.md).
