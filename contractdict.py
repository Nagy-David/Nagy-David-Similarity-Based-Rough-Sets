"""Contraction methods using Python dicts."""
# for FEDCSIS-WCO 2015
# updated for FEDCSIS-WCO 2016 - in parts, recursively
import copy
import math


def update_attraction(force, index, value):
    """Increase the value, or delete the item, if the value is zero."""
    # we do not store the common zero values
    if index in force:
        force[index] += value
    else:
        force[index] = value
    if force[index] == 0:
        del force[index]


class ContractDict2(object):
    """Contraction with dict of dicts."""

    def __init__(self, N, g):
        """Coding the maxtrix g in a dict of dicts."""
        # empty data structure
        self.size = N
        self.tolerance = {}
        for i in range(N):
            self.tolerance[i] = {}
        # fill up
		# végigmegyek a mátrix felén és belepakolom
        for i, j, weight in g:
            self.tolerance[i][j] = weight    # double accounting
            self.tolerance[j][i] = weight
        # we use the same data structure in the other cases
        self.force = copy.deepcopy(self.tolerance)
        self.attraction = copy.deepcopy(self.tolerance)

    def contraction_step(self, i, j):
        """Merge clusters i and j."""
        # We add two columns at attractions
        for k in range(self.size):
            if j in self.attraction[k]:
                if i in self.attraction[k]:
                    self.attraction[k][i] += self.attraction[k][j]
                else:
                    self.attraction[k][i] = self.attraction[k][j]
                del self.attraction[k][j]

        # At forces we add columns and rows
        force_j = self.force[j].copy()
        if i not in self.force:
            self.force[i] = {}
        # symmetric way
        for key, value in force_j.items():  # take the elements to delete
            if key in self.force[i]:
                # no new element
                self.force[i][key] += value
                self.force[key][i] += value
                # if the value to store is zero, then delete the item
                if self.force[i][key] == 0:
                    del self.force[i][key]
                    del self.force[key][i]
            else:  # if no predecessor, construct it
                self.force[i][key] = value
                self.force[key][i] = value

            del self.force[key][j]    # delete the last element
            if self.force[key] == {}:     # if the row became empty,
                del self.force[key]       # delete it.
        if i in self.force[i]:        # we contracted by f_ij, but forget it
            del self.force[i][i]
        del self.force[j]              # delete the line
        if self.force[i] == {}:        # if nothing left, delete the whole line
            del self.force[i]

    def max_max_val(self, lower, upper):
        """Search for the first maximal value."""
        # the first value to start with it, we will increase it
        max_val = 0
        max_pos = (lower, lower)
        # csak a határok között mozoghatunk
        for i in range(lower, upper):
            if i in self.force:
                for j, value in self.force[i].items():
                    # de data structure symmetric, so use one half only
                    if i < j and j < upper and value > max_val:
                        max_val = value
                        max_pos = (i, j)
        return max_pos

    def contract(self, union_find, lower, upper):
        """Összevonás, amíg csak lehet."""
        if len(self.force) < 2:
            return  # we have one or 0 cluster, cannot to contract
        # look for the maximal value
        i, j = self.max_max_val(lower, upper)
        while i != j:  # we have a good canditate pair
            # document it
            if union_find.union(i, j):
                self.contraction_step(i, j)
            else:
                self.contraction_step(j, i)
            if len(self.force) < 2:
                return
            i, j = self.max_max_val(lower, upper)

    def contract_in_pieces(self, union_find, parts):
        """Divide and conquer."""
        small_size = math.ceil(self.size/parts)
        for lower in range(0, self.size, small_size):
            upper = min(lower + small_size, self.size)
            self.contract(union_find, lower, upper)

    def calc_attract(self, union_find, i, lower, upper):
        """Determine the most attractive cluster for element i."""
        # we need a better value
        max_pos = union_find[i]
        if max_pos in self.attraction[i]:  # there are other elements here
            max_val = self.attraction[i][max_pos]
        else:  # it is alone
            max_val = 0
        own_value = max_val
        for key, value in self.attraction[i].items():
            if lower <= key and key < upper and value > max_val:
                max_pos = key
                max_val = value
        return (max_pos, max_val, own_value)

    def to_move(self, union_find, lower, upper):
        """Which elements would like to move somewhere else."""
        for i in range(lower, upper):  # id of element
            (group, value, old_value) = \
                self.calc_attract(union_find, i, lower, upper)
            if value > old_value or old_value < 0:
                # there is a better cluster
                return (group, i, value)
        # no better cluster
        return None

    def recalculate(self, union_find, i, group, old_group):
        """Element i get in to group, we need to recalculate the values."""
        for j in self.tolerance[i]:
            # attractions ###########################################
            t_ij = self.tolerance[j][i]
            # i bring its attractions into group, recalculate the target
            update_attraction(self.attraction[j], group, t_ij)
            # recalculate from the beginning (only for testing)
            # if group in self.attraction[j]:
            #     self.attraction[j][group] += t_ij
            # else:  # ha nincs létre kell hozni
            #     self.attraction[j][group] = t_ij
            # if self.attraction[j][group] == 0:
            #     del self.attraction[j][group]

            # recalculate the source, too
            update_attraction(self.attraction[j], old_group, -t_ij)
            # recalculate from the beginning (only for testing)
            # if old_group in self.attraction[j]:
            #     self.attraction[j][old_group] -= t_ij
            # else:
            #     self.attraction[j][old_group] = -t_ij
            # if self.attraction[j][old_group] == 0:
            #    del self.attraction[j][old_group]

            # forces ############################################
            ufj = union_find[j]
            if ufj not in self.force:
                self.force[ufj] = {}
            # at escape we use an empty cluster
            if group not in self.force:
                self.force[group] = {}
            # if the target is known
            update_attraction(self.force[group], ufj, t_ij)
            update_attraction(self.force[ufj], group, t_ij)
            # recalculate from the beginning (only for testing)
            # if ufj in self.force[group]:
            #     self.force[group][ufj] += t_ij
            #     self.force[ufj][group] += t_ij
            # else:  # if missing
            #     self.force[group][ufj] = t_ij
            #     self.force[ufj][group] = t_ij
            # if self.force[ufj][group] == 0:  # empty, to delete
            #     del self.force[ufj][group]
            #     del self.force[group][ufj]

            # it can be occur?
            if old_group not in self.force:
                self.force[old_group] = {}
            update_attraction(self.force[old_group], ufj, -t_ij)
            update_attraction(self.force[ufj], old_group, -t_ij)
            # recalculate from the beginning (only for testing)
            # if ufj in self.force[old_group]:
            #     self.force[old_group][ufj] -= t_ij
            #     self.force[ufj][old_group] -= t_ij
            # else:
            #     self.force[old_group][ufj] = -t_ij
            #     self.force[ufj][old_group] = -t_ij
            # if self.force[old_group][ufj] == 0:
            #     del self.force[old_group][ufj]
            #     del self.force[ufj][old_group]
            # if self.force[ufj] == {}:
            #     del self.force[ufj]

        # clean the diagonal
        for j in self.force:
            if j in self.force[j]:
                del self.force[j][j]
        # is some cluster is empty, delete
        if self.force[old_group] == {}:
            del self.force[old_group]

        if self.force[group] == {}:
            del self.force[group]

    def correct(self, union_find, lower, upper):
        """Correct the errors of the contraction."""
        move = self.to_move(union_find, lower, upper)
        while move:
            group, i, value = move
            old_group = union_find[i]
            if value < 0:  # all clusters are repulsive
                union_find.escape(i, lower, upper)
                group = union_find[i]

            else:  # there is an attractive set
                union_find.move(i, group)
            self.recalculate(union_find, i, group, old_group)
            move = self.to_move(union_find, lower, upper)

    def correct_in_pieces(self, union_find, parts):
        """Divide and conquer."""
        small_size = math.ceil(self.size/parts)
        for lower in range(0, self.size, small_size):
            upper = min(lower + small_size, self.size)
            self.correct(union_find, lower, upper)

    def calc_force_pair(self, group_i, group_j):
        """Calculate the attraction between two sets."""
        if not group_i or not group_j:
            return 0
        counter = 0
        for k in group_i:
            for elem_j in group_j:
                counter += self.tolerance[k].get(elem_j, 0)
        return counter

    def check_force(self, union_find):
        """Check the consistency of the matrix."""
        groups = {}
        for i in range(self.size):
            groups[i] = union_find.get_cluster(i)
        for i in range(self.size):
            if groups[i]:
                for j in range(i+1, self.size):
                    if groups[j]:
                        counter = self.calc_force_pair(groups[i], groups[j])
                        if self.force != {} and \
                                counter != self.force[i].get(j, 0):
                            print(
                                "(F) at {}/{}: calc:{} vs store:{}".format(
                                    i, j, counter, self.force[i].get(j, 0)))
                    else:
                        if self.force != {} and j in self.force[i]:
                            print(
                                "(F) We have {} at {}/{} instead 0".format(
                                    self.force[i][j], i, j))
            else:
                if i in self.force:
                    print("(F) {} at {}, instead of nothing".format(
                        self.force[i], i))

    def check_attraction(self, union_find):
        """Check the consistency of the matrix."""
        for i in range(self.size):  # as element
            for j in range(self.size):  # as cluster
                group = union_find.get_cluster(j)
                if group:
                    counter = 0
                    for elem in group:
                        counter += self.tolerance[i].get(elem, 0)
                    if counter != self.attraction[i].get(j, 0):
                        print(
                            "(A) at {}/{}: calc:{} vs store:{}".format(
                                i, j, counter, self.attraction[i][j]))
                else:
                    if j in self.attraction[i]:
                        print(
                            "(A) We have {} at {}/{} instead 0".format(
                                self.attraction[i][j], i, j))

    def recursive_contract(self, union_find, size, lower, upper):
        """Contraction applied by recursively."""
        if lower + size < upper:
            mid = (lower + upper)//2
            self.recursive_contract(union_find, size, lower, mid)
            self.recursive_contract(union_find, size, mid, upper)
        self.contract(union_find, lower, upper)
        self.correct(union_find, lower, upper)

    def rec2_contract(self, union_find, size, lower, upper):
        """Contraction applied by recursively, without correction."""
        if lower + size < upper:
            mid = (lower + upper)//2
            self.recursive_contract(union_find, size, lower, mid)
            self.recursive_contract(union_find, size, mid, upper)
        self.contract(union_find, lower, upper)
