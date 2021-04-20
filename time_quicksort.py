import os


def gen_data(n_data):
    fname = f'data/quicksort-{n_data}.txt'
    if not os.path.isfile(fname):
        os.system(f'rust-bin/data_gen quicksort {fname} {n_data} {n_data}')
    return fname


def time_cmd(cmd):
    python_cmd = f"import os; os.system('{cmd}')"
    os.system(f'python -m timeit "{python_cmd}"')


def time_quicksort(n_data, n_threads):
    fname = gen_data(n_data)
    print('quicksort')
    print(f'data size: {n_data}, n_threads:{n_threads}')

    print('rust, serial:')
    cmd = f'rust-bin/quicksort {fname} serial > /dev/null'
    time_cmd(cmd)

    print('rust, parallel:')
    cmd = f'rust-bin/quicksort {fname} parallel {n_threads} > /dev/null'
    time_cmd(cmd)

    print('c, serial:')
    cmd = f'c-bin/quicksort-serial {fname} > /dev/null'
    time_cmd(cmd)

    print('c, parallel:')
    cmd = f'c-bin/quicksort-parallel {fname} {n_threads} > /dev/null'
    time_cmd(cmd)
    print('-' * 25)


if __name__ == '__main__':
    n_data = 50000
    for n_threads in [1, 2, 4, 8, 16, 32]:
        time_quicksort(n_data, n_threads)
