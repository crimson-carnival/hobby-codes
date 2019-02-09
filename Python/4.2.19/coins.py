class Denominations():

    def __init__(self):
        self.money = 0
        self.num_coins = 0
        self.count = 0
        self.coins = []
        self.final_denominations = ""
    
    def input_data(self):
        self.money = int(input('Enter the number of coins: '))
        self.num_coins = int(input('Number of coins: '))
        self.coins = list(map(int, input('Enter the denominations: ').split()))

    def chain(self, index, sum, denom_so_far):
        temp_sum = 0
        temp_denom = ''
        while index < self.num_coins:
            temp_sum = sum + self.coins[index]
            temp_denom = denom_so_far + ' ' + str(self.coins[index])
            if(temp_sum < self.money):
                self.chain(index, temp_sum, temp_denom)
            elif (temp_sum == self.money):
                self.final_denominations += "\n" + temp_denom.strip()
                self.count += 1
                return
            else:
                return
            index += 1

    def output(self):
        if self.count != 0:
            print(self.final_denominations.strip('\n'))
        else:
            print(-1)

    def run(self):
        self.input_data()
        self.chain(0,0,'')
        self.output()

denominations = Denominations()
denominations.run()