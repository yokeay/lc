class Test:
    def test(self, str):
        # for s in str:
        #     print(ord(s))
        val = sum([ord(s) for s in str])
        print(val)

if __name__ == '__main__':
    # s = Test()
    # s.test("abc")
    a = [1,1,1,1,2,3,4,5]
    dict = {i-1:i for i in a}
    # print(set(a))
    print(dict)
