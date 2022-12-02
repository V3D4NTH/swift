var some_var: Int = 555;
func some_function(a: Int) -> Int {
    a += 111;
    return a;
}
var glob: Int = some_function(some_var);