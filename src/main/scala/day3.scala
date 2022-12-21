import scala.io.Source

def lk(x: Char): Int = {
    val v1 = x.toInt - 'a'.toInt + 1
    val v2 = x.toInt - 'A'.toInt + 27
    val ret = if (v1 < 0) v2 else v1
    println(s"${x} -> ${ret}")
    ret
}

def eval(s1:String, s2:String, s3:String): Int = {
    s1.map(c => if (s2.indexOf(c) != -1 && s3.indexOf(c) != -1) lk(c) else 0).max
}

@main def day3() = {
    val lines: List[String] = Source.fromFile("data/day3.txt").getLines.toList
    val test = lines.grouped(3).map { x => eval(x(0), x(1), x(2)) }
    println(test.sum)
}