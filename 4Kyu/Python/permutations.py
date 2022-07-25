from itertools import permutations


def swap(string, i, j):
    if not string:
        return ''
    string_list = list(string)
    temp = string_list[i]
    string_list[i] = string_list[j]
    string_list[j] = temp
    return ''.join(string_list)


def permutations_2(prefix, input_chars, results):
    if len(input_chars) == 0:
        results.add(prefix)
    for i in range(len(input_chars)):
        new_prefix = prefix + input_chars[i]
        new_input = input_chars[:i] + input_chars[i + 1:]
        permutations_2(new_prefix, new_input, results)


def permutations(s):
    results = set()
    permutations_2("", s, results)
    return list(results)


class TestPermutations:
    def test_given_empty_list_return_empty_list(self):
        res = permutations('')
        assert res == ['']

    def test_given_a_single_element_list_return_list(self):
        res = permutations('a')
        assert res == ['a']

    def test_2(self):
        res = permutations('aabb')
        assert sorted(res) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
