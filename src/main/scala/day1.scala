import scala.math.Ordering

def part1(input: String): Int =
  maxInventories(scanInventories(input), 1).head

def part2(input: String): Int =
  maxInventories(scanInventories(input), 3).sum

case class Inventory(items: List[Int])

def scanInventories(input: String): List[Inventory] =
  val inventories = List.newBuilder[Inventory]
  var items = List.newBuilder[Int]
  for line <- input.linesIterator do
    if line.isEmpty then
      inventories += Inventory(items.result())
      items = List.newBuilder
    else items += line.toInt
  inventories.result()

def maxInventories(inventories: List[Inventory], n: Int): List[Int] =
  inventories
    .map(inventory => inventory.items.sum)
    .sorted(using Ordering.Int.reverse)
    .take(n)