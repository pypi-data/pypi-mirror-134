import numpy as np 
import matplotlib.pyplot as plt
import numpy.matlib
from .res import Res
from .PSO import PSO_alg
import time
from joblib import Parallel, delayed


def run_pso(n_vars, fitness_function, low_bounds, up_bounds, initial_solution=[],brm_function = 4,n_jobs=-2,direct_repair=None,
            perc_repair=0.1,wmax = 0.5,wmin = 0.1,c1min = 0,c1max = 0.4,c2min = 0.1,c2max = 2,n_iterations = 100,
            n_particles = 10,n_trials = 30, show_fitness_grapic=False, show_particle_graphics=False, verbose=True):
    """
    Function to execute the pso algorithm

    Parameters:
        n_vars: int
            The number of variables present in the solution
        fitness_function: function
            The fitness function
        low_bounds: matrix
            Matrix containing the lowest boundaries the solution array might have for each particle
        up_bounds: matrix
            Matrix containing the highest boundaries the solution array might have for each particle
        initial_solution: matrix or array
            Matrix or array containing the initial solutions or solution
        brm_function: function
            Function to handle boundary constraint violation. One of: 
                - BRM_control_brick_wall_penalty (1)
                - BRM_control_adaptive_penalty (2)
                - BRM_control_random_reinitialization (3)
                - BRM_control_bounce_back (4)
                - Custom one created by the user
        n_jobs: int
            Number of concurrently running jobs: 
                - For the value -1 all CPUs are used. 
                - For the value 1 there is no parallel processing.
                - For values below -1, the number of CPUs used is given by (n_cpus + 1 + n_jobs).
                - For any other positive values, the number given is the number of CPUs used.
        direct_repair: function
            The direct repair function
        perc_repair: float
            Value between 0 and 1 that determines the percentage of iterations starting from the end where a repair function is applied
        wmin: float
            The minimum value of the itertia weight
        wmax: float
            The maximum value of the inertia weight
        c1min: float
            Minimum value of the acceleration coefficient c1
        c1max: float
            Maximum value of the acceleration coefficient c1
        c2min: float
            Minimum value of the acceleration coefficient c2
        c2max: float
            Maximum value of the acceleration coefficient c1 
        n_iterations: int
            The total number of iterations
        n_particles: int
            The total number of particles
        n_trials: int
            The total number of trials
        show_fitness_graphic: bol
            Boolean that indicates if the fitness graphic is to be shown or not
        show_particles_graphics: bol
            Boolean that indicates if the particles graphics are to be shown or not (Only works with solutions of 2 dimensions)
    
    Returns: Result
        The result of running the pso algorithm
    """
    if n_vars<=0:
        raise ValueError("n_vars must be value above 0")

    if direct_repair != None:
        if perc_repair < 0 or perc_repair > 1:
            raise ValueError("perc_repair must be between 0 and 1")

    if n_iterations < 1:
        raise ValueError("n_iterations must at least be 1")

    if n_particles < 1:
        raise ValueError("n_particles must at least be 1")

    if n_trials < 1:
        raise ValueError("n_trials must be at least be 1")

    if c1min < 0:
        raise ValueError("c1min must at least be 0")

    if c2min < 0:
        raise ValueError("c2min must at least be 0")

    if wmin < 0:
        raise ValueError("wmin must at least be 0")

    if wmax < wmin:
        raise ValueError("wmax must have a bigger or equal value than wmin")

    if c1max < c1min:
        raise ValueError("c1max must have a bigger or equal value than c1min")

    if c2max < c2min:
        raise ValueError("c2max must have a bigger or equal value than c2min")

    if isinstance(up_bounds, list):
        if len(up_bounds)!=n_vars:
            raise ValueError("Up matrix must have a length of "+str(n_vars))
    else:
        up_bounds = [up_bounds]*n_vars
    
    if isinstance(low_bounds, list):
        if len(low_bounds)!=n_vars:
            raise ValueError("Low matrix must have a length of "+str(n_vars))
    else:
        low_bounds = [low_bounds]*n_vars

    
    if initial_solution!=[]:
        if all(isinstance(ele, list) for ele in initial_solution):
            if len(initial_solution)!= n_particles:
                raise ValueError("Initial solution must have a length of "+str(n_particles))
            for e in initial_solution:
                if len(e)!=n_vars:
                    raise ValueError("Initial solution's elements must have a length of "+str(n_vars))
                if any([e[i]<low_bounds[i] for i in range(len(e))]) or any([e[i]>up_bounds[i] for i in range(len(e))]):
                    raise ValueError("Initial solution's elements value must be between the low and the up matrix values")
            initial_solution= np.array(initial_solution, dtype=float)
        else:
            if len(initial_solution)!=n_vars and len(initial_solution)!=0:
                raise ValueError("Initial solution must have a length of "+str(n_vars))
            elif any([initial_solution[i]<low_bounds[i] for i in range(len(initial_solution))]) or any([initial_solution[i]>up_bounds[i] for i in range(len(initial_solution))]):
                raise ValueError("Initial solution values must be between the low and the up matrix values")
            else:
                initial_solution = np.array([initial_solution], dtype=float)
    
    low_bounds = np.matlib.repmat(low_bounds,n_particles,1)
    up_bounds = np.matlib.repmat(up_bounds,n_particles,1)
    fitness_value    = np.array([float('inf') for _ in range(n_trials)])
    it_fitness_value = np.array([[float('inf') for _ in range(n_iterations)] for _ in range(n_trials)])
    solution         = np.array([[float('inf') for _ in range(n_vars)] for _ in range(n_trials)])
    exec_times       = np.array([float('inf') for _ in range(n_trials)])
    if show_particle_graphics and n_vars==2:
        for nr in range(n_trials):
            i_time = time.time()
            fitness_value[nr],it_fitness_value[nr],solution[nr] =PSO_alg(wmax,wmin,c1min,c1max,c2min,c2max,initial_solution,
                                brm_function,(1-perc_repair),n_iterations,n_particles,n_vars,
                                up_bounds,low_bounds,fitness_function, direct_repair, show_particle_graphics)
            exec_times[nr] = time.time() - i_time
            if verbose:
                print("Number of trial =", nr+1, "... Fitness Value = ", fitness_value[nr])
            plt.show()
    else:
        i_time = time.time()
        parallel = Parallel(n_jobs=n_jobs)
        result = parallel(delayed(PSO_alg)(wmax,wmin,c1min,c1max,c2min,c2max,initial_solution,
                                brm_function,(1-perc_repair),n_iterations,n_particles,n_vars,
                                up_bounds,low_bounds,fitness_function, direct_repair, show_particle_graphics) for _ in range(n_trials))
        exec_times = time.time() - i_time
        for nr in range(n_trials):
            fitness_value[nr],it_fitness_value[nr],solution[nr] = result[nr]
            if verbose:
                print("Number of trial =", nr+1, "... Fitness Value = ", fitness_value[nr])
    mean = np.mean(it_fitness_value, axis=0)
    std = np.std(it_fitness_value,axis=0)
    if show_fitness_grapic:
        plt.plot(mean)
        plt.fill_between(range(len(it_fitness_value[0])),mean-std,mean+std,facecolor='#95d3ff',alpha=.3 )
        plt.xlim(left=0)
        plt.xlabel("Iterations")
        plt.ylabel("Fitness value")
        plt.show()

    n = np.argmin(fitness_value)
    if verbose:
        print(f"Best fitness value is {fitness_value[n]:.6e} found in run {n+1}")
        print(f"Average fitness_value: {np.mean(fitness_value):.6e}")
        print(f"Standard deviation: {np.std(fitness_value):.6e}")
        print(f"Total execution time: {np.sum(exec_times):.2e}")
        print(f"Average execution time: {np.sum(exec_times)/n_trials:.2e}")
        numpy.set_printoptions(precision=6)
        print(f"Solution: {solution[n]}")
    #current_process().t
    return Res(fitness_value[n], it_fitness_value, solution[n], np.sum(exec_times), np.sum(exec_times)/n_trials)
