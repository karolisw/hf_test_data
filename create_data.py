import hyperfetch.tuning as hp  # type: ignore
import yaml

pruners = ["halving", "median", "patient", "percentile", "hyperband", "threshold", "none"]
samplers = ["random", "cmaes", "nsgaii", "tpe"]
environments_con = ["Pendulum-v1", "MountainCarContinuous-v0", ]
environments_dis = ["Acrobot-v1", "CartPole-v1", "MountainCar-v0"]
algs_con = ["sac", "td3", "a2c"] # done: ppo
algs_dis = ["ppo", "a2c", "dqn"]


def create_data_con(config_file):
    stream = open(config_file, 'r')
    data = yaml.safe_load(stream)  # dict

    for env in environments_con:
        # Update yaml file
        data.update({'env': env})
        with open(config_file, "w") as writer:
            yaml.safe_dump(data, writer)

        for alg in algs_con:
            # Update yaml file
            data.update({'alg': alg})
            with open(config_file, "w") as writer:
                yaml.safe_dump(data, writer)

            for pruner in pruners:
                # Update yaml file
                data.update({'pruner': pruner})
                with open(config_file, "w") as writer:
                    yaml.safe_dump(data, writer)

                for sampler in samplers:
                    # Update yaml file
                    data.update({'sampler': sampler})
                    data.update({'project_name': env + "_" + pruner + "_" + sampler})
                    with open(config_file, "w") as writer:
                        yaml.safe_dump(data, writer)
                    # Tune
                    hp.tune(config_path=config_file)


def create_data_dis(config_file):
    stream = open(config_file, 'r')
    data = yaml.safe_load(stream)  # dict

    for env in environments_dis:
        # Update yaml file
        data.update({'env': env})
        with open(config_file, "w") as writer:
            yaml.safe_dump(data, writer)

        for alg in algs_dis:
            # Update yaml file
            data.update({'alg': alg})
            with open(config_file, "w") as writer:
                yaml.safe_dump(data, writer)

            for pruner in pruners:
                # Update yaml file
                data.update({'pruner': pruner})
                with open(config_file, "w") as writer:
                    yaml.safe_dump(data, writer)

                for sampler in samplers:
                    # Update yaml file
                    data.update({'sampler': sampler})
                    data.update({'project_name': env + "_" + pruner + "_" + sampler})
                    with open(config_file, "w") as writer:
                        yaml.safe_dump(data, writer)
                    # Tune
                    hp.tune(config_file)


if __name__ == '__main__':
    create_data_con("tuning_parameters.yml")
    create_data_dis("tuning_parameters.yml")
