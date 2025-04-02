# RLfOLD
This is the implementation of RLfOLD, which is described in:

> [**RLfOLD: Reinforcement Learning from Online Demonstrations in Urban Autonomous Driving**](https://ojs.aaai.org/index.php/AAAI/article/view/29049)

>
> [Daniel Coelho](https://github.com/DanielCoelho112), 
[Miguel Oliveira](https://github.com/miguelriemoliveira),
[Vítor Santos](https://github.com/vitoruapt).
>
> [AAAI 2024](https://aaai.org/aaai-conference/)<br/>

If you find our work useful, please consider citing: 
```bibtex
@inproceedings{coelho2024rlfold,
  title={RLfOLD: Reinforcement Learning from Online Demonstrations in Urban Autonomous Driving},
  author={Coelho, Daniel and Oliveira, Miguel and Santos, Vitor},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={38},
  number={10},
  pages={11660--11668},
  year={2024}
}
```
  

## Setup
- Clone the repository with `git clone git@github.com:DanielCoelho112/rlfold.git`
- Download [CARLA 0.9.10.1](https://github.com/carla-simulator/carla/releases/tag/0.9.10.1).
- Run the docker container with `docker run -it --gpus all --network=host -v results_path:/root/results/rlfold -v rlfold_path:/root/rlfold danielc11/rlfold:0.0 bash`
where `results_path` is the path where the results will be written, and `rlfold_path` is the path of the rlfold repository.


## Set environment variables
```
export RLFOLD_ROOT=/home/jshiao/Dev/rlfold
export PYTHONPATH=$PYTHONPATH:/home/jshiao/Dev/rlfold

# $HOME
# $USER
```

## Training
- Start the CARLA server
- Run: `python3 rlfold/run/python3 main.py -en rlfold_original`


## Credits
Thanks to the authors of [End-to-End Urban Driving by Imitating a Reinforcement Learning Coach](https://github.com/zhejz/carla-roach)
for providing a framework to train RL agent in CARLA.
