#4) Making a progress bar for all the work that I do

    # Features:
        # 1 -> An 'iterable' wrapped in 'tqdm.tqdm' will display a progress bar
import tqdm
import random

# for i in tqdm.tqdm(range(100)):
#     # do something slow
#     _ = [random.random() for _ in range(1000000)]

        # Shows fraction of loop complete / time elapsed / and est time remaining

        # 2 -> when wrapping a call to a range, we can use 'tqdm.trange
            ## *also can add a description of the progress bar w/ a "with" statement

from typing import List

def primes_up_to(n: int) -> List[int]:
    primes = [2]

    with tqdm.trange(3, n) as t:
        for i in t:
            # is is prime if no smaller prime divides it
            i_is_prime = not any(i % p == 0 for p in primes)
            if i_is_prime:
                primes.append(i)

            t.set_description(f"{len(primes)} primes")
    return primes

my_primes = primes_up_to(100_000)