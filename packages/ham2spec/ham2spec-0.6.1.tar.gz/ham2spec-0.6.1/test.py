import numpy as np
import ham2spec
from time import perf_counter
from typing import List
from dataclasses import dataclass
from pathlib import Path


DEFAULT_CONFIG = {
    "xfrom": 11790,
    "xto": 13300,
    "xstep": 1,
    "bandwidth": 70,
    "abs_bws": [120 for _ in range(7)],
    "cd_bws": [120 for _ in range(7)],
    "band_cutoff": 4,
    "shift_diag": -2420,
    "dip_cor": 0.014,
    "delete_pig": 0,
    "use_shift_T": False,
    "scale": False,
    "overwrite": False,
    "save_figs": False,
    "save_intermediate": False,
    "empirical": False,
    "normalize": False
}


@dataclass(frozen=True)
class Config:
    xfrom: int
    xto: int
    xstep: int
    bandwidth: float
    abs_bws: List[float]
    cd_bws: List[float]
    band_cutoff: float
    shift_diag: float
    dip_cor: float
    delete_pig: int
    use_shift_T: bool
    scale: bool
    overwrite: bool
    save_figs: bool
    save_intermediate: bool
    empirical: bool
    normalize: bool

def main():
    validation_data_dir = Path.cwd() / "validation_data"
    ham = np.loadtxt(validation_data_dir / "hamiltonian.txt", delimiter=",", dtype=np.float64).reshape((7,7))
    mus_single = np.loadtxt(validation_data_dir / "dipole_moments.txt", dtype=np.float64).reshape((7,3))
    rs_single = np.loadtxt(validation_data_dir / "positions.txt", dtype=np.float64).reshape((7,3))
    config_opts = DEFAULT_CONFIG.copy()
    config_opts["bandwidth"] = 120
    config = Config(**config_opts)
    stick = ham2spec.compute_stick_spectrum(ham, mus_single, rs_single)
    mock_stick = {
        
    }
    b = ham2spec.compute_broadened_spectrum_from_stick(stick, config)
    b["abs"] *= 0
    # hams = np.empty((100, 7, 7))
    # mus = np.empty((100, 7, 3))
    # rs = np.empty((100, 7, 3))
    # for i in range(100):
    #     hams[i] = ham
    #     mus[i] = mus_single
    #     rs[i] = rs_single
    # n = 1_000
    # times = list()
    # for _ in range(n):
    #     t_start = perf_counter()
    #     # broadened = ham2spec.compute_broadened_spectra(hams, mus, rs, config)
    #     # broadened = ham2spec.compute_het_broadened_spectrum_from_stick(stick, config)
    #     broadened = ham2spec.compute_het_broadened_spectrum_from_ham(ham, mus_single, rs_single, config)
    #     t_stop = perf_counter()
    #     times.append(t_stop - t_start)
    # per_call = sum(times) / n * 1e6
    # print(f"{per_call:.3f}us per call")


if __name__ == "__main__":
    main()