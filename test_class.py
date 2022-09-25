import pytest
from main import add


class TestClass:

    @pytest.mark.parametrize("test_input,expected",
                             [
                                 ("", 0),
                                 ("2", 2),
                                 ("20", 20),
                                 ("2,3", 5),
                                 ("100,200", 300),
                                 ("2,4", 6),
                                 ("3,9", 12),
                                 ("1,2,3,4,5,6,7", 28),
                                 ("1,5,9", 15),
                                 ("20,100,200", 320),
                                 ("1\n2,3", 6),
                                 ("1\n2\n3\n4", 10),
                                 ("1,2\n3\n4,5", 15),
                                 ("//[;]\n1;2", 3),
                                 ("//[p]\n1p2p3p4p50", 60),
                                 ("//[;]\n1", 1),
                                 ("//[,]\n", 0),
                                 ("//[/]\n1/2", 3),
                                 ("//[;,]\n1;,2;,3", 6),
                                 ("1001", 0),
                                 ("25433", 0),
                                 ("5,3,6,1050", 14),
                                 ("12\n1000", 1012),
                                 ("1000\n1000,900", 2900),
                                 ("//[;]\n1000", 1000),
                                 ("//[;]\n1001", 0),
                                 ("//[;]\n1001;5;2", 7),
                                 ("//[p]\n1001p2000p3000", 0),
                                 ("//[***]\n1***2***3", 6),
                                 ("//[;,;]\n20;,;30;,;9", 59),
                                 ("//[,,]\n2000,,1", 1),
                                 ("//[;;]\n20003", 0),
                                 ("//[api]\n3api2api6", 11),
                                 ("//[.]\n1.2", 3),
                                 ("//[*][%]\n1*2%3", 6),
                                 ("//[*][%][,]\n1*2%3,3,3", 12),
                                 ("//[*][*]\n1*2*3", 6),
                                 ("//[*][%]\n1*2%3", 6),
                                 ("//[*][%%]\n1*2%%3", 6),
                                 ("//[*.,][%][,]\n1*.,2%3,6", 12),
                                 ("//[1]\n22136", 58),  # you can use numbers as delimiter
                                 ("//[+]\n1+1", 2),
                                 ("//[-]\n1-1", 2),
                                 ("//[a-a]\n1a-a1", 2),


                             ])
    def test_add_correct(self, test_input, expected):
        assert add(test_input) == expected

    @pytest.mark.parametrize("value",
                             [
                                 "s",
                                 "s,",
                                 "s, ",
                                 "s,1",
                                 "1,s",
                                 "1,2,3,4,s",
                                 "1,",
                                 "2,-",
                                 "-3,-",
                                 "1,\n",
                                 "s\n",
                                 "1\n",
                                 "1,2,3,4\n5\ns",
                                 "//[;]\n1,2",
                                 "//[;]\n1;2;3\n5",
                                 "/[;]/\n1;2",
                                 "//[1]\n2\n3",

                             ])
    def test_add_errors1(self, value):
        with pytest.raises(ValueError):
            add(value)

    @pytest.mark.parametrize("value",
                             [
                                 "//[;]1;2;3",
                                 "//[]1,2,3",
                                 "//[]\n1,2",
                                 "//[]\n1\n2",
                                 "//[\n]\n1\n1\n2"
                             ])
    def test_add_errors2(self, value):
        with pytest.raises(AttributeError):
            add(value)

    @pytest.mark.parametrize("value",
                             [
                                 "//[;]\n1;-2;3",
                                 "-1,2",
                                 "1\n-2",
                                 "-2",
                                 "//[;]\n-3"

                             ])
    def test_add_errors3(self, value):
        with pytest.raises(Exception, match='negatives not allowed'):
            add(value)

