import os


def gen_data(n_data):
    fname = f'data/histogram-{n_data}.txt'
    if not os.path.isfile(fname):
        os.system(f'rust-bin/data_gen histogram {fname} {n_data}')
    return fname


def time_cmd(cmd):
    python_cmd = f"import os; os.system('{cmd}')"
    os.system(f'python -m timeit "{python_cmd}"')


def time_histogram(n_data, n_threads):
    fname = gen_data(n_data)

    print('histogram')
    print(f'data size: {n_data}, n_threads:{n_threads}')

    print('rust, serial:')
    cmd = f'rust-bin/histogram {fname} serial > /dev/null'
    time_cmd(cmd)

    print('rust, parallel:')
    cmd = f'rust-bin/histogram {fname} parallel {n_threads} > /dev/null'
    time_cmd(cmd)

    print('c, serial:')
    cmd = f'c-bin/histogram-serial {fname} > /dev/null'
    time_cmd(cmd)

    print('c, parallel:')
    cmd = f'c-bin/histogram-parallel {fname} {n_threads} > /dev/null'
    time_cmd(cmd)
    print('-' * 25)


if __name__ == '__main__':
    n_data = 4000
    n_threads = 4
    time_histogram(n_data, n_threads)
