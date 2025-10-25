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

def test_nested_quantifiers():
    st = import_student()
    domain_x = [1, 2, 3]
    domain_y = [1, 2, 3]

    def P(x, y): return x < y
    results = st.nested_quantifiers(P, domain_x, domain_y)

    # Ensure the dictionary has all four keys
    expected_keys = {"forall_forall", "forall_exists", "exists_forall", "exists_exists"}
    assert set(results.keys()) == expected_keys

    # Just check for correct logical pattern for this simple predicate
    assert results["forall_forall"] is False
    assert results["forall_exists"] is False
    assert results["exists_forall"] is False
    assert results["exists_exists"] is True

