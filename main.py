import random
import json
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
    # print("result knapsack", total_amount)
    # print("total address used", count_address)
    return total_amount, count_address


if __name__ == "__main__":
    amount_send = 500
    value = [round(random.uniform(0.001, 10), 10) for _ in range(100)]
    # print(value)
    # value = [1, 5, 8, 15, 19, 25]
    # total of address in cluster
    # count = [10, 20, 7, 12, 10, 1]
    count = [random.randint(1, 100) for _ in range(100)]
    print(count)
    packs = []
    for i in range(len(value)):
        packs.append(Item(value[i], count[i]))
    packs.sort(reverse=True)
    f = open("btc_report.txt", "w")
    f.write("Input data \n")
    f.write('Amount cluster: ')
    json.dump(value, f)
    f.write("\n")
    f.write('Address in cluster: ')
    json.dump(count, f)
    f.write("\nTotal address {}".format(sum(count)))
    f.write('\n\n\nOutputs')
    for i in range(100):
        f.write("\n ============================================================== \n")
        amount_send = round(random.uniform(0.01, 10000), 10)
        f.write("Amount send: ")
        f.write(str(amount_send))
        f.write("\n")
        div_inputs = greedy(packs, amount_send)
        if len(div_inputs) > 1:
            total_send, count_address = knapsack(div_inputs, amount_send)
            f.write("Knapsack\n")
            f.write("Total send {} \nTotal address used {} \n".format(total_send, count_address))
        else:
            f.write("Greedy\n")
            f.write("Total send {} \nTotal address used {} \n".format(div_inputs[0].value, 1))
    f.close()
