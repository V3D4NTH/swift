var a : Int = someOtherFunction(52);
var b : Int = someOtherFunction2(43);
a = someOtherFunction3(a,b);
b = someComplexFunction(42,42,42,42);

func someOtherFunction(b: Int) -> Int{
    for(var j: Int = 1; j < 32*42; j+= 1;){
        b *= j;
    }
    return b;
}
func someOtherFunction2(a:Int) -> Int{
    for(var j: Int = 0; j < 32*42; j+= 1;){
        a += j * 5;
    }
    return a;
}
func someOtherFunction3(a:Int, b:Int) -> Int{
    var c: Int = 0;
    for(var j: Int = 0; j < 32*42; j+= 1;){
        a += 1;
        b += 2;
    }
    return a;

}

func someComplexFunction(A: Int, B: Int, C: Int, D: Int)->Int {
    var someResult : Int = 42;
    for(var i : Int = 1; i < 20; i += 1;){
        for(var j : Int = 1; i < 20; j += 1;){
            for(var k : Int = 1; i < 20; k += 1;){
                for(var l : Int = 1; i < 20; l+= 1;){
                        someResult += A * B * C * D + i * j * l * l;
                    }
                }
            }
    }
    return someResult;
}

if( 52 > 43){
    a *= 32;

}
else {
    a -= 4;
}