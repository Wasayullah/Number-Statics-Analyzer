def get_even_numbers(nums):
    return [n for n in nums if n % 2 == 0]


def get_odd_numbers(nums):
    return [n for n in nums if n % 2 != 0]


def get_positive_numbers(nums):
    return [n for n in nums if n > 0]


def get_negative_numbers(nums):
    return [n for n in nums if n < 0]


def get_zero_numbers(nums):
    return [n for n in nums if n == 0]
def analyze_numbers(nums):
    stats = {}

    stats['total_numbers'] = len(nums)
    stats['sum'] = sum(nums)
    stats['average'] = sum(nums) / len(nums)

    stats['maximum'] = max(nums)
    stats['minimum'] = min(nums)

    stats['even'] = get_even_numbers(nums)
    stats['odd'] = get_odd_numbers(nums)

    stats['positive'] = get_positive_numbers(nums)
    stats['negative'] = get_negative_numbers(nums)
    stats['zeros'] = get_zero_numbers(nums)

    return stats
def get_user_input():
    raw = input('Enter numbers separated by commas: ').strip()

    numbers = []
    for part in raw.split(','):
        part = part.strip()
        if part != '':
            numbers.append(int(part))

    return numbers
def display_results(nums, stats):
    total = stats['total_numbers']
    total_sum = stats['sum']
    avg = stats['average']
    max_num = stats['maximum']
    min_num = stats['minimum']
    even = stats['even']
    odd = stats['odd']
    positive = stats['positive']
    negative = stats['negative']
    zeros = stats['zeros']

    print()
    print('========== NUMBER ANALYSIS ==========')
    print()
    print(f'Numbers: {nums}')
    print()
    print(f'Total Numbers : {total}')
    print(f'Sum           : {total_sum}')
    print(f'Average       : {avg}')
    print()
    print(f'Maximum       : {max_num}')
    print(f'Minimum       : {min_num}')
    print()
    print(f'Even Numbers  : {even}')
    print(f'Odd Numbers   : {odd}')
    print()
    print(f'Positive      : {positive}')
    print(f'Negative      : {negative}')
    print(f'Zeros         : {zeros}')
    print()
    print('Number of each category:')
    print(f'  Even count     : {len(even)}')
    print(f'  Odd count      : {len(odd)}')
    print(f'  Positive count : {len(positive)}')
    print(f'  Negative count : {len(negative)}')
    print(f'  Zero count     : {len(zeros)}')
    print()
    print('=====================================')


def main():
    numbers = get_user_input()

    if not numbers:
        print('No numbers entered. Exiting.')
        return

    stats = analyze_numbers(numbers)
    display_results(numbers, stats)
if __name__ == '__main__':
    main()