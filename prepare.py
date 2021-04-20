import os
import shutil

os.makedirs('rust-bin', exist_ok=True)
os.makedirs('c-bin', exist_ok=True)
os.makedirs('data', exist_ok=True)
rust_proj_dir = '/Users/ruoyi/Projects/CLionProjects/parallel-cmp'
c_proj_dir = '/Users/ruoyi/Projects/CLionProjects/parallel-cmp-c'

# copy rust binaries
for name in ['data_gen', 'quicksort', 'matmul', 'histogram']:
    shutil.copy(f'{rust_proj_dir}/target/release/{name}', f'rust-bin/{name}')

# copy c binaries
for name in ['quicksort', 'matmul', 'histogram']:
    for version in ['serial', 'parallel']:
        shutil.copy(f'{c_proj_dir}/cmake-build-release/{name}-{version}', f'c-bin/{name}-{version}')
