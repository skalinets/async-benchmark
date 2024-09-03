import random
import asyncio
from memory_profiler import profile

async def generage_random_numbers():
    await asyncio.sleep(5)
    return random.randint(1, 10)


@profile
async def main(count):
    # def tasks ():
    #     for _ in range(count):
    #         yield generage_random_numbers()

    tasks = (generage_random_numbers() for _ in range(count))

    numbers = await asyncio.gather(*tasks)

    print(f"done, result: {sum(numbers)}")

if __name__ == "__main__":
    asyncio.run(main(1000))
