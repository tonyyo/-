class Solution:
    def sequenceReconstruction(self, org, seqs):
        from collections import defaultdict
        edges = defaultdict(list)
        indegrees = defaultdict(int)
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
            for i in range(len(seq)):
                if i == 0:
                    indegrees[seq[i]] += 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indegrees[seq[i + 1]] += 1
        cur = [k for k in indegrees if indegrees[k] == 0]
        res = []
        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in edges[cur_node]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org
#主函数
if __name__ == '__main__':
    solution = Solution()
    org = [1, 2, 3]
    seqs = [[1, 2], [1, 3], [2, 3]]
    print("org是：", org, "seqs是：", seqs)
    print("可否从seqs唯一重构出org：", solution.sequenceReconstruction(org, seqs))