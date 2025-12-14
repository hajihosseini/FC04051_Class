import pytest
import exam

@pytest.mark.skip("Not Implemented")
def test_q0_check_is_triangle():
    assert not exam.q0_check_is_triangle(3,2,1)
    assert not exam.q0_check_is_triangle(2,1,3)
    assert exam.q0_check_is_triangle(5,8,4)
    assert not exam.q0_check_is_triangle(4,2,8)
    assert exam.q0_check_is_triangle(9,7,7)
    assert exam.q0_check_is_triangle(10,15,20)
    assert exam.q0_check_is_triangle(6,4,5)


@pytest.mark.skip("Not Implemented")
def test_q1_Divisors_of_a_number():
    assert exam.q1_Divisors_of_a_number(1) == [1]
    assert exam.q1_Divisors_of_a_number(7) == [1,7]
    assert exam.q1_Divisors_of_a_number(12) == [1,2,3,4,6,12]
    assert exam.q1_Divisors_of_a_number(169) == [1,13,169]
    assert exam.q1_Divisors_of_a_number(144) == [1,2,3,4,6,8,9,12,16,18,24,36,48,72,144]


#@pytest.mark.skip("Not Implemented")
def test_q2_nth_prime_number():
    assert exam.q2_nth_prime_number(1)== 2
    assert exam.q2_nth_prime_number(2) == 3
    assert exam.q2_nth_prime_number(20) == 71
    assert exam.q2_nth_prime_number(5) == 11
    assert exam.q2_nth_prime_number(9) == 23
    assert exam.q2_nth_prime_number(15) == 47
    assert exam.q2_nth_prime_number(12)== 37


@pytest.mark.skip("Not Implemented")
def test_q3_insert_value_to_lis():
    assert exam.q3_insert_value_to_lis([], 5, 10) == [5]
    assert exam.q3_insert_value_to_lis(['a','c','z'], 5, 1) == ['a', 5, 'c','z']
    assert exam.q3_insert_value_to_lis([1,0,5,3], 8, 2) == [1,0,8,5,3]
    assert exam.q3_insert_value_to_lis([2,9,8,4,12,13], 11, 5) == [2,9,8,4,12,11,13]
    assert exam.q3_insert_value_to_lis(['x', 'w', 'p', 'e', 'r'], 'u', 3) == ['x', 'w', 'p', 'u', 'e', 'r']
    assert exam.q3_insert_value_to_lis([2,9,8,4,12,13], 11, 20) == [2,9,8,4,12,13,11]
    assert exam.q3_insert_value_to_lis([5,4,3,2,1], -5, 0) == [-5,5,4,3,2,1]
    assert exam.q3_insert_value_to_lis([12,-8,-9,14], 10, 1) == [12,10,-8,-9,14]
    assert exam.q3_insert_value_to_lis([101, -102, 103, 108, -210, 98], 300, 4) == [101, -102, 103, 108, 300, -210, 98]


@pytest.mark.skip("Not Implemented")
def test_q4_uinque_value_in_list():
    assert exam.q4_uinque_value_in_list([1,2,'a',6,2,8,1,'b','a',6]) == [1,2,'a',6,8,'b']
    assert exam.q4_uinque_value_in_list([10,8,12,8,5,10,4,2,12,7]) == [10,8,12,5,4,2,7]
    assert exam.q4_uinque_value_in_list(['a','b','z','y','b','x','y','d','d','e','d','b']) == ['a','b','z','y','x','d','e']
    assert exam.q4_uinque_value_in_list(['ax','by','bz','xa','ax','bd','bz']) == ['ax','by','bz','xa','bd']
    assert exam.q4_uinque_value_in_list([1,2,1,3,2,1,4,1,1,1,1,1,1,2]) == [1,2,3,4]


#@pytest.mark.skip("Not Implemented")
def test_q5_count_substrings():
    assert exam.q5_count_substring("aaa", "a") == 3
    assert exam.q5_count_substring("a", "aaa") == 0
    assert exam.q5_count_substring("abababa", "bab") == 2
    assert exam.q5_count_substring("abccccbd", "cc") == 3
    assert exam.q5_count_substring("xydwz", "ybw") == 0
    assert exam.q5_count_substring("ababab", "ab") == 3
    assert exam.q5_count_substring("ababab", "aba") == 2

#@pytest.mark.skip("Not Implemented")
def test_q6_reverse_prime_positions():
    input = [0,1,2,3,4,5,6,7,8,9]
    revin = [0,1,7,5,4,3,6,2,8,9]
    assert exam.q6_reverse_prime_positions(input) == revin
    input = [0,1,2,3,4,5,6,7,8,9]
    revin = [0,1,7,5,4,3,6,2,8,9]
    assert exam.q6_reverse_prime_positions(revin) == input

    input = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    revin = [0,1,19,17,4,13,6,11,8,9,10,7,12,5,14,15,16,3,18,2,20]
    assert exam.q6_reverse_prime_positions(input) == revin
    input = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    revin = [0,1,19,17,4,13,6,11,8,9,10,7,12,5,14,15,16,3,18,2,20]
    assert exam.q6_reverse_prime_positions(revin) == input

    input = [0,1,2,3,4,5]
    revin = [0,1,5,3,4,2]
    assert exam.q6_reverse_prime_positions(input) == revin
    input = [0,1,2,3,4,5]
    revin = [0,1,5,3,4,2]
    assert exam.q6_reverse_prime_positions(revin) == input

    
@pytest.mark.skip("Not Implemented")
def test_q7_is_symmetry():
    assert exam.q7_is_symmetry("aaa") 
    assert exam.q7_is_symmetry("aba") 
    assert exam.q7_is_symmetry("abba")
    assert exam.q7_is_symmetry("abdba")
    assert not exam.q7_is_symmetry("abdbd") 
    assert not exam.q7_is_symmetry("xyxyz") 
    assert exam.q7_is_symmetry("xx")
    assert exam.q7_is_symmetry("abcdefgfedcba")
    assert not exam.q7_is_symmetry("abab")


#@pytest.mark.skip("Not Implemented")
def test_q8_count_chrs():
    input = ["hello", "students", "university", "computer"]
    result = {'h': 1, 'e': 4, 'l': 2, 'o': 2, 's': 3, 't': 4, 'u': 3, 'd': 1, 'n': 2, 'i': 2, 'v': 1, 'r': 2, 'y': 1, 'c': 1, 'm': 1, 'p': 1}
    assert exam.q8_count_chrs(input) == result

    input = ["Palestine", "Lebanon", "Iran", "Yemen"]
    result = {'P': 1, 'a': 3, 'l': 1, 'e': 5, 's': 1, 't': 1, 'i': 1, 'n': 5, 'L': 1, 'b': 1, 'o': 1, 'I': 1, 'r': 1, 'Y': 1, 'm': 1}
    assert exam.q8_count_chrs(input) == result

    input = ["Computer", "Software", "Hardware", "Malware", "Network", "Artificial", "Intelligence"]
    result = {'C': 1, 'o': 3, 'm': 1, 'p': 1, 'u': 1, 't': 5, 'e': 8, 'r': 7, 'S': 1, 'f': 2, 'w': 4, 'a': 6, 'H': 1, 'd': 1, 'M': 1, 'l': 4, 'N': 1, 'k': 1, 'A': 1, 'i': 4, 'c': 2, 'I': 1, 'n': 2, 'g': 1}
    assert exam.q8_count_chrs(input) == result

