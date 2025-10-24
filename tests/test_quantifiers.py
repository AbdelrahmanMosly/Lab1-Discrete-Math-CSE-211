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

def test_quantifiers_simple():
    st = import_student()
    domain = [1, 2, 3, 4, 5]
    assert st.check_universal(lambda x: x < 10, domain)
    assert st.check_existential(lambda x: x == 3, domain)
    assert not st.check_existential(lambda x: x < 0, domain)
