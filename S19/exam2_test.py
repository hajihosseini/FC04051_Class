import pytest
import exam2


#@pytest.mark.skip("Not Implemented")
def test_q0_pythagoras():
    assert exam2.q0_pythagoras(3, 4) == 5
    assert exam2.q0_pythagoras(4, 3) == 5
    assert exam2.q0_pythagoras(6, 8) == 10
    assert exam2.q0_pythagoras(8, 6) == 10
    assert exam2.q0_pythagoras(5, 12) == 13

@pytest.mark.skip("Not Implemented")
def test_q1_ghjklkjgfhkjljhgjkis_pythagoras():
    assert exam2.q1_is_pythagoras(3, 4, 5) 
    assert exam2.q1_is_pythagoras(5, 4, 3) 
    assert exam2.q1_is_pythagoras(4, 5, 3) 
    assert not exam2.q1_is_pythagoras(4, 5, 4) 

#@pytest.mark.skip("Not Implemented")
def test_q2_get_last_index():
    nums1 = [1, -1, 0, 2]
    assert exam2.q2_get_last_index(nums1, 1) == 0
    assert exam2.q2_get_last_index(nums1, -1) == 1
    assert exam2.q2_get_last_index(nums1, 4) == -1

    nums2 = [1, -1, 0, 1]
    assert exam2.q2_get_last_index(nums2, 1) == 3
    assert exam2.q2_get_last_index(nums2, 0) == 2
    
    nums2 = [1, 1, 1, 1]
    assert exam2.q2_get_last_index(nums2, 1) == 3
    assert exam2.q2_get_last_index(nums2, 0) == -1

@pytest.mark.skip("Not Implemented")
def test_q3_dedup():
    nums1 = [1, 2, 1, 2, 1, 2, 1]
    assert exam2.q3_dedup(nums1) == [1, 2]

    nums2 = [1, 2, 1, 3, 2, 1, 2, 1]
    assert exam2.q3_dedup(nums2) == [1, 2, 3]

    nums3 = [1, 1, -1, -1, 1]
    assert exam2.q3_dedup(nums3) == [1, -1]


@pytest.mark.skip("Not Implemented")
def test_q4_sum_of_dividable_indexes():
    nums = [1, 5, 2, -1, 4, 3, 7, 2, 1, 1, 1, 2, 3, 4, 5]
    assert exam2.q4_sum_of_dividable_indexes(nums, 2) == 24
    assert exam2.q4_sum_of_dividable_indexes(nums, 3) == 11
    assert exam2.q4_sum_of_dividable_indexes(nums, 4) == 9
    assert exam2.q4_sum_of_dividable_indexes(nums, 6) == 11

@pytest.mark.skip("Not Implemented")
def test_q5_concat_of_prime_positions():
    str = '0123456789'
    assert exam2.q5_concat_of_prime_positions(str) == '2357'
    str = 'abcdefghij'
    assert exam2.q5_concat_of_prime_positions(str) == 'cdfh'
    str = 'kjshlejlejrolvkereqseiryqlekroqu'
    assert exam2.q5_concat_of_prime_positions(str) == 'shelovesyou'

@pytest.mark.skip("Not Implemented")
def test_q6_contains_pattern():
    nums = [0, 1, 2, 4, 5, 4, 4, 3, 2, 2, 7, 8, 9, 9, 9, 1]
    assert exam2.q6_contains_pattern(nums, [8, 9, 9, 9])
    assert exam2.q6_contains_pattern(nums, [0, 1, 2])
    assert exam2.q6_contains_pattern(nums, [3, 2, 2])
    assert not exam2.q6_contains_pattern(nums, [9, 9, 9, 9])
    assert not exam2.q6_contains_pattern(nums, [2, 2, 2])
    assert not exam2.q6_contains_pattern(nums, [1, 2, 3])

@pytest.mark.skip("Not Implemented")
def test_q7_reverse_dict_mapping():
    dict1 = { 1:'ali', 2:'pejman', 3:'niki'}
    dict1r = { 'pejman':2, 'niki': 3, 'ali': 1}
    assert exam2.q7_reverse_dict_mapping(dict1) == dict1r
    assert exam2.q7_reverse_dict_mapping(dict1r) == dict1

    dict2 = { 'purple':42, 'green':11, 'red':25, 'yellow':31}
    dict2r = { 11:'green', 25:'red', 31:'yellow', 42: 'purple'}
    assert exam2.q7_reverse_dict_mapping(dict2) == dict2r
    assert exam2.q7_reverse_dict_mapping(dict2r) == dict2

@pytest.mark.skip("Not Implemented")
def test_q8_get_odd_file_lines():
    ftest1 = open("testfile1", "w")
    lines = [ 'a1\n', 'b2\n', 'c3\n', 'd4\n', 'e5\n']
    ftest1.writelines(lines)
    ftest1.close()
    ftest1_outfile = exam2.q8_get_odd_file_lines("testfile1")
    ftest1_out = open(ftest1_outfile)
    out_lines1 = ftest1_out.readlines()
    assert out_lines1 == ['a1\n', 'c3\n', 'e5\n']
    ftest1_out.close()

    ftest2 = open("testfile2", "w")
    lines = [ 'red\n', 'green\n', 'yellow\n', 'blue\n', 'orange\n', 'purple\n', 'navy\n']
    ftest2.writelines(lines)
    ftest2.close()
    ftest2_outfile = exam2.q8_get_odd_file_lines("testfile2")
    ftest2_out = open(ftest2_outfile)
    out_lines2 = ftest2_out.readlines()
    assert out_lines2 == ['red\n', 'yellow\n', 'orange\n', 'navy\n']
