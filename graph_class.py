"""
Simple graph implementation
"""
from queue_stack import Queue, Stack  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v1 not in self.vertices:
        #     self.add_vertex(v1)
        #     self.vertices[v1]
        # if v2 not in self.vertices:
        #     self.add_vertex(v2)
        #     self.vertices[v2]
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def add_bidirectional_edge(self, v1, v2):
        self.add_edge(v1, v2)
        self.add_edge(v2, v1)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            print("That vertex does not yet exist")
            return
        else:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create an empty Queue and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
    
        # Create an empty set to track visited verticies
        visited_vertices = set()
        
        # while queue is not empty:
        while queue.size() > 0:
            # Get the current vertex (dequeue from queue)
            current_vertex = queue.dequeue()

            # Check to see if the current vertex has not been visited. If it hasn't been visited:
            if current_vertex not in visited_vertices:
                # Print the current vertex
                print(current_vertex)
                # Mark the current vertex as being visited
                    # Add the current vertex to a visted_set
                visited_vertices.add(current_vertex)
                # Queue up all the neighbors of the current vertex (So we can visit them next)
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    if neighbor not in visited_vertices:
                        queue.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty Stack and push the starting_vertex onto it
        stack = Stack()
        stack.push(starting_vertex)
    
        # Create an empty set to track visited verticies
        visited_vertices = set()
        
        # while stack is not empty:
        while stack.size() > 0:
            # Get the current vertex (pop from stack)
            current_vertex = stack.pop()

            # Check to see if the current vertex has not been visited. If it hasn't been visited:
            if current_vertex not in visited_vertices:
                # Print the current vertex
                print(current_vertex)
                # Mark the current vertex as being visited (Add the current vertex to a visted_set)
                visited_vertices.add(current_vertex)
                # Stack up all the neighbors of the current vertex (So we can visit them next)
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    if neighbor not in visited_vertices:
                        stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited_vertices=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited_vertices is None:
            visited_vertices = set()
            
        print(starting_vertex)

        visited_vertices.add(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)
        
        for neighbor in neighbors:
            if neighbor not in visited_vertices:
                self.dft_recursive(neighbor, visited_vertices)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
#################### My Code From Day 1 ####################
        # # Create an empty Queue and enqueue the PATH TO THE starting_vertex
        # queue = Queue()
        # queue.enqueue([starting_vertex])
        # # Create an empty set to track visited verticies
        # visted_vertices = set()
        
        # # while queue is not empty:
        # while queue.size() > 0:
        #     # Get the current vertex PATH (dequeue from queue)
        #     # SET THE CURRENT VERTEX TO THE LAST ELEMENT OF THE PATH
        #     current_path = queue.dequeue()
        #     current_vertex = current_path[len(current_path) - 1]

        #     # Check to see if the current vertex has not been visited. If it hasn't been visited:
        #     if current_vertex not in visted_vertices:
        #         # CHECK IF THE CURRENT VERTEX IS THE DESTINATION
        #         if current_vertex == destination_vertex:
        #             # IF IT IS, STOP AND RETURN
        #             return current_path
        #         # Mark the current vertex as being visited (Add the current vertex to a visted_set)
        #         visted_vertices.add(current_vertex)

        #         # Queue up NEW PATHS WITH EACH NEIGHBOR:
        #         neighbors = self.get_neighbors(current_vertex)
        #         for neighbor in neighbors:
        #             # TAKE CURRENT PATH
        #             copy_of_current_path = list(current_path)
        #             # APPEND THE NEIGHBOR TO IT
        #             copy_of_current_path.append(neighbor)
        #             new_path = copy_of_current_path
        #             # QUEUE UP NEW PATH
        #             queue.enqueue(new_path)

################ Code From Class The Next Day ################
        queue = Queue()
        visited_vertices = set()

        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        while queue.size() > 0:
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            if current_vertex not in visited_vertices:

                if current_vertex == destination_vertex:
                    return current_path

                visited_vertices.add(current_vertex)

                for neighbor_vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                        })


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

#################### My Code From Day 1 ####################

        # # Create an empty Stack and push the PATH TO THE starting_vertex to the stack
        # stack = Stack()
        # stack.push([starting_vertex])
        # # Create an empty set to track visited verticies
        # visted_vertices = set()
        
        # # while queue is not empty:
        # while stack.size() > 0:
        #     # Get the current vertex PATH (dequeue from queue)
        #     # SET THE CURRENT VERTEX TO THE LAST ELEMENT OF THE PATH
        #     current_path = stack.pop()
        #     current_vertex = current_path[len(current_path) - 1]

        #     # Check to see if the current vertex has not been visited. If it hasn't been visited:
        #     if current_vertex not in visted_vertices:
        #         # CHECK IF THE CURRENT VERTEX IS THE DESTINATION
        #         if current_vertex == destination_vertex:
        #             # IF IT IS, STOP AND RETURN
        #             return current_path
        #         # Mark the current vertex as being visited (Add the current vertex to a visted_set)
        #         visted_vertices.add(current_vertex)

        #         # Queue up NEW PATHS WITH EACH NEIGHBOR:
        #         neighbors = self.get_neighbors(current_vertex)
        #         for neighbor in neighbors:
        #             # TAKE CURRENT PATH
        #             copy_of_current_path = list(current_path)
        #             # APPEND THE NEIGHBOR TO IT
        #             copy_of_current_path.append(neighbor)
        #             new_path = copy_of_current_path
        #             # QUEUE UP NEW PATH
        #             stack.push(new_path)


################ Code From Class The Next Day ################
        stack = Stack()
        visited_vertices = set()

        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        while stack.size() > 0:
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            if current_vertex not in visited_vertices:

                if current_vertex == destination_vertex:
                    return current_path

                visited_vertices.add(current_vertex)

                for neighbor_vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    stack.push({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                        })

    def dfs_recursive(self, starting_vertex, destination_vertex, visited_vertices=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited_vertices is None:
            visited_vertices = set()
        
        if path is None:
            path = []

        path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path
        
        visited_vertices.add(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited_vertices:
                path_copy = list(path)
                path_with_new_neighbor = self.dfs_recursive(neighbor, destination_vertex, visited_vertices, path_copy)
                if path_with_new_neighbor is not None:
                    return path_with_new_neighbor
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
