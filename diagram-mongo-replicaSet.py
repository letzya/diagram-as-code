# diagram.py
import ssl
import requests
from urllib.request import urlretrieve


from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.onprem.database import MongoDB
from diagrams.custom import Custom


# Download an image to be used into a Custom Node class
#tyk_url = "https://tyk.io/wp-content/uploads/2019/08/cropped-favicon-384x384.png"
#tyk_icon = "tykicon.png"
#x = requests.get(tyk_url)
#urlretrieve(tyk_url, tyk_icon)
#myIcon = Custom("Tyk Icon", tyk_icon)

#myIcon >> svc_group


with Diagram("MongoDB Active/Passive for DR", filename="mongodb-dr", show=False, direction="BT"):
    with Cluster("MongoDB Replica Set rs0",direction="LR"):
        with Cluster("Active site",direction='BT') as activeSite:
            with Cluster("AZ1"):
                with Cluster("EC2"):
                  svc_group = MongoDB("Node1 - P\nPriority 1")
            with Cluster("AZ2"):
                with Cluster("EC2"):
                  MongoDB("Node2 - S\nPriority 1")
            with Cluster("AZ3"):
                with Cluster("EC2"):
                  MongoDB("Node3 - S\nPriority 1")
        with Cluster("Passive site") as passiveSite:
            with Cluster("AZ1"):
                with Cluster("EC2"):
                  MongoDB("Node4 - S\nPriority 0.5")
            with Cluster("AZ2"):
                with Cluster("EC2"):
                  MongoDB("Node5 - S\nPriority 0.5")
            with Cluster("AZ3"):
                with Cluster("EC2"):
                  MongoDB("Node6 - S\nPriority 0.5")
        with Cluster("Arbiter site") as arbiter:
            with Cluster("AZ1"):
                with Cluster("EC2"):
                #  svc_group - Edge(color="brown", style="dashed") - MongoDB("Node7 - A")
                    MongoDB("Node7 - A")


    with Cluster("Index"):
           MongoDB("P - Primary")
           MongoDB("R - Replica/Scondary")
           MongoDB("A - Arbiter")

