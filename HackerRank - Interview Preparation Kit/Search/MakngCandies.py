"""
Karl loves playing games on social networking sites. His current favorite is
CandyMaker, where the goal is to make candies.
Karl just started a level in which he must accumulate n candies starting with
m machines and w workers. In a single pass, he can make m * w candies. After
each pass, he can decide whether to spend some of his candies to buy more
machines or hire more workers. Buying a machine or hiring a worker costs p
units, and there is no limit to the number of machines he can own or workers
he can employ.

Karl wants to minimize the number of passes to obtain the required number of
candies at the end of a day. Determine that number of passes.
"""
import math


def optimal_alloc(n_cur, p, m, w):
    """
    Given current amount of money (candies), determine optimal allocation
    of machines and workers after purchase
    """
    if n_cur // p == 0:
        return m, w
    num_possible_buy = n_cur // p
    diff = math.fabs(m - w)
    if diff >= num_possible_buy:
        if m >= w:
            return m, w + num_possible_buy
        else:
            return m + num_possible_buy, w
    else:
        num_possible_buy -= diff
        if m >= w:
            w += diff
        else:
            m += diff
        return m + math.floor(num_possible_buy / 2), w + math.ceil(num_possible_buy / 2)


# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    """
    Args:
        m: Number of machines
        w: Number of workers
        p: Price of the candy
        n: Number of candies required

    Returns:
        Minimum passes required
    """
    count = 1
    n_cur = m * w
    count_saving_only = math.ceil(n / (m * w))
    while n_cur < n:
        if count_saving_only <= count:
            return count_saving_only

        if p > m * w:
            wait_to_buy = math.ceil((p - n_cur) / (m * w))
            n_after_wait = n_cur + wait_to_buy * (m * w)
            if n_after_wait >= n:
                return min(count + wait_to_buy, count_saving_only)
            count += wait_to_buy
            n_cur += wait_to_buy * (m * w)

        count_saving_from_now = count + math.ceil((n - n_cur) / (m * w))
        count_saving_only = min(count_saving_from_now, count_saving_only)

        m, w = optimal_alloc(n_cur, p, m, w)
        n_cur = n_cur % p + m * w
        count += 1
    return count


input = "3 1 2 12"  # Expected: 3
input = "1 1 6 45"  # Expected: 16
input = "499999 1000000 999996 1000000000000"  # Expected: 2
input = "5361 3918 8447708 989936375520"  # Expected: 3577
input = "5184889632 5184889632 20 10000"  # Expected: 1
input = "3 3 9 27"  # Expected: 3
args = [int(n) for n in input.split(" ")]
print(minimumPasses(*args))
