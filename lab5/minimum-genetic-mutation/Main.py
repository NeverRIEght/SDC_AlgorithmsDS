class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list) -> int:
        # BFS
        # O(4 * L * N)
        # L - length of the gene
        # N - the number of genes in the bank

        if endGene not in bank:
            return -1

        gene_symbols = ['A', 'C', 'G', 'T']

        # Deque-based BFS (startGene, mutations counter)
        queue = deque([(startGene, 0)])

        visited = {startGene}

        while queue:
            current_gene, mutations = queue.popleft()

            # Destination reached
            if current_gene == endGene:
                return mutations

            # Generate all possible combinations
            for i in range(len(current_gene)):
                for current_symbol in gene_symbols:
                    # Do not override the same symbol
                    if current_gene[i] == current_symbol:
                        continue

                    # New mutation
                    mutated_gene = current_gene[:i] + current_symbol + current_gene[i + 1:]

                    if mutated_gene in bank and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutations + 1))

        # No mutations found
        return -1