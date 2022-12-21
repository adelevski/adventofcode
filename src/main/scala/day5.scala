import scala.io.Source


@main def day5() = {
    val lines: List[String] = Source.fromFile("data/day5.txt").getLines.toList
    println(lines)
}

