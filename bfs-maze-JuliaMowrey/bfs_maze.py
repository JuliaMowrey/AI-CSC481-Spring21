import time


class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('\033[96m*\x1b[0m', end=' ')   # print a blue *
                else:
                    print(self.grid[r][c], end=' ')      # prints a space or wall
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        # YOU FILL THIS IN
        r,c = self.location
        moves = []

        if(self.grid[r+1][c]== " "):
            moves.append("S")
        if (self.grid[r][c-1] == " "):
            moves.append("W")
        if (self.grid[r-1][c] == " "):
            moves.append("N")
        if (self.grid[r][c+1] == " "):
            moves.append("E")

        return moves


    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # YOU FILL THIS IN
        r,c = self.location

        if(move == "N"):
            newLocation = r-1,c
        if(move == "S"):
            newLocation = r+1,c
        if(move == "W"):
            newLocation = r,c-1
        if(move == "E"):
            newLocation = r,c+1

        return Maze(self.grid, (newLocation))


class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal, ):
        """Return an ordered list of moves to get the maze to match the goal."""
        # YOU FILL THIS IN
        frontier = [[maze,[]]]
        visited = set([maze.location])
        while frontier != []:
            parent = frontier.pop(0) #parent = [maze,[]]
            pmaze, ppath = parent
            moves = pmaze.moves()
            for x in moves: # x = "N" or "S" or "E" ...
                neighbor = pmaze.neighbor(x)
                if(neighbor.location in visited):
                    continue
                child = [neighbor, ppath + [x]] #gets the parents maze next move and adds previious path
                frontier.append(child)
                visited.add(child[0].location)
                if(child[0].location == goal.location):
                    return child[1]
def main():
    """Create a maze, solve it with BFS, and console-animate."""

    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(.5)
        maze.display()


if __name__ == '__main__':
    main()
