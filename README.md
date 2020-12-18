# QVMix and QVMix-Max: Extending the Deep Quality-Value Family of Algorithms to Cooperative Multi-Agent Reinforcement Learning


## Installation

Set up StarCraft II and SMAC:

```shell
./install_sc2.sh
```

This will download SC2 into the 3rdparty folder and copy the maps necessary to run over.

The requirements.txt file can be used to install the necessary packages into a virtual environment.

Set up the virtual envrionment with python3.6:

```
./install_venv.sh
```
## Run an experiment 

```shell
source env/bin/activate
python src/main.py --config=qv --env-config=sc2 with env_args.map_name=3m use_tensorboard=True
deactivate

```

## Paper hypeparameters
The [config files](paleroy/qvmix/src/config) provided are the one used to train the different methods for the experiments of the paper.

You can use the `run_all.sh` script to train sequentially each of the seven method on a given map.


## Citation
If you use QVMix implementation in your own work, please cite our paper:

```
TBA
```

## Credits
This code has been adapted from the [Python MARL framework (pymarl)](github.com/oxwhirl/pymarl) and from the [Maven implementation](https://github.com/AnujMahajanOxf/MAVEN).