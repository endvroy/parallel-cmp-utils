import os


def gen_data(n_rows_a, n_cols_a, n_cols_b):
    fname_a = f'data/matmul-a-{n_rows_a}-{n_cols_a}.txt'
    fname_b = f'data/matmul-b-{n_cols_a}-{n_cols_b}.txt'
    if not os.path.isfile(fname_a) or not os.path.isfile(fname_b):
        os.system(f'rust-bin/data_gen matrix {fname_a} {fname_b} {n_rows_a} {n_cols_a} {n_cols_b}')
    return fname_a, fname_b


def time_cmd(cmd):
    python_cmd = f"import os; os.system('{cmd}')"
    os.system(f'python -m timeit "{python_cmd}"')


def time_matmul(n_rows_a, n_cols_a, n_cols_b, n_threads):
    fname_a, fname_b = gen_data(n_rows_a, n_cols_a, n_cols_b)

    print('matmul')
    print(f'data size: {n_rows_a}*{n_cols_a}*{n_cols_b}, n_threads:{n_threads}')

    print('rust, serial:')
    cmd = f'rust-bin/matmul {fname_a} {fname_b} serial > /dev/null'
    time_cmd(cmd)

    print('rust, parallel:')
    cmd = f'rust-bin/matmul {fname_a} {fname_b} parallel {n_threads} > /dev/null'
    time_cmd(cmd)

    print('c, serial:')
    cmd = f'c-bin/matmul-serial {fname_a} {fname_b} > /dev/null'
    time_cmd(cmd)

    print('c, parallel:')
    cmd = f'c-bin/matmul-parallel {fname_a} {fname_b} {n_threads} > /dev/null'
    time_cmd(cmd)
    print('-' * 25)


if __name__ == '__main__':
    n_rows_a = 200
    n_cols_a = 400
    n_cols_b = 300
    for n_threads in [1, 2, 4, 8, 16, 32]:
        time_matmul(n_rows_a, n_cols_a, n_cols_b, n_threads)
