#!/bin/bash
source env/bin/activate
python src/main.py --config=$1 --env-config=sc2 with env_args.map_name=$2 use_tensorboard=True name=$1$2
deactivate
