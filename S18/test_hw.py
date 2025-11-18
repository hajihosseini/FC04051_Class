import hw
import pytest

@pytest.mark.skip("Not Implemented")
def test_is_prime():
    out1 = hw.is_prime(1)
    assert out1==False

    out2 = hw.is_prime(2)
    assert out2==True

    out3 = hw.is_prime(17)
    assert out3==True

    out4 = hw.is_prime(55)
    assert out4==False

    out5 = hw.is_prime(1009)
    assert out5==True

@pytest.mark.skip("Not Implemented")
def test_BMM():
    out1 = hw.BMM(1,10)
    assert out1==1

    out2 = hw.BMM(8,12)
    assert out2==4

    out3 = hw.BMM(5,7)
    assert out3==1

    out4 = hw.BMM(4,16)
    assert out4==4

    out5 = hw.BMM(6,9)
    assert out5==3
