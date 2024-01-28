import heapq


def calculate_order(entities):
    heap = entities[:]
    heapq.heapify(heap)
    order_counter = 1
    sum_entities = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        first_and_second = first + second
        print(f"Step {order_counter}: connect { first } and { second}, cost: {first_and_second}")
        sum_entities += first_and_second
        heapq.heappush(heap, first_and_second)
        print(f"Current entities: {heap}")
        order_counter += 1
    print(f"Connection costs: {sum_entities}")


if __name__ == "__main__":
    cable_entities = [1, 2, 4, 10]
    calculate_order(cable_entities)
