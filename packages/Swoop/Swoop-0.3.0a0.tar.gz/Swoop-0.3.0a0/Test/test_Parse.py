import unittest
from pyparsing import *

class TestPyParse(unittest.TestCase):
    
    def setUp(self):
        pass

    @unittest.skipIf(True, "Disabled in production")
    def test_Parse(self):
        SIPrefixes = {"G" : 1e9,
                      "M" : 1e6,
                      "K" : 1e3,
                      "k" : 1e3,
                      "m" : 1e-3,
                      "u" : 1e-6,
                      "n" : 1e-9,
                      "p" : 1e-12,
                      "f" : 1e-15,
                      ""  : 1.0};

        def SIMagnitude(p):
            return SIPrefixes[p]



        class Identifier:
            def __init__(self, t):
                self.v = t[0][0]

            def __str__(self):
                return self.v
            
            def eval(self, env):
                return self.v
        
        class PredicateExpr:
            def __init__(self, t):
                self.lhs = t[0][0]
                self.op = t[0][1]
                self.rhs= t[0][2]

            def __str__(self):
                return " ".join(map(str,[self.lhs, self.op, self.rhs]))
            
            def eval(self, env):
                if isinstance(self.lhs, str):
                    l = env[self.lhs]
                else:
                    l = self.lhs

                if isinstance(self.rhs, str):
                    r = env[self.rhs]
                else:
                    r = self.rhs

                if self.op == "<" or self.op == "<=":
                    return l <= r
                elif self.op == ">" or self.op == ">=":
                    return l >= r
                elif self.op == "==":
                    return l == r
                elif self.op == "!=":
                    return l != r
                else:
                    assert False

        class TrinaryPredicateExpr:
            def __init__(self, t):
                self.lhs = t[0][0]
                self.lop = t[0][1]
                self.chs = t[0][2]
                self.rop = t[0][3]
                self.rhs = t[0][4]

            def __str__(self):
                return " ".join(map(str,[self.lhs, self.lop, self.chs, self.rop, self.rhs]))
            
            def eval(self, env):
                if isinstance(self.lhs, str):
                    l = env[self.lhs]
                else:
                    l = self.lhs

                if isinstance(self.rhs, str):
                    r = env[self.rhs]
                else:
                    r = self.rhs

                if isinstance(self.chs, str):
                    c = env[self.chs]
                else:
                    c = self.chs

                if self.lop == "<" or self.lop == "<=":
                    assert self.rop == "<" or self.rop == "<="

                if self.lop == ">" or self.lop == ">=":
                    assert self.rop == ">" or self.rop == ">="
                        
                if self.lop == "<" or self.lop == "<=":
                    lp = l <= c
                elif self.lop == ">" or self.lop == ">=":
                    lp = l >= c
                else:
                    assert False

                if self.rop == "<" or self.rop == "<=":
                    rp = c <= r
                elif self.rop == ">" or self.rop == ">=":
                    rp = c >= r
                else:
                    assert False

                return (lp and rp)

        class FloatConstant:
            def __init__(self, t):
                if type(t) is float:
                    self.v = t
                else:
                    print t
                    print type(t)
                    print t[0]
                    print type(t[0])
                    self.v = float(t[0])

            def __str__(self):
                return str(self.v)
            
            def eval(self, env):
                return self.v


        FLOAT = Regex('([+-]?(([1-9][0-9]*)|0+)(\.[0-9]*)?)').setParseAction(FloatConstant)

        BASE_UNIT = oneOf("F W V A Ohm m g")
        SI_PREFIX = oneOf(" ".join(SIPrefixes.keys()))

        class SIPrefix(FloatConstant):
            def __init__(self,t):
                FloatConstant.__init__(self,SIPrefixes[t[0]])
                
        SI_UNIT = Optional(SI_PREFIX("prefix"), "").setParseAction(SIPrefix) + BASE_UNIT("base_unit")

        class SIConstant(FloatConstant):
            def __init__(self, t):
                FloatConstant(t.num.v * t.mult.v)
            
        SI_CONSTANT = (FLOAT("num") + SI_UNIT("mult")).setParseAction(SIConstant)

        def Percent(FloatConstant):
            def __init__(self,t):
                FloatConstant.__init__(self, t[0].num.v * 0.01)

        PERCENT_CONSTANT = (FLOAT("num") + Literal("%").suppress()).setParseAction(Percent)
        CONSTANT = SI_CONSTANT | PERCENT_CONSTANT | FLOAT
        
        IDENTIFIER = Regex('[a-zA-Z_][a-zA-Z_0-9]*').setParseAction(lambda s,l,t: [Identifier(t)])

        ORDERING_OPERATOR = oneOf("< > >= <=")
        PREDICATE_OPERATOR = oneOf("== !=") | ORDERING_OPERATOR

                    
        TERM = CONSTANT | IDENTIFIER

        PREDICATE_EXPR = (TERM.setResultsName("lhs") +
                          PREDICATE_OPERATOR.setResultsName("op") +
                          TERM.setResultsName("rhs")).setParseAction(lambda s,l,t: [PredicateExpr(t.lhs, t.op, t.rhs)])

        TRINARY_PREDICATE_EXPR = (TERM("lhs") +
                                  PREDICATE_OPERATOR.setResultsName("lop") +
                                  TERM("chs") +
                                  PREDICATE_OPERATOR.setResultsName("rop") +
                                  TERM("rhs")).setParseAction(lambda s,l,t: [TrinaryPredicateExpr(t.lhs, t.lop, t.chs, t.rop, t.rhs)])

        EXPR = PREDICATE_EXPR | TRINARY_PREDICATE_EXPR | TERM
        #PLUS_MINUS = Literal("+/-")

        #PLUS_MINUS_RANGE = (CONSTANT("v") + PLUS_MINUS + CONSTANT("delta")).setParseAction(lambda s,l,t: (t.v - t.delta*t.v, t.v + t.delta*t.v))

        floatTests =["1.0", "1", "-2", "-0.0", "+4.2", "1", "-100", "1234.123445"];
        for t in floatTests:
            #print "r = " + str(FLOAT.parseString(t))
            #print "r1 = " + str(FLOAT.parseString(t)[0].eval({}))
            self.assertEqual(FLOAT.parseString(t)[0].eval({}), float(t), "Float parse error")
            #self.assertEqual(FLOAT.parseString(t)[0], float(t), "Float parse error")

        siTests=[("uF", {}, 1e-6), ("mA", {}, 1e-3), ("pV", {}, 1e-12), ("kW", {}, 1e3), ("MA", {}, 1e6)]
        for t in siTests:
            print "test = " + str(t)
            self.assertEqual(SI_UNIT.parseString(t[0])[0].eval(t[1]), t[2], "SI unit parse error")

        print "================================="
        
        percentTests = [("10%", {}, 0.1), ("10 %", {}, 0.1)]
        for t in percentTests:
            print "test = " + str(t)
            print PERCENT_CONSTANT.parseString(t[0])
            print PERCENT_CONSTANT.parseString(t[0])[0]
            print PERCENT_CONSTANT.parseString(t[0])[0].eval(t[1])
            self.assertEqual(PERCENT_CONSTANT.parseString(t[0]).eval(t[1]), t[2], "Percent parse error")
            #self.assertEqual(PERCENT_CONSTANT.parseString(t[0])[0], t[2], "Percent parse error")

        siConstantTests =[("1.0F", {},1.0), ("1 A", {},1), ("-2V", {},-2), ("-0.0W", {},0), ("+4.2A", {},4.2), ("1F", {},1), ("-100W", {},-100), (" 1234.123445 V", {},1234.123445)]
        for t in siConstantTests:
            #print t
            self.assertEqual(SI_CONSTANT.parseString(t[0])[0].eval(t[1]), t[2], "Dimensionsed constant parse error")

        constantTests = [("1.0F", {},1.0), ("1 A", {},1), ("-2V", {},-2), ("-0.0W", {},0), ("+4.2A", {},4.2), ("1F", {},1), ("-100W", {},-100), (" 1234.123445 V", {},1234.123445)]
        for t in constantTests:
            #print t
            self.assertEqual(CONSTANT.parseString(t[0])[0].eval(t[1]), float(t[2]), "Float parse error")

        constantTests2 = [("1.0uF", {},1.0*1e-6), ("1 mA",{}, 1*1e-3),
                          ("-2MV", {},-2*1e6), ("-0.0nW", {},0),
                          ("+4.2A", {},4.2), ("1pF", {},1*1e-12),
                          ("-100kW",{}, -100*1e3), ("-100fW", {},-100*1e-15),
                          ("10%",{}, 10*.01)]
        for t in constantTests2:
            #print t
            self.assertEqual(CONSTANT.parseString(t[0])[0].eval(t1), t[2], "Float parse error")

        self.assertEqual(PredicateExpr(0, "<", 10).eval({}),  True, "Predicate expr error")
        self.assertEqual(PredicateExpr(0, ">", 10).eval({}),  False, "Predicate expr error")
        self.assertEqual(PredicateExpr(0, "!=", 10).eval({}), True, "Predicate expr error")
        self.assertEqual(PredicateExpr(0, "==", 0).eval({}),  True, "Predicate expr error")
        self.assertEqual(PredicateExpr("x", "==", 0).eval({"x":0}), True, "Predicate expr error")
        self.assertEqual(PredicateExpr("x", "<", "y").eval({"x":0, "y": 10}), True, "Predicate expr error")

        predicateExprTests = [("x < 10", {"x":5}, True),
                              ("x>y", {"x":1,"y":2}, False),
                              ("x!= 10", {"x":4}, True),
                              ("x < 10pF", {"x":0}, True),
                              ("1pF < 1uF", {}, True)]

            
        for t in predicateExprTests:
            r = PREDICATE_EXPR.parseString(t[0])
            self.assertEqual(r[0].eval(t[1]), t[2], "Predicate expr error")

        trinaryPredicateTests = [("0 < x < 10", {"x":5}, True),
                                 ("0 > x > 10", {"x":5}, False),
                                 ("0 >= x > 10", {"x":5}, False),
                                 ("1uF < x < 10MF", {"x": 10*1e-6}, True)]

        for t in trinaryPredicateTests:
            r = TRINARY_PREDICATE_EXPR.parseString(t[0])
            self.assertEqual(r[0].eval(t[1]), t[2], "Predicate expr error")

        
        for t in predicateExprTests + trinaryPredicateTests + constantTests2:
            r = EXPR.parseString(t[0])
            self.assertEqual(r[0].eval(t[1]), t[2], "Predicate expr error")
            
