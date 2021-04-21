import numpy as np
import matplotlib.pyplot as plt

n_threads = np.array([1, 2, 4, 8, 16, 32])
histogram_rust_serial = np.array([30.1, 30, 30.2, 30, 29.9, 29.9])
histogram_rust_parallel = np.array([30.6, 30.6, 31.6, 34.4, 34.4, 38.5])
histogram_c_serial = np.array([29.1, 29.3, 29.1, 29.1, 29, 29])
histogram_c_parallel = np.array([29, 30.5, 29.2, 29.2, 28.9, 29.2])

histogram_rust_speedup = histogram_rust_serial / histogram_rust_parallel
histogram_c_speedup = histogram_c_serial / histogram_c_parallel

matmul_rust_serial = np.array([101, 100, 100, 101, 101, 101])
matmul_rust_parallel = np.array([1050, 437, 235, 202, 311, 358])
matmul_c_serial = np.array([179, 178, 180, 180, 179, 181])
matmul_c_parallel = np.array([255, 253, 255, 257, 254, 254])

matmul_rust_speedup = matmul_rust_serial / matmul_rust_parallel
matmul_c_speedup = matmul_c_serial / matmul_c_parallel

quicksort_rust_serial = np.array([60.9, 60.8, 60.5, 60.8, 62.4, 62])
quicksort_rust_parallel = np.array([64.5, 56.6, 53.8, 53.4, 55.7, 59.6])
quicksort_c_serial = np.array([248, 247, 247, 248, 250, 248])
quicksort_c_parallel = np.array([248, 249, 251, 250, 256, 254])

quicksort_rust_speedup = quicksort_rust_serial / quicksort_rust_parallel
quicksort_c_speedup = quicksort_c_serial / quicksort_c_parallel


def draw_fig(n_threads, speedup, title, save_path=None):
    fig, ax = plt.subplots()
    ind = np.arange(len(n_threads))
    bars = ax.bar(ind, speedup)
    ax.set_xticks(ind)
    ax.set_xticklabels(n_threads)
    ax.set_xlabel('threads')
    ax.set_ylabel('speedup')
    ax.set_title(title)
    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)


if __name__ == '__main__':
    draw_fig(n_threads, matmul_rust_speedup, 'Matrix multiplication, Rust', 'figs/matmul_rust.png')
    draw_fig(n_threads, matmul_c_speedup, 'Matrix multiplication, C', 'figs/matmul_c.png')
    draw_fig(n_threads, histogram_rust_speedup, 'Histogram, Rust', 'figs/histogram_rust.png')
    draw_fig(n_threads, histogram_c_speedup, 'Histogram, C', 'figs/histogram_c.png')
    draw_fig(n_threads, quicksort_rust_speedup, 'Quicksort, Rust', 'figs/quicksort_rust.png')
    draw_fig(n_threads, quicksort_c_speedup, 'Quicksort, C', 'figs/quicksort_c.png')
