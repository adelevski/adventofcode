import scala.io.Source


@main def day5() = {
    val fn: String = "data/smol.txt"
    val tb: Array[String] = Source.fromFile(fn).mkString.split("\n\n")
    println(tb)
    // val a = tb(0).split("\n").reverse.toList.tail.map(x => x.tail.grouped(4).map(_.head).toList)
    // println(a)
    // val lines: List[String] = Source.fromFile(fn).getLines.toList
    // println(lines)
}

