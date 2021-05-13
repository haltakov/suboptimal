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
    <p>An algorithm that is used to narrow down datasets.</p>
    <p>PCA (as any 'dimensionality reduction' algorithms) has several advantages:
	<ul>
		<li>it reduces the storage space required</li>
		<li>it improves the performance of the machine learning model by removing the multicollinearity in the data</li>
		<li>it eases the visualization of the data when reduced to very low dimensions such as 2D or 3D</li>
	</ul>
    </p>
    <p>Technically, it's a statistical procedure that uses an orthogonal transformation to <strong>identify a small number of uncorrelated variables, called principal components</strong> from a large set of data possibly containing correlated variables.</p>
    <p>This transformation is defined in such a way that the first principal component has the largest possible variance (variability in the data), and each succeeding component in turn has the highest variance possible under the constraint that it is orthogonal to the preceding components. So if we want to reduce from <tt>n</tt> to <tt>k</tt> dimensions, we keep the k's first principal components.</p>
    <dl><dt>Source:</dt><dd>notes from the <a href="https://www.coursera.org/learn/machine-learning">Coursera's ML Course</a></dd></dl>
</td>
</tr>
</tbody>
</table>

Machine Learning terms are one thing the math is another. Get some human language explanation of some confusing terms [here](math-terms.md).
