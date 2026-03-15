def sieve_of_eratosthenes(limit):
    # 创建一个布尔数组，并初始化为True
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是素数

    # 从2开始筛选
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # 将i的所有倍数标记为非素数
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    # 收集所有素数
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes

if __name__ == "__main__":
    primes = sieve_of_eratosthenes(100)
    print("100以内的素数:", primes)