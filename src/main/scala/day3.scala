import scala.io.Source


def lk(x: Char): Int = {
    val v1 = x.toInt - 'a'.toInt + 1
    val v2 = x.toInt - 'A'.toInt + 27
    val ret = if (v1 < 0) v2 else v1
    println(s"${x} -> ${ret}")
    ret
}

def eval(x: String): Int = {
    val s1 = x.slice(0, x.length/2)
    val s2 = x.slice(x.length/2, x.length)
    val myval = s1.map(c => if (s2.indexOf(c) != -1) lk(c) else 0)
    myval.max
}

@main def day3() = {
    val lines: List[String] = Source.fromFile("data/day3.txt").getLines.toList
    println(lines.map(eval).sum)
}