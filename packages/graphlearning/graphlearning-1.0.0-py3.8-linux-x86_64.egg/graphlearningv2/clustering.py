from abc import ABCMeta, abstractmethod
import scipy.optimize as opt
import sklearn.cluster as cluster
import numpy as np
import sys

class clustering:
    __metaclass__ = ABCMeta

    def __init__(self, W, num_clusters):
        if type(W) == graph.graph:
            self.graph = W
        else:
            self.graph = graph.graph(W)
        self.cluster_labels = None
        self.num_clusters = num_clusters

    def predict(self):
        """Predict
        ========

        Makes label predictions based on clustering. 
        
        Returns
        -------
        pred_labels : (int) numpy array
            Predicted labels as integers for all datapoints in the graph.
        """

        if self.fitted == False:
            sys.exit('Model has not been fitted yet.')

        return self.cluster_labels

    def fit_predict(self, all_labels=None):
        """Fit and predict
        ======

        Calls fit() and predict() sequentially.

        Parameters
        ----------
        all_labels : numpy array, int (optional)
            True labels for all datapoints.

        Returns
        -------
        pred_labels : (int) numpy array
            Predicted labels as integers for all datapoints in the graph.
        """

        self.fit(all_labels=all_labels)
        return self.predict()

    @abstractmethod
    def fit(self, all_labels=None):
        """Fit
        ======

        Solves clustering problem to perform clustering. 

        Parameters
        ----------
        all_labels : numpy array, int (optional)
            True labels for all datapoints.

        Returns
        -------
        all_labels : numpy array, int (optional)
            True labels for all datapoints.
        """

        raise NotImplementedError("Must override solve")


class spectral(clustering):
    def __init__(self, W, num_clusters, method='NgJordanWeiss', extra_dim=0):
        """Spectral clustering
        ===================

        Implements several methods for spectral clustering, including Shi-Malik and Ng-Jordan-Weiss. See
        the tutorial paper [1] for details.

        Parameters
        ----------
        W : numpy array, scipy sparse matrix, or graphlearning graph object
            Weight matrix representing the graph.
        num_clusters : int
            Number of desired clusters.
        method : {'combinatorial', 'ShiMalik', 'NgJordanWeiss'} (optional), default='NgJordanWeiss'
            Spectral clustering method.
        extra_dim : int (optional), default=0
            Extra dimensions to include in spectral embedding.

        Reference
        ---------
        [1] U. Von Luxburg.  [A tutorial on spectral clustering.](https://link.springer.com/content/pdf/10.1007/s11222-007-9033-z.pdf) Statistics and computing 17.4 (2007): 395-416.
        """
        super().__init__(W, num_clusters)
            
        self.method = method
        self.extra_dim = extra_dim

    def fit(self, all_labels=None):

        n = self.graph.num_nodes
        num_clusters = self.num_clusters
        method = self.method
        extra_dim = self.extra_dim

        if method == 'combinatorial':
            vals, vec = self.graph.eigen_decomp(k=num_clusters+extra_dim)
        elif method == 'ShiMalik':
            vals, vec = self.graph.eigen_decomp(normalization='randomwalk', k=num_clusters+extra_dim)
        elif method == 'NgJordanWeiss':
            vals, vec = self.graph.eigen_decomp(normalization='normalized', k=num_clusters+extra_dim)
            norms = np.sum(vec*vec,axis=1)
            T = sparse.spdiags(norms**(-1/2),0,n,n)
            vec = T@vec  #Normalize rows
        else:
            sys.exit("Invalid spectral clustering method " + method)

        kmeans = cluster.KMeans(n_clusters=k).fit(vec)

        return kmeans.labels_

class incres(clustering):
    def __init__(self, W, num_clusters, speed=5, T=100):
        """INCRES clustering
        ===================

        Implements the INCRES clustering algorithm from [1].

        Parameters
        ----------
        W : numpy array, scipy sparse matrix, or graphlearning graph object
            Weight matrix representing the graph.
        num_clusters : int
            Number of desired clusters.
        speed : float (optional), default=5
            Speed parameter.
        T : int (optional), default=100
            Number of iterations.

        Reference
        ---------
        [1] X. Bresson, H. Hu, T. Laurent, A. Szlam, and J. von Brecht. [An incremental reseeding strategy for clustering](https://arxiv.org/pdf/1406.3837.pdf). In International Conference on Imaging, Vision and Learning based on Optimization and PDEs (pp. 203-219), 2016.
        """
        super().__init__(W, num_clusters)
            
        self.speed = speed
        self.T = T

    def fit(self, all_labels=None):

        #Short cuts
        n = self.graph.num_nodes
        speed = self.speed
        T = self.T
        k = self.num_clusters

        #Increment
        Dm = np.maximum(int(speed*1e-4*n/k),1)
        
        #Random initial labeling
        u = np.random.randint(0,k,size=n)

        #Initialization
        F = np.zeros((n,k))
        J = np.arange(n).astype(int)

        #Random walk transition
        D = self.graph.degree_matrix(p=-1)
        P = self.graph.weight_matrix*D

        m = int(1)
        for i in range(T):
            #Plant
            F.fill(0)
            for r in range(k):
                I = u == r
                ind = J[I]
                F[ind[random.choice(np.sum(I),m)],r] = 1
            
            #Grow
            while np.min(F) == 0:
                F = P*F

            #Harvest
            u = np.argmax(F,axis=1)

            #Increment
            m = m + Dm
                
            #Compute accuracy
            if all_labels is not None: 
                acc = clustering_accuracy(u,all_labels)
                print("Iteration "+str(i)+": Accuracy = %.2f" % acc+"%%, #seeds= %d" % m)

        return u

def withinss(x):
    """WithinSS
    ======

    Clustering of 1D data with WithinSS. Gives exact solution to the 2-means clustering problem

    Parameters
    ----------
    x : numpy array
        1D array of data to cluter.

    Returns
    -------
    w : float
        WithinSS value, essentially the 2-means energy.
    m : float
        Threshold that clusters the data array x optimally.
    """

    x = np.sort(x)
    n = x.shape[0]
    sigma = np.std(x)
    v = np.zeros(n-1,)

    #Initial values for m1,m2
    x1 = x[:1]
    x2 = x[1:]
    m1 = np.mean(x1)
    m2 = np.mean(x2)
    for i in range(n-1):
        v[i] = (i+1)*m1**2 + (n-i-1)*m2**2
        if i < n-2:
            m1 = ((i+1)*m1 + x[i+1])/(i+2)
            m2 = ((n-i-1)*m2 - x[i+1])/(n-i-2)
    ind = np.argmax(v)
    m = x[ind]
    w = (np.sum(x**2) - v[ind])/(n*sigma**2)
    return w,m

#RP1D clustering from
#Han, Sangchun, and Mireille Boutin. "The hidden structure of image datasets." 2015 IEEE International Conference on Image Processing (ICIP). IEEE, 2015.
#X = data
def RP1D_clustering(X,T=100):
    """Random Projection Clustering
    ======

    Binary clustering of 1D data with the Random Projection 1D (RP1D) clustering method from [1].

    Parameters
    ----------
    X : numpy array
        (n,d) dimensional array of n datapoints in dimension d.
    T : int (optional), default=100
        Number of random projections to try.

    Returns
    -------
    cluster_labels : int
        0/1 array indicating cluster membership

    References
    ----------
    [1] S. Han and M. Boutin. [The hidden structure of image datasets.](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7350969&casa_token=UsN9y0textMAAAAA:-K9r-Sv4njFQ_txJUpkqCbavM-wTA2CmkgU3co7RjmjTKdcP3guTjahyHA7jZBs1WZTz-E2fETQ&tag=1) 2015 IEEE International Conference on Image Processing (ICIP). IEEE, 2015.
    """

    n = X.shape[0]
    d = X.shape[1]
    v = np.random.rand(T,d)
    wmin = np.inf
    imin = 0;
    for i in range(T):
        x = np.sum(v[i,:]*X,axis=1)
        w,m = withinss(x)
        if w < wmin:
            wmin = w
            imin = i
    x = np.sum(v[imin,:]*X,axis=1)
    w,m = withinss(x)

    cluster_labels = np.zeros(n,)
    cluster_labels[x>m] = 1

    return cluster_labels

def clustering_accuracy(pred_labels,true_labels):
    """Clustering accuracy
    ======

    Accuracy for clustering in graph learning. Uses a linear sum assignment
    to find the best permutation of cluster labels.

    Parameters
    ----------
    pred_labels : numpy array, int
        Predicted labels
    true_labels : numpy array, int
        True labels

    Returns
    -------
    accuracy : float
        Accuracy as a number in [0,100].
    """

    unique_classes = np.unique(true_labels)
    num_classes = len(unique_classes)

    C = np.zeros((num_classes, num_classes))
    for i in range(num_classes):
        for j in range(num_classes):
            C[i][j] = np.sum((pred_labels == i) & (true_labels != j))
    row_ind, col_ind = opt.linear_sum_assignment(C)

    return 100*(1-C[row_ind,col_ind].sum()/len(pred_labels))



