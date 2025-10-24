import importlib.util, os, glob

def import_student():
    pyfiles = glob.glob("lab1_*.py")
    if not pyfiles:
        raise RuntimeError("Student file lab1_(ID).py not found")
    path = os.path.abspath(pyfiles[0])
    spec = importlib.util.spec_from_file_location("student_lab", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def test_number_functions():
    st = import_student()
    assert st.is_divisible(12, 4)
    assert not st.is_divisible(7, 3)
    assert st.gcd(24, 36) == 12
    assert st.mod_equiv(17, 5, 6)
    assert not st.mod_equiv(24, 14, 6)
    assert st.mod_exp(3, 4, 5) == pow(3, 4, 5)
    assert st.is_prime(17)
    assert not st.is_prime(15)
