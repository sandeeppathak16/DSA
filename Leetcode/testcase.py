def run_tests(func, test_cases, comparator=None):
    passed = 0

    for i, (inp, expected) in enumerate(test_cases, 1):
        try:
            if isinstance(inp, tuple):
                result = func(*inp)
            else:
                result = func(inp)

            if comparator:
                ok = comparator(result, expected)
            else:
                ok = result == expected

            if ok:
                print(f"Test {i}: PASS")
                passed += 1
            else:
                print(f"Test {i}: FAIL")
                print("  Input   :", inp)
                print("  Expected:", expected)
                print("  Got     :", result)

        except Exception as e:
            print(f"Test {i}: ERROR")
            print("  Input:", inp)
            print("  Error:", str(e))

    print(f"\n✅ Passed {passed}/{len(test_cases)} tests")