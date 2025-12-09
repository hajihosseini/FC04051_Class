import turtle
import pytest
import exam1_1402

@pytest.mark.skip()
def test_q0_manhatan_distance():
    x1, y1, x2, y2 = 0, 0, 1, 0
    assert 1 == exam1_1402.q0_manhatan_distance(x1, y1, x2, y2)

    x1, y1, x2, y2 = 0, 0, 1, 1
    assert 2 == exam1_1402.q0_manhatan_distance(x1, y1, x2, y2)

    x1, y1, x2, y2 = -1, -3, 1, 3
    assert 8 == exam1_1402.q0_manhatan_distance(x1, y1, x2, y2)

    x1, y1, x2, y2 = 5, 1, -1, 2
    assert 7 == exam1_1402.q0_manhatan_distance(x1, y1, x2, y2)

@pytest.mark.skip()
def test_q1_closest_neighbor():
    assert exam1_1402.q1_closest_neighbor([1, 5, 2]) == 3
    assert exam1_1402.q1_closest_neighbor([1, 2, 5, 8, 1, 4, -3, 5, 1, 7]) == 1
    assert exam1_1402.q1_closest_neighbor([1, 10, 5, 8, 1, 5, -3, 5, 1, 7]) == 3

@pytest.mark.skip()
def test_q2_add_nums():
    assert exam1_1402.q2_add_nums([1, 1, 1, 1], [-1, 0, -1, 0]) == [0, 1, 0, 1]
    assert exam1_1402.q2_add_nums([1, 2, 1, 5, 8], [1, 7, -1, -4, 2]) == [2, 9, 0, 1, 10]

@pytest.mark.skip()
def test_q3_closest_two_friends():
    assert exam1_1402.q3_closest_two_friends([1, 5, 2]) == (0, 2, 1)
    assert exam1_1402.q3_closest_two_friends([1, -5, 5, 8, -1, 4, -3, 5, 12, 7]) == (2, 7, 0)
    assert exam1_1402.q3_closest_two_friends([11, 2, -5, 8, 17, -9, -3, 5, 20, -7]) == (2, 6, 2)

@pytest.mark.skip()
def test_q4_apply_rule_once():
    assert exam1_1402.q4_apply_rule_once('A', ['A', 'AB']) == 'AB'
    assert exam1_1402.q4_apply_rule_once('AA', ['A', 'AB']) == 'ABAB'
    assert exam1_1402.q4_apply_rule_once('ABA', ['A', 'AB']) == 'ABBAB'
    assert exam1_1402.q4_apply_rule_once('A', ['B', 'A']) == 'A'
    assert exam1_1402.q4_apply_rule_once('ABABA', ['A', 'BB']) == 'BBBBBBBB'

@pytest.mark.skip()
def test_q5_apply_rules_once():
    rule1 = ['A', 'B']
    rule2 = ['B', 'AB']
    assert exam1_1402.q5_apply_rules_once('A', [rule1, rule2]) == 'AB'
    assert exam1_1402.q5_apply_rules_once('AB', [rule1, rule2]) == 'ABAB'
    rule1 = ['A', 'ABA']
    rule2 = ['B', 'BAB']
    assert exam1_1402.q5_apply_rules_once('A', [rule1, rule2]) == 'ABABA'
    assert exam1_1402.q5_apply_rules_once('AB', [rule1, rule2]) == 'ABABABAB'
    rule1 = ['A', 'C']
    rule2 = ['C', 'B']
    rule3 = ['B', 'A']
    assert exam1_1402.q5_apply_rules_once('A', [rule1, rule2, rule3]) == 'A'
    assert exam1_1402.q5_apply_rules_once('A', [rule1, rule3, rule2]) == 'B'
    assert exam1_1402.q5_apply_rules_once('ABCABC', [rule1, rule2, rule3]) == 'AAAAAA'
    assert exam1_1402.q5_apply_rules_once('ABCABC', [rule1, rule3, rule2]) == 'BABBAB'

@pytest.mark.skip()
def test_q6_apply_rules_n():
    rule1 = ['A', 'AB']
    assert exam1_1402.q6_apply_rules_n('A', [rule1], 1) == 'AB'
    assert exam1_1402.q6_apply_rules_n('A', [rule1], 2) == 'ABB'
    assert exam1_1402.q6_apply_rules_n('A', [rule1], 3) == 'ABBB'
    assert exam1_1402.q6_apply_rules_n('A', [rule1], 4) == 'ABBBB'
    rule2 = ['B', 'AB']
    assert exam1_1402.q6_apply_rules_n('A', [rule1, rule2], 3) == 'AABAABABAABAABABAABAB'
    assert exam1_1402.q6_apply_rules_n('A', [rule1, rule2], 4) == 'AABAABABAABAABABAABABAABAABABAABAABABAABABAABAABABAABAB'
    rule1 = ['A', 'CA']
    rule2 = ['C', 'BC']
    rule3 = ['B', 'AC']
    assert exam1_1402.q6_apply_rules_n('A', [rule1, rule2, rule3], 2) == 'ACCAACCACCACCA'
    assert exam1_1402.q6_apply_rules_n('A', [rule1, rule2, rule3], 3) == 'ACCAACCACCACCAACCAACCACCACCAACCACCACCAACCACCACCA'

@pytest.mark.skip()
def test_q7_turtle_follows_instruction():
    t = init_turtle()
    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, 'F', 100, 0, [])
    assert_turtle_states(t, locs, heads, cols, [(0, 100)], [90])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, 'F', 100, 0, [])
    assert_turtle_states(t, locs, heads, cols, [(0, 200)], [90])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, '+', 100, 90, [])
    assert_turtle_states(t, locs, heads, cols, [(0, 200)], [0])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, '+', 100, 90, [])
    assert_turtle_states(t, locs, heads, cols, [(0, 200)], [270])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, '-', 100, 45, [])
    assert_turtle_states(t, locs, heads, cols, [(0, 200)], [315])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, '-', 100, 45, [])
    assert_turtle_states(t, locs, heads, cols, [(0, 200)], [0])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, 'FF', 100, 90, [])
    assert_turtle_states(t, locs, heads, cols, [(100, 200), (200, 200)], [0, 0])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, '++', 100, 45, [])
    assert_turtle_states(t, locs, heads, cols, [(200, 200), (200, 200)], [315, 270])

    locs, heads, cols = exam1_1402.q7_turtle_follows_instruction(t, 'F+F+F', 200, 90, [])
    assert_turtle_states(t, locs, heads, cols, [(200, 0),(200, 0),(0, 0),(0, 0),(0, 200)], [270,180,180,90,90])

    cleanup_turtle()    


@pytest.mark.skip()
def test_q8_turtle_follows_instruction2():
    t = init_turtle()
    exam1_1402.q8_turtle_follows_instruction2(t, 'F[F]', 100, 90, [])
    assert (0, 100) == pytest.approx(t.position()) and 90 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, 'F[F+F]', 100, 90, [])
    assert (0, 200) == pytest.approx(t.position()) and 90 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, '[F[F[F]', 100, 90, [])
    assert (0, 400) == pytest.approx(t.position()) and 90 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, '[F[F[F]]', 100, 90, [])
    assert (0, 500) == pytest.approx(t.position()) and 90 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, '[F[F[F]]]', 100, 90, [])
    assert (0, 500) == pytest.approx(t.position()) and 90 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, '[+[+[+', 100, 10, [])
    assert (0, 500) == pytest.approx(t.position()) and 60 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, '[+[+[+]', 100, 10, [])
    assert (0, 500) == pytest.approx(t.position()) and 40 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, '[+[+[+]]', 100, 10, [])
    assert (0, 500) == pytest.approx(t.position()) and 30 == pytest.approx(t.heading())

    exam1_1402.q8_turtle_follows_instruction2(t, '[+[+[+]]]', 100, 10, [])
    assert (0, 500) == pytest.approx(t.position()) and 30 == pytest.approx(t.heading())


@pytest.mark.skip()
def test_q9_turtle_following_rules():
    colors = [(140/255, 80/255, 60/255), (24/255, 180/255, 24/255), (48/255, 220/255, 48/255), (64/255, 255/255, 64/255)]
    start = 'F'
    rule = ['F', 'C0FF+[C1+F-F-F]-[C2-F+F+F]']
    rules = [rule]
    instructions = exam1_1402.q6_apply_rules_n(start, rules, 5)
    t = init_turtle()
    t.penup()
    t.setpos(0, -200)
    t.pendown()
    exam1_1402.q8_turtle_follows_instruction2(t, instructions, 4, 25, colors)
    turtle.getscreen().getcanvas().postscript(colormode='color', file='beautiful_rules1.ps')
    # turtle.mainloop()
    t.reset()
    t.penup()
    t.setpos(0, -200)
    t.left(90)
    t.pendown()
    start = 'FX'
    rule1 = ['F','C0FF-[C1-F+F]+[C2+F-F]']
    rule2 = ['X','C0FF+[C1+F]+[C3-F]']
    rules = [rule1, rule2]
    instructions = exam1_1402.q6_apply_rules_n(start, rules, 5)
    exam1_1402.q8_turtle_follows_instruction2(t, instructions, 4, 25, colors)
    turtle.getscreen().getcanvas().postscript(colormode='color', file='beautiful_rules2.ps')
    # turtle.mainloop()


## Helper Functions. Do not touch/look
def assert_turtle_states(t, locs, heads, cols, exp_locs, exp_heads):
    assert exp_locs[-1] == pytest.approx(t.position())
    assert exp_heads[-1] == pytest.approx(t.heading())
    assert len(heads) == len(exp_heads) and len(locs) == len(exp_locs)
    for i in range(len(exp_locs)):
        assert exp_heads[i] == pytest.approx(heads[i]) 
        assert exp_locs[i] == pytest.approx(locs[i])

def init_turtle():
    turtle.reset()
    turtle.clearscreen()
    turtle.setup(width=800, height=800)
    turtle.tracer(0)
    t = turtle.Turtle()
    t.left(90)
    return t

def cleanup_turtle():
    turtle.bye()
    turtle.Turtle._screen = None  
    turtle.TurtleScreen._RUNNING = True  