def delone_triangulation(self,points, values, p, n):
    #https://stackoverflow.com/questions/30373912/interpolation-with-delaunay-triangulation-n-dim
    # dimension of the problem (in this example I use 3D grid,
    # but the method works for any dimension n>=2)
    #n = 2
    # my array of grid points (array of n-dimensional coordinates)
    #points = [[1, 2], [2, 3], ...]
    # each point has some assigned value that will be interpolated
    # (e.g. a float, but it can be a function or anything else)
    #values = [7, 8, ...]
    # a set of points at which I want to interpolate (it must be a NumPy array)
    #p = np.array([[1.5, 2.5, 3.5], [1.1, 2.2, 3.3], ...])

    # create an object with triangulation
    tri = Delaunay(points)
    # find simplexes that contain interpolated points
    s = tri.find_simplex(p)
    # get the vertices for each simplex
    v = tri.vertices[s]
    # get transform matrices for each simplex (see explanation bellow)
    m = tri.transform[s]

    # for each interpolated point p, mutliply the transform matrix by
    # vector p-r, where r=m[:,n,:] is one of the simplex vertices to which
    # the matrix m is related to (again, see bellow)
    #for i in range(len(p)): b[i] = m[i, :n, :n].dot(p[i] - m[i, n, :]) аналог нижней строчки
    b = np.einsum('ijk,ik->ij', m[:, :n, :n], p - m[:, n, :])

    # get the weights for the vertices; `b` contains an n-dimensional vector
    # with weights for all but the last vertices of the simplex
    # (note that for n-D grid, each simplex consists of n+1 vertices);
    # the remaining weight for the last vertex can be copmuted from
    # the condition that sum of weights must be equal to 1
    w = np.c_[b, 1 - b.sum(axis=1)]

    #Now, v contains indices of vertex points for each simplex and w holds corresponding weights.
    # To get the interpolated values p_values at set of points p,
    # we do (note: values must be NumPy array for this):
    #for i in range(len(p)): p_values[i] = np.inner(values[v[i]], w[i])
    p_values = np.einsum('ij,ij->i', values[v], w)
    return p_values