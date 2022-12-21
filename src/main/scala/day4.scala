import scala.io.Source



def proc(x: String): Int = {
    val a  = x.split(",|-").map(_.toInt)
    if ((a(0) <= a(2) && a(3) <= a(1)) ||
    (a(2) <= a(0) && a(1) <= a(3))) 1 else 0
}


def proc2(x: String): Int = {
    val a = x.split(",|-").map(_.toInt)
    if ((a(1) < a(2)) ||
        (a(0) > a(3))) 0 else 1
}


@main def day4() = {
    val lines: List[String] = Source.fromFile("data/day4.txt").getLines.toList
    println(s"Part 1: ${lines.map(proc).sum}")
    println(s"Part 2: ${lines.map(proc2).sum}")
}

