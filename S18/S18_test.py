# import pytest
# import S18

# @pytest.mark.skip("Not Implemented")
# def test_q1_add_if_odd():
#     assert S14.q1_add_if_odd(5, 8) == 13
#     assert S14.q1_add_if_odd(5, 7) == -12
#     assert S14.q1_add_if_odd(2, -4) == 2
#     assert S14.q1_add_if_odd(-1, 14) == 13

# @pytest.mark.skip("Not Implemented")
# def test_q2_average():
#     assert S14.q2_average([19, 17.5, 12, 14.25, 18, 13]) == 15.62
#     assert S14.q2_average([20, 10.5, 11.75]) == 14.08
#     assert S14.q2_average([8.25, 12, 15.3, 16.9, 13.7]) == 13.23
#     assert S14.q2_average([19.75, 11.5, 13.25, 18.7]) == 15.8


# @pytest.mark.skip("Not Implemented")
# def test_q3_is_closest_to_average():
#     assert S14.q3_is_closest_to_average([19, 17.5, 12, 14.25, 18, 13]) == 14.25
#     assert S14.q3_is_closest_to_average([20, 10.5, 11.75]) == 11.75
#     assert S14.q3_is_closest_to_average([8.25, 12, 15.3, 16.9, 13.7]) == 13.7
#     assert S14.q3_is_closest_to_average([19.75, 11.5, 13.25, 18.7]) == 13.25


# @pytest.mark.skip("Not Implemented")
# def test_q4_split_word_to_characters():
#     assert S14.q4_split_word_to_characters("Computer") == ['C', 'o', 'm', 'p', 'u', 't', 'e', 'r']
#     assert S14.q4_split_word_to_characters("engineering") == ['e', 'n', 'g', 'i', 'n', 'e', 'e', 'r', 'i', 'n', 'g']
#     assert S14.q4_split_word_to_characters("algorithm") == ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm']
#     assert S14.q4_split_word_to_characters("data") == ['d', 'a', 't', 'a']


# @pytest.mark.skip("Not Implemented")
# def test_q5_average_all():
#     assert S14.q5_average_all([[19, 17.5, 12, 14.25, 18, 13],[20, 10.5, 11.75]]) == [15.62, 14.08, 14.85]
#     assert S14.q5_average_all([[8.25, 12, 15.3, 16.9, 13.7],[20, 10.5, 11.75, 14, 19],[19.25, 12, 13.3, 16.9, 13.7]]) == [13.23, 15.05, 15.03, 14.44]
#     assert S14.q5_average_all([[19.75, 11.5, 13.25, 18.7],[20, 10.5, 11.75]]) == [15.8, 14.08, 14.94] 


# @pytest.mark.skip("Not Implemented")
# def test_q6_Check_Arithmetic_or_Geometric():
#     assert S14.q6_Check_Arithmetic_or_Geometric([1,2,3,4,5,6],5) == 5
#     assert S14.q6_Check_Arithmetic_or_Geometric([4,7,10,13],7) == 22
#     assert S14.q6_Check_Arithmetic_or_Geometric([5,15,45,135],10) == 98415.0
#     assert S14.q6_Check_Arithmetic_or_Geometric([2,4,8,16],7) == 128.0
#     assert S14.q6_Check_Arithmetic_or_Geometric([1,1,2,3],7) == 0

# @pytest.mark.skip("Not Implemented")
# def test_q7_determinant_2_2():
#     assert S14.q7_determinant_2_2([[-4,2],[5,8]]) == -42
#     assert S14.q7_determinant_2_2([[3,5],[-2,6]]) == 28
#     assert S14.q7_determinant_2_2([[-3,-6],[2,4]]) == 0
#     assert S14.q7_determinant_2_2([[3,3],[-8,-4]]) ==  12   
