# Load required packages
library(igraph)

# Read the file
data <- read.table("/home/sneha/work/RnaP/contacts/chainAB_contacts", header = TRUE)

# Create a bipartite graph
graph <- graph_from_data_frame(data, directed = FALSE)

# Set vertex types
V(graph)$type <- V(graph)$name %>% strsplit(":") %>% sapply(function(x) x[1])

# Plot the bipartite graph
plot(graph, layout = layout_as_bipartite)
