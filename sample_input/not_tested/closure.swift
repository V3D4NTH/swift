var some_param: Int = 1000;
let something = { (some_param) -> Int in
        var number = some_param;
        repeat {
            number /= 10;
        } while number > 0
        return number;
    }