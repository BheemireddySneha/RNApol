#To calculate the perturbation response scanning and generate a heatmap, you can use the following code snippet:

#python
from matplotlib import cm
import numpy as np
from lib.cli import CLI
from lib.utils import Logger
from lib.trajectory import load_trajectory

import argparse
import math
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def parse_traj(traj, topology=None, step=1, selected_atoms=["CA"], lazy_load=False):
    traj = load_trajectory(traj, topology, step, lazy_load)[0]

    residues = {}

    for frame in traj:
        for atom in frame.topology.atoms:
            if atom.name in selected_atoms:
                res = atom.residue.index

                ac = frame.xyz[0, atom.index]
                co_ords = [ac[0], ac[1], ac[2]]

                if res in residues:
                    residues[res].append(co_ords)
                else:
                    residues[res] = [co_ords]

    return residues


def mean_dot(m1, m2, size):
    DOT = np.zeros(size)

    for t in range(size):
        DOT[t] = np.dot(m1[t], m2[t])

    return np.mean(DOT)


def perturbation_response_scanning(traj_matrix, num_perturbations):
    sorted_residues = sorted(traj_matrix.keys())

    num_trajectories = len(traj_matrix[sorted_residues[0]])
    num_residues = len(traj_matrix)

    perturbation_response = np.zeros((num_residues, num_perturbations))

    for a, key_a in enumerate(sorted_residues):
        i = traj_matrix[key_a]
        resI = np.array(i)

        for p in range(num_perturbations):
            perturbation = np.random.normal(size=(num_trajectories, 3))
            perturbed_resI = resI + perturbation

            corr_matrix = np.zeros((num_trajectories,))

            for t in range(num_trajectories):
                corr_matrix[t] = np.corrcoef(resI[t], perturbed_resI[t])[0, 1]

            perturbation_response[a, p] = np.mean(corr_matrix)

    return perturbation_response


def plot_heatmap(data, title, output_prefix):
    M = np.array(data)

    ax = plt.subplots()[1]
    colors = [('white')] + [(cm.jet(i)) for i in range(40, 250)]

    new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=300)
    heatmap = ax.pcolor(M, cmap=new_map)

    fig = plt.gcf()
    ax.set_frame_on(False)
    ax.grid(False)

    plt.xticks(rotation=90)

    # Turn off all the ticks
    ax = plt.gca()
    for t in ax.xaxis.get_major_ticks():
        t.tick1line.set_visible = False
        t.tick2line.set_visible = False
        t.label.set_fontsize(8)

    for t in ax.yaxis.get_major_ticks():
        t.tick1line.set_visible = False
        t.tick2line.set_visible = False
        t.label.set_fontsize(8)

    plt.title(title, fontsize=16)
    plt.xlabel('Perturbation Index', fontsize=12)
    plt.ylabel("Residue Index", fontsize=12)

    plt.colorbar(heatmap, orientation="vertical")
    plt.savefig('%s.png' % output_prefix, dpi=300)
    plt.close('all')


def main(args):
    log.info("Preparing a trajectory matrix...\n")
    traj_matrix = parse_traj(args.trajectory, args.topology, args.step, lazy

_load=args.lazy_load)

    log.info("Calculating perturbation response scanning...\n")
    perturbation_response = perturbation_response_scanning(traj_matrix, args.num_perturbations)

    log.info("Plotting heat map...\n")
    plot_heatmap(perturbation_response, args.title, args.prefix)


log = Logger()

if __name__ == "__main__":
    # parse cmd arguments
    parser = argparse.ArgumentParser()

    # custom arguments
    parser.add_argument("--trajectory", help="Trajectory file")
    parser.add_argument("--topology", help="Reference PDB file (must contain the same number of atoms as the trajectory)")
    parser.add_argument("--step", help="Size of the step to take when iterating the trajectory frames", type=int)
    parser.add_argument("--lazy-load",
                        help="Iterate through the trajectory, loading one frame into memory at a time (memory-efficient for large trajectories)",
                        action='store_true', default=False)

    parser.add_argument("--num-perturbations", help="Number of perturbations", type=int, default=1000)
    parser.add_argument("--title", help="Title for heatmap", default="Perturbation Response Scanning")
    parser.add_argument("--prefix", help="Prefix for output files", default="perturbation_response")

    CLI(parser, main, log)
```

You can run this code by providing the necessary command-line arguments. For example:

```
python your_script.py --trajectory 5uh5.xtc --topology 5uh5.pdb --step 1 --num-perturbations 1000
```

This will calculate the perturbation response scanning for the given trajectory and topology files using 1000 perturbations and generate a heatmap as an output. Adjust the arguments according to your specific needs.
