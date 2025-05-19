# Network Project

## Overview
This project implements Dijkstra's algorithm for finding shortest paths in a directed weighted graph. The implementation uses the NetworkX library for graph representation and manipulation, and Matplotlib for visualization.

## Features
- Single-source shortest path calculation using Dijkstra's algorithm
- Graph visualization with node and edge weights
- Input graph data from text file

## Requirements
- Python 3.x
- NetworkX
- Matplotlib
- Other dependencies as listed in `requirements.txt`

## Setup
1. Clone the repository
2. Set up a virtual environment (recommended):
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Input Format
Create a text file with the following format:
- First line: `<num_nodes>,<num_edges>`
- Following lines: `<source>,<target>,<weight>`

Example (`example.txt`):
```
6,10
u,v,2
u,w,5
u,x,1
x,v,2
v,w,3
x,w,3
w,y,1
x,y,1
w,z,5
y,z,2
```

### Running the Program
```
python main.py
```

This will:
1. Load the graph from `example.txt`
2. Run Dijkstra's algorithm from each node
3. Display the shortest paths and distances
4. Show a visualization of the graph

## Algorithm
The implementation uses a heap-based priority queue to efficiently find the shortest paths from a source node to all other nodes in the graph, following Dijkstra's algorithm.

## Visualization
The graph is visualized using a circular layout with:
- Blue nodes representing vertices
- Edges with their weights displayed
- Clear labels for easy identification