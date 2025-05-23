from carla_env.envs.base_env import CarlaEnv


class EndlessEnv(CarlaEnv):
    def __init__(self, carla_map, host, port, obs_configs,  terminal_configs, reward_configs, num_zombie_vehicles, num_zombie_walkers, weather_group, carla_fps, tm_port, seed):
        all_tasks = self.build_all_tasks(num_zombie_vehicles, num_zombie_walkers, weather_group)
        super().__init__(carla_map, host, port, obs_configs, terminal_configs, reward_configs, all_tasks, carla_fps, tm_port, seed)

    @staticmethod
    def build_all_tasks(num_zombie_vehicles, num_zombie_walkers, weather_group):
        if weather_group == 'new':
            weathers = ['SoftRainSunset', 'WetSunset']
        elif weather_group == 'train':
            weathers = ['ClearNoon', 'WetNoon', 'HardRainNoon', 'ClearSunset']
        elif weather_group == 'all':
            weathers = ['ClearNoon', 'CloudyNoon', 'WetNoon', 'WetCloudyNoon', 'SoftRainNoon', 'MidRainyNoon',
                        'HardRainNoon', 'ClearSunset', 'CloudySunset', 'WetSunset', 'WetCloudySunset',
                        'SoftRainSunset', 'MidRainSunset', 'HardRainSunset']
        else:
            weathers = [weather_group]

        actor_configs_dict = {
            'ego_vehicles': {
                'hero': {'model': 'vehicle.lincoln.mkz_2017'}
            }
        }
        route_descriptions_dict = {
            'ego_vehicles': {
                'hero': []
            }
        }
        endless_dict = {
            'ego_vehicles': {
                'hero': True
            }
        }
        all_tasks = []
        for weather in weathers:
            task = {
                'weather': weather,
                'description_folder': 'None',
                'route_id': 0,
                'num_zombie_vehicles': num_zombie_vehicles,
                'num_zombie_walkers': num_zombie_walkers,
                'ego_vehicles': {
                    'routes': route_descriptions_dict['ego_vehicles'],
                    'actors': actor_configs_dict['ego_vehicles'],
                    'endless': endless_dict['ego_vehicles']
                },
                'scenario_actors': {},
            }
            all_tasks.append(task)

        return all_tasks
