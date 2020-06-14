import concurrent.futures
from tqdm import tqdm


def map_threads(func, _iterable):
    """Map function with iterable object in using thread pools."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = list(
            tqdm(
                executor.map(func, _iterable),
                total=len(_iterable),
                desc="Locations mined",
                position=1,
                smoothing=0.9,
            )
        )
    return result


def map_processes(func, _iterable):
    """Map function with iterable object in using process pools."""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = list(
            tqdm(
                executor.map(func, _iterable),
                total=len(_iterable),
                desc="Locations mined",
                position=1,
                smoothing=0.9,
            )
        )
    return result
