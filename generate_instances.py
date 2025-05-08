import random as r
import os
import logging
import argparse

from batching_problem.generator import generate_instance

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

parameters = {
    "tiny":{
        "nbr_warehouse_items": 100,
        "nbr_orders": 10,
        "nbr_zones": 1,
        },
    "small":{
        "nbr_warehouse_items": 1_000,
        "nbr_orders": 50,
        "nbr_zones": 5,
    },
    "medium": {
        "nbr_warehouse_items": 10_000,
        "nbr_orders": 500,
        "nbr_zones": 10,
    },
    "large": {
        "nbr_warehouse_items": 100_000,
        "nbr_orders": 5_000,
        "nbr_zones": 50,
    },
    "huge": {
        "nbr_warehouse_items": 1_000_000,
        "nbr_orders": 50_000,
        "nbr_zones": 100,
    },
}




if __name__ == "__main__":
    args = parser.parse_args()
    r.seed(1)
    os.makedirs(args.dir, exist_ok=True)
    for size in args.instance_types:
        for nbr in range(args.nbr_instances):
            path = f"{args.dir}/{size}-{nbr}"
            os.makedirs(path, exist_ok=True)
            generate_instance(path, parameters[size])
