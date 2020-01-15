"""Union-find data structure."""
# based on https://www.ics.uci.edu/~eppstein/PADS/UnionFind.py


class UnionFind:
    """Union-find data structure."""

    def __init__(self, n):
        """Create a new empty union-find structure."""
        # we have singletons
        self.array = list(range(n))
        self.size = n
        # We give the clusters as a dict
        self.clusters = {i: {i} for i in range(n)}

    def __getitem__(self, element):
        """Find and return the name of the set containing the element."""
        return self.array[element]

    def union(self, group1, group2):
        """Find the sets containing the objects and merge them all."""
        if len(self.clusters[group1]) > len(self.clusters[group2]):
            normal_order = True
            to_extend = group1
            to_delete = group2
        else:
            normal_order = False
            to_extend = group2
            to_delete = group1

        # update elements
        for i in self.clusters[to_delete]:
            self.array[i] = to_extend

        # updating the clusters
        self.clusters[to_extend].update(self.clusters[to_delete])
        del self.clusters[to_delete]
        # which cluster is bigger?
        return normal_order

    def get_cluster(self, group):
        """List of element with id group."""
        if group in self.clusters:
            if self.clusters[group] == set():
                print("Something went wrong!")
            return self.clusters[group]
        else:
            return None

    def move(self, elem, group):
        """Move element into group."""
        elem_group = self.array[elem]
        self.clusters[elem_group].remove(elem)
        if self.clusters[elem_group] == set():
            del self.clusters[elem_group]
        self.array[elem] = group
        if group in self.clusters:
            self.clusters[group].add(elem)
        else:
            self.clusters[group] = {elem}

    def escape(self, elem, lower, upper):
        """Move element somewhere else."""
        elem_group = self.array[elem]
        self.clusters[elem_group].remove(elem)

        for i in range(lower, upper):
            if i not in self.clusters:   # if the cluster is empty
                self.array[elem] = i
                self.clusters[i] = {elem}
                break

    def __repr__(self):
        """To print only."""
        return str(self.array)+str(self.clusters)
