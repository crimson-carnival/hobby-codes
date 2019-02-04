import java.util.Scanner;
public class Coins {

    int money, num_coins, count, coins[];
    String final_denominations;

    public Coins() {
        money = num_coins = count = 0;
        final_denominations = "";
    }

    private void input() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Final sum: ");
        money = sc.nextInt();
        
        System.out.print("Number of coins: ");
        num_coins = sc.nextInt();
        
        System.out.print("Denominations: ");
        coins = new int[num_coins];
        for(int i = 0; i < num_coins; i++) coins[i] = sc.nextInt(); 
    }

    private void chain(int index, int sum, String denom_so_far) {
        int temp_sum = 0;
        String temp_denom = "";
        while(index < num_coins) {
            temp_sum = sum + coins[index];
            temp_denom = denom_so_far + " " + coins[index];
            if(temp_sum < money) {
                chain(index, temp_sum, temp_denom);
            }
            else if (temp_sum == money) {
                final_denominations += "\n" + temp_denom.trim();
                count++;
                return;
            }
            else return;
            index++;
        }
    }

    private void output() {
        System.out.println( (count > 0) ? final_denominations.trim() : -1);
    }

    public void run() {
        input();
        chain(0, 0, "");
        output();
    }

    public static void main(String args[]) {
        new Coins().run();
    }
}