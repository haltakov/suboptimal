Title: Principal Component Analysis (PCA)
TitleShort: PCA
Date: 2021-05-14
Author: Valkea
AuthorLink: https://twitter.com/lunarkin
Category: Machine Learning Terms
Slug: pca
Summary: An algorithm that removes less important data from a dataset.

An algorithm that removes less important data from a dataset.

PCA (as any 'dimensionality reduction' algorithms) helps to reduce the storage space, to improve the performance of the models, and, to ease the data visualization.

Technically, it's a statistical procedure that identifies and sorts a small number of uncorrelated variables, called principal components, in such a way that the first one has the most scattered data. So, if we want to reduce from `n` to `k` dimensions, we keep the `k`'s first principal components. But the lower is `k` the greater is the information loss.
