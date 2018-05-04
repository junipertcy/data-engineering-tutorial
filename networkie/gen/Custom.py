import networkx as nx


class LoadFromFile(object):
    def __init__(self):
        """
        Initiate variables for the class.
        """
        self.g = nx.Graph()

        pass

    def from_edgelist(self, path):
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''

        edgelist = []
        with open(path, 'r') as f:
            for line in f:
                node_pair = line.replace('\n', '').split(' ')
                edgelist += [node_pair]
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g

    def from_in_class_network(self):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        
        Read the data from a file.

        Creat undirected edges by the relationship between Col. ID and Col. IDs-of-acquaintances.
        '''
        path = "dataset/In-class_network.txt"
       
        with open(path,"r") as data:
            
            next(data)  # Skip header row
        
            for row in data:
                x= row.split("\t")
             
                for i in x[1].split(","):
            
                    if i != " ":   # Some ID have no acquaintances
                        e = [(x[0],i)]
                        self.g.add_edges_from(e)
                
        
        return self.g