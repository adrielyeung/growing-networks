# growing-networks
(Project for Complexity and Networks course in spring 2018)

A lot of connections can be described using network theory: hyperlinks between websites, citations between papers, relationships between people etc. This project aims to study how properties of a network, such as degree distribution (number of connections per node), change as the network grows, tweaking the ways with which the network grows. The main network to be studied is the Barab´asi-Albert model [1], where the probability of connecting to a node is proportional to its degree (equivalent to the case where a more popular website will attract more links to it). A scale-free behaviour (similar to as seen in Complexity Science) can be found in networks as well. Results as detailed in ```NetworksReport.pdf```.

Program written in Python, using the ```networkx``` package.

## References
1. A.-L. Barab\´asi and R. Albert, Emergence of scaling in random networks Science, 286, 173 (1999).

## Acknowledgements
Credits to Dr. Tim Evans for designing the project, and Max Falkenberg McGillivray for the code for log-binning of the data (```logbin6_2_2018.py```).
