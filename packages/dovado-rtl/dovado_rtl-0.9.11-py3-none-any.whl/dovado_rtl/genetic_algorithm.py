from typing import List, Tuple, Optional
from collections import OrderedDict

from pymoo.core.callback import Callback
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.moo.age import AGEMOEA
from pymoo.factory import (
    get_sampling,
    get_crossover,
    get_mutation,
    get_termination,
)
from pymoo.optimize import minimize
from pymoo.core.repair import Repair


import numpy as np
from dovado_rtl.simple_types import Metric
from dovado_rtl.fitness import FitnessEvaluator
from pathlib import Path


class MyRepair(Repair):
    def __init__(self, power_of_2: List[str]) -> None:
        self.__power_of_2 = power_of_2
        super().__init__()

    def _do(self, problem, pop, **kwargs):
        for k, _ in enumerate(pop):
            x = pop[k].X
            for j in [i for i, v in enumerate(self.__power_of_2) if v == "y"]:
                v = x[j]
                v -= 1
                v |= v >> 1
                v |= v >> 2
                v |= v >> 4
                v |= v >> 8
                v |= v >> 16
                # next power of 2
                v += 1

                # previous power of 2
                n = v >> 1
                if np.random.random() < 0.5:
                    x[j] = n
                else:
                    x[j] = v
        return pop


class MyProblem(ElementwiseProblem):
    def __init__(
        self,
        fitness_evaluator: FitnessEvaluator,
        free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
        metrics: List[Metric],
    ):
        self.evaluator: FitnessEvaluator = fitness_evaluator
        self.metrics: List[Metric] = metrics
        super().__init__(
            n_var=len(free_parameters_range.keys()),
            n_obj=len(free_parameters_range.keys()),
            xl=[
                free_parameters_range[parameter][0]
                for parameter in free_parameters_range.keys()
            ],
            xu=[
                free_parameters_range[parameter][1]
                for parameter in free_parameters_range.keys()
            ],
            type_var=np.int,
        )

    def _evaluate(self, x: List[int], out, *args, **kwargs):
        fitness = self.evaluator.fitness(x)
        out["F"] = np.column_stack(fitness)

    def __is_power_of_2(self, n) -> int:
        return 0 if (n & (n - 1) == 0) and (n != 0) else 1


def optimize(
    evaluator: FitnessEvaluator,
    free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
    metrics: List[Metric],
    execution_time: Optional[str],
    power_of_2: Optional[List[str]],
    many_objective: bool = False,
) -> float:
    problem = MyProblem(evaluator, free_parameters_range, metrics)

    if many_objective:
        ga = AGEMOEA
    else:
        ga = NSGA2
    algorithm = ga(
        repair=MyRepair(power_of_2) if power_of_2 else None,
        pop_size=10 * len(free_parameters_range.keys()),
        n_offsprings=10 * len(free_parameters_range.keys()),
        sampling=get_sampling("int_random"),
        crossover=get_crossover("int_sbx", prob=0.9, eta=15),
        mutation=get_mutation("int_pm", eta=20),
        eliminate_duplicates=True,
    )

    if execution_time:
        termination = get_termination("time", execution_time)
        res = minimize(
            problem,
            algorithm,
            termination,
            seed=1,
            save_history=True,
            verbose=True,
        )
    else:
        res = minimize(
            problem,
            algorithm,
            seed=1,
            save_history=True,
            verbose=True,
        )
    design_space_path = "dovado_work/design_space.csv"
    objective_space_path = "dovado_work/objective_space.csv"
    Path(design_space_path).open("w")
    Path(objective_space_path).open("w")
    np.savetxt(
        design_space_path,
        res.X if res.X.ndim == 2 else np.reshape(res.X, (1, res.X.size)),
        delimiter=",",
        comments="",
        header=",".join(list(free_parameters_range.keys())),
    )
    np.savetxt(
        objective_space_path,
        res.F if res.F.ndim == 2 else np.reshape(res.F, (1, res.F.size)),
        delimiter=",",
        comments="",
        header=",".join(
            [
                i.utilisation[1]
                if i.utilisation
                else i.custom_metric[0]
                if i.custom_metric
                else "frequency"
                for i in metrics
            ]
        ),
    )
    return res.exec_time
