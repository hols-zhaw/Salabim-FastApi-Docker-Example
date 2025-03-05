import salabim as sim


class Process(sim.Component):
    def process(self):
        self.request(self.env.resource)
        self.hold(self.env.processing_time)
        self.release(self.env.resource)


def simulate(
    random_seed="*",
    run_duration=100,
    iat_mean=1,
    pt_mean=0.8,
):
    params = locals().copy()
    env = sim.Environment(random_seed=random_seed)
    env.resource = sim.Resource("Resource")
    env.processing_time = sim.Exponential(pt_mean)
    sim.ComponentGenerator(Process, iat=sim.Exponential(iat_mean))
    env.run(run_duration)
    return {
        **params,
        "waiting_time_mean": env.resource.requesters().length_of_stay.mean(),
        "waiting_time_std": env.resource.requesters().length_of_stay.std(),
        "waiting_time_max": env.resource.requesters().length_of_stay.maximum(),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(simulate())
