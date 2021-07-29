class Item(object):
    def __init__(self, value, count):
        self.value = value
        self.count = count
        self.remain = count
        self.used = self.count - self.remain

    def decrease_remain(self):
        if self.remain - 1 > 0:
            self.remain -= 1
            self.used += 1

    def __lt__(self, other):
        return self.value < other.value

    def print(self):
        print(self.value, self.used)

def greedy(packs, amount) :
    lessers = [item for item in packs if item.value < amount]
    greaters = [item for item in packs if item.value >= amount]

    if greaters:
        min_greater = min(greaters)
        return [min_greater]
    return lessers


def knapsack(packs, amount_send):
    result = []
    total_amount = 0
    stop = False
    i = 0
    count_address = 0
    while not stop:
        if packs[i].value >= amount_send:
            packs[i].decrease_remain()
            result.append(packs[i])
            count_address += 1
            print("result", result)
            break

        for k in range(packs[i].count):
            total_amount += packs[i].value
            packs[i].decrease_remain()
            result.append(packs[i])
            count_address += 1
            if total_amount >= amount_send:
                break

        if total_amount >= amount_send:
            stop = True
        i += 1
        if i > len(value) - 1:
            stop = True
        print("result knapsack", total_amount)
        print("total address used", count_address)


if __name__ == "__main__":
    amount_send = 5
    value = [1, 5, 8, 15, 19, 25]
    count = [10, 20, 7, 12, 10, 1]
    packs = []
    for i in range(len(value)):
        packs.append(Item(value[i], count[i]))

    packs.sort(reverse=True)
    div_inputs = greedy(packs, amount_send)
    if len(div_inputs) > 1:
        knapsack(div_inputs, amount_send)
    else:
        print("result greedy", div_inputs[0].value)
        print("total address used", 1)