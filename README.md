# growing-networks
(Project for Complexity and Networks course in spring 2018)

A lot of connections can be described using network theory: hyperlinks between websites, citations between papers, relationships between people etc. This project aims to study how properties of a network, such as degree distribution (number of connections per node), change as the network grows, tweaking the ways with which the network grows. The main network to be studied is the Barabási-Albert model [1], where the probability of connecting to a node is proportional to its degree (equivalent to the case where a more popular website will attract more links to it). A scale-free behaviour (similar to as seen in Complexity Science) can be found in networks as well. Results as detailed in ```NetworksReport.pdf```.

Program written in Python 3, using the ```networkx``` package. A Kolmogorov-Smirnov (KS) test (```ks.py```) was also performed to evaluate the goodness of fit between simualted and theoretical data.

## References
1. A.-L. Barabási and R. Albert, Emergence of scaling in random networks Science, 286, 173 (1999).
