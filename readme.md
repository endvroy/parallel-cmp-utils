# Parallel Comparison

## clone repos
`git clone --branch no-generics https://github.com/endvroy/parallel-cmp`

`git clone https://github.com/endvroy/parallel-cmp-c`

`git clone https://github.com/endvroy/parallel-cmp-utils`

## build Rust binaries
```
cd parallel-cmp
cargo build --release
```

## build C binaries
Unless you are building on Mac, comment out line 6 of `CMakeLists.txt` (`set(CMAKE_C_COMPILER /usr/local/bin/gcc-10)`). Otherwise, change this line to point to the correct `gcc` binary.

Then, the easiest way to build the C binaries is to load it as a project in CLion and build with a `release` profile.

Or, try the following commands:
```
cd parallel-cmp-c
mkdir cmake-build-release
gcc -fopenmp -std=c99 -o cmake-build-release/histogram-serial histogram.h histogram-serial.c
gcc -fopenmp -std=c99 -o cmake-build-release/histogram-parallel histogram.h histogram-parallel.c
gcc -fopenmp -std=c99 -o cmake-build-release/quicksort-serial quicksort.h quicksort-serial.c
gcc -fopenmp -std=c99 -o cmake-build-release/quicksort-parallel quicksort.h quicksort-parallel.c
gcc -fopenmp -std=c99 -o cmake-build-release/matmul-serial matmul.h matmul-serial.c
gcc -fopenmp -std=c99 -o cmake-build-release/matmul-parallel matmul.h matmul-parallel.c
```

## prepare for testing
1. Change `rust_proj_dir` and `c_proj_dir` in `prepare.py` (line 7 and 8) to be the corresponding repo paths.
2. Run `python3 prepare.py`. It will copy the compiled binaries into local directories and prepare the local directory structure for testing.

## test
```
python3 time_histogram.py
python3 time_matmul.py
python3 time_quicksort.py
```
You can change the problem size and number of threads in the main entry of these Python files.
