from point import Point

def test_bound_instance_method():
    p = Point()
    p.set_x(10)
    p.set_y(10)
    p.show()
    print(p.get_x(), p.get_y(), sep=',')

def test_unbound_class_method():
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    Point.show(p)
    print(Point.get_x(p),Point.get_y(p))

def test_other_method():
    # 어노테이션 추가하여 호출방식이 변경됨
    # print(Point.class_method(Point))
    print(Point.class_method())
    print(Point.static_method())

def main():
    test_bound_instance_method()
    test_unbound_class_method()
    test_other_method()

if __name__ == '__main__':
    main()