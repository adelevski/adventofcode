import scala.io.Source

@main def main() = {
    val lines: List[String] = Source.fromfile("data.txt").getLines.toList
    println(lines)
}